import test from "node:test";
import assert from "node:assert/strict";
import worker from "../src/index.ts";

function call(path, options = {}, assets) {
  const env = {
    ASSETS: assets ?? { fetch: async () => new Response("asset", { status: 200 }) },
  };
  return worker.fetch(new Request("https://example.test" + path, options), env);
}

test("health JSON dan tidak dapat dicache", async () => {
  const response = await call("/healthz");
  assert.equal(response.status, 200);
  assert.deepEqual(await response.json(), { ok: true });
  assert.equal(response.headers.get("cache-control"), "no-store");
});

test("hello masuk handler API dan bukan aset", async () => {
  const response = await call("/api/hello", {}, {
    fetch: async () => { throw new Error("ASSET_MUST_NOT_RUN"); },
  });
  assert.equal(response.status, 200);
  assert.equal(typeof (await response.json()).message, "string");
});

test("API tidak dikenal tetap JSON 404", async () => {
  for (const path of ["/api", "/api/typo", "/api/hello/other"]) {
    const response = await call(path);
    assert.equal(response.status, 404);
    assert.match(response.headers.get("content-type"), /application\/json/);
    assert.equal((await response.json()).error, "NOT_FOUND");
  }
});

test("metode tulis ditolak tanpa operasi aset", async () => {
  const response = await call("/api/hello", { method: "POST" });
  assert.equal(response.status, 405);
  assert.equal(response.headers.get("allow"), "GET, HEAD");
});

test("HEAD pada health dan API tidak memiliki body", async () => {
  for (const path of ["/healthz", "/api/hello", "/api/typo"]) {
    const response = await call(path, { method: "HEAD" });
    assert.equal(await response.text(), "");
    assert.equal(response.status, path.endsWith("typo") ? 404 : 200);
  }
});

test("rute web menggunakan binding ASSETS", async () => {
  const response = await call("/");
  assert.equal(await response.text(), "asset");
});

test("detail error internal tidak dibuka ke client", async () => {
  const response = await call("/", {}, {
    fetch: async () => { throw new Error("PRIVATE_PROVIDER_DETAIL"); },
  });
  assert.equal(response.status, 500);
  const text = await response.text();
  assert.ok(!text.includes("PRIVATE_PROVIDER_DETAIL"));
  assert.equal(JSON.parse(text).error, "INTERNAL_ERROR");
});

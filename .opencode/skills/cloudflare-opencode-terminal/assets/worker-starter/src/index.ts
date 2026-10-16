function json(
  body: Record<string, unknown>,
  status = 200,
  extraHeaders: Record<string, string> = {},
): Response {
  return Response.json(body, {
    status,
    headers: {
      "Cache-Control": "no-store",
      "X-Content-Type-Options": "nosniff",
      ...extraHeaders,
    },
  });
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const requestId = crypto.randomUUID();
    const url = new URL(request.url);
    const isApi = url.pathname === "/api" || url.pathname.startsWith("/api/");
    const isHealth = url.pathname === "/healthz";

    if (isApi || isHealth) {
      if (request.method !== "GET" && request.method !== "HEAD") {
        return json({ error: "METHOD_NOT_ALLOWED", request_id: requestId }, 405, {
          Allow: "GET, HEAD",
        });
      }

      let response: Response;
      if (isHealth) {
        response = json({ ok: true });
      } else if (url.pathname === "/api/hello") {
        response = json({ message: "Halo dari Cloudflare Workers." });
      } else {
        response = json({ error: "NOT_FOUND", request_id: requestId }, 404);
      }
      return request.method === "HEAD"
        ? new Response(null, { status: response.status, headers: response.headers })
        : response;
    }

    try {
      return await env.ASSETS.fetch(request);
    } catch {
      console.error(JSON.stringify({
        event: "asset_error",
        request_id: requestId,
      }));
      return json({ error: "INTERNAL_ERROR", request_id: requestId }, 500);
    }
  },
} satisfies ExportedHandler<Env>;

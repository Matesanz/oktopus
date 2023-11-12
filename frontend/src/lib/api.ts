
import { env } from '$env/dynamic/public'

const API_HOST = env.PUBLIC_API_HOST || 'localhost'
const API_PORT = env.PUBLIC_API_PORT || 8080
const IS_LOCAL = API_HOST == 'localhost'
// const API_HOST = IS_PROD ? 'oktopus-m3z38.ondigitalocean.app' : 'localhost'
const METHOD = IS_LOCAL ? 'http' : 'https'

export const api_url = `${METHOD}://${API_HOST}${IS_LOCAL ? `:${API_PORT}` : ''}`;

export async function get_all_documents() {
    let res = await fetch(`${api_url}/documents`);
    return res.json();
}

export async function post_query(query: string) {
    let res = await fetch(`${api_url}/search`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json'
        },
        body: JSON.stringify({ query: query })
    });
    return await res.json()
}

export async function get_document_info(id: number) {
    let res = await fetch(`${api_url}/documents/${id}`);
    return await res.json();
}
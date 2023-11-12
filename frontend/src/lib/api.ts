
const IS_PROD = import.meta.env.PROD
const API_PORT = import.meta.env.VITE_PUBLIC_API_PORT || 8080
const API_HOST = IS_PROD ? 'oktopus-m3z38.ondigitalocean.app' : 'localhost'
const METHOD = IS_PROD ? 'https' : 'https'

export const api_url = `${METHOD}://${API_HOST}${IS_PROD ? '' : `:${API_PORT}`}`;
console.log(api_url);

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
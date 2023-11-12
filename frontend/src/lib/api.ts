
const API_HOST = import.meta.env.VITE_PUBLIC_API_HOST || 'localhost'
const API_PORT = import.meta.env.VITE_PUBLIC_API_PORT || 8080
const IS_DEV = API_HOST == 'localhost'

export const api_url = `${IS_DEV ? 'http' : 'https'}://${API_HOST}${IS_DEV ? `${API_PORT}` : ''}`;

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
const API_HOST = import.meta.env.API_HOST || 'localhost';
const API_PORT = import.meta.env.API_PORT || 8080;
export const api_url = `http://${API_HOST}:${API_PORT}`;

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
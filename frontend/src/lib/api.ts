let api_url = 'http://localhost:8015';

export async function get_all_documents() {
    let res = await fetch(`${api_url}/documents`);
    return res.json();
}

export async function post_query(query: string) {
    let res = await fetch(`${api_url}/generate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json'
        },
        body: JSON.stringify({ query: query })
    });
    let matches = await res.json();
    return matches.map((x: any) => x[0]);
}

export async function get_document_info(id: number) {
    let res = await fetch(`${api_url}/documents/${id}`);
    return res.json();

}
<script>
	import { onMount } from 'svelte';

	const API_URL = '127.0.0.1';
	let query = '';

	let documents = [];
	let best;
	let chartCanvas;

	onMount(async () => {
		documents = await get_documents();
		draw_docs(documents);
	});

	async function get_documents() {
		alert(`beep bop beep.... GET!`);
		return [1, 2, 3, 4, 5, 6];
	}

function draw_docs(data) {
	let ctx = chartCanvas.getContext('2d');
		let chart = new chartjs(ctx, {
			type: 'line',
			data: {
					labels: chartLabels,
					datasets: [{
							label: 'Revenue',
							backgroundColor: 'rgb(255, 99, 132)',
							borderColor: 'rgb(255, 99, 132)',
							data: chartValues
					}]
            		}
 }}

	async function send_query() {
		alert(`beep bop beep.... \`${query}\``);
		return [2, 4, 6];
	}
</script>

<section class="hero is-fullheight">
	<div class="hero-body">
		<div class="container has-text-centered">
			<h1 class="title">Oktopus</h1>
			<div class="field has-addons">
				<div class="control">
					<input
						class="input"
						type="text"
						placeholder="Look for insight"
						bind:value={query}
						on:keydown={(e) => {
							if (e.key == 'Enter') {
								best = send_query();
							}
						}}
					/>
				</div>
				<div class="control">
					<button class="button is-info is-bold" on:click={send_query}>Search</button>
				</div>
			</div>
		</div>
	</div>
</section>

chart:
<canvas bind:this={chartCanvas} id="myChart" />
end

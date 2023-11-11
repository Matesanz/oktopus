<script lang="ts">
	import Chart from 'svelte-frappe-charts';

	let query: string = '';
	let translateY = 0;

	let data = {
		labels: ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'],
		datasets: [
			{
				values: [10, 12, 3, 9, 8, 15, 9]
			}
		]
	};
	let chartRef;

	function send_query() {
		alert(`beep bop beep.... \`${query}\``);
	}

	function handleEnter({ key }: any) {
		if (key === 'Enter') {
			submit(query);
		}
	}

	function submit(query: string) {
		window.alert(`API call with query: ${query}`);
	}
</script>

<svelte:window on:keyup={handleEnter} />

<section class="hero is-fullheight">
	<div class="hero-body">
		<div class="container is-centered has-text-centered">
			<h1 class="title">Oktoopus</h1>
			<div class="columns is-centered to-bottom">
				<div class="column is-three-fifths is-justify-content-center">
					<div class="field has-addons is-justify-content-center">
						<div class="control is-expanded">
							<input class="input" type="text" placeholder="Look for insight" bind:value={query} />
						</div>
						<div class="control">
							<button class="button is-bold is-primary is-rounded" on:click={() => submit(query)}
								>Search</button
							>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<Chart {data} bind:this={chartRef} />

<script lang="ts">
	import { Node } from 'svelvet';

	export let title: string;
	export let x: number;
	export let y: number;
</script>

<Node position={{ x: x, y: y }}>
	<h1>{title}</h1>
</Node>

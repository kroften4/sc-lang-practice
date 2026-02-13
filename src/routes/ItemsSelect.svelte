<script lang="ts">
	import Item from './Item.svelte';
	import Fuse from 'fuse.js';

	let { langData, engLangData } = $props();
	let filteredList: any[] = $state([]);

	let searchTerm = $state('');

	type Item = {
		key: string;
		original: string;
		translated: string;
	};

	const fuseOptions = {
		keys: ['key', 'original', 'translated'],
		threshold: 0.29
	};
	let fuse: any;
	let allItems: Item[] = [];
	$effect(() => {
		allItems = [];
		for (let itemName in langData) {
			allItems.push({
				key: itemName,
				original: engLangData[itemName],
				translated: langData[itemName]
			});
		}
		fuse = new Fuse(allItems, fuseOptions);
	});

	$effect(() => {
		filteredList = fuse.search(searchTerm);
	});
</script>

<input bind:value={searchTerm} class="m-1 border-2" />

{#each filteredList as item}
	<Item
		name={item.item.key}
		englishVariant={item.item.original}
		translation={item.item.translated}
	/>
{/each}

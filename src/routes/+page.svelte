<script lang="ts">
	import langList from '$lib/data/langlist.json';
	import categoriesData from '$lib/data/categories.json';
	import Dropdown from '$lib/Dropdown.svelte';
	import type { Dictionary } from '$lib/types/Dictionary';

	let langNames = langList.map((name: string) => name.split('.')[0]).sort();

	type Category = { name: string; useful: string[]; other: string[] };
	// TODO: prepare CategoriesData (parse and shit)
	let categories: Dictionary<Category> = $state(categoriesData);

	let selectedLangName = $state(langNames[0]);
	let selectedLangData = $state(null);
	$effect(() => {
		fetch(`/langfiles/${selectedLangName}.json`)
			.then((r) => r.json())
			.then((r) => {
				selectedLangData = r;
			});
		return;
	});

	let selectedCategoryId: string = $state(Object.keys(categories)[1]);
	let selectedCategory: Category = $derived(categories[selectedCategoryId]);

	function addCategory(id: string, item: Category) {
		categories[id] = item;
	}

	$inspect(categories);
	$inspect(selectedCategoryId);
	$inspect(selectedCategory);
</script>

<h1>Search Crafting Language Learning</h1>

<label for="lang-select">Language: </label>
<Dropdown id="lang-select" bind:value={selectedLangName} contents={langNames} />
<br />
<!-- <label for="category-select">Category: </label> -->
<Dropdown
	id="category-select"
	bind:value={selectedCategoryId}
	values={Object.keys(categories)}
	contents={Object.values(categories).map((it) => it.name)}
/>

<button>+</button>

{#if selectedLangData}
	<p>
		Loaded {selectedLangData['language.name']}
		({selectedLangData['language.region']})
	</p>

	{#each selectedCategory.useful as usefulItem}
		<b>{usefulItem}:</b>
		<div class="mc-font" style:display="inline">
			{selectedLangData[usefulItem]}
		</div>
        <br>
	{/each}
{:else}
	<p>Loading...</p>
{/if}

<style>
	:root {
		margin: 5px;
	}

	@font-face {
		font-family: Minecraft; /* set name */
		src: url(/fonts/MinecraftDefault-Regular.ttf); /* url of the font */
	}
	.mc-font {
		font-family: Minecraft;
		font-size: 23px;
	}

	button {
		outline: 2px solid black;
		padding: 3px 10px;
	}
</style>

<script lang="ts">
	import langList from '$lib/data/langlist.json';
	import engLangData from '$lib/data/en_gb.json';
	import categoriesData from '$lib/data/categories.json';
	import ItemsSelect from './ItemsSelect.svelte';
	import Dropdown from '$lib/Dropdown.svelte';
	import type { Dictionary } from '$lib/types/Dictionary';
	import Item from './Item.svelte';

	let langNames = langList.map((name: string) => name.split('.')[0]).sort();
	let langKeys = Object.keys(engLangData);

	type Category = { name: string; useful: string[]; other: string[] };
	prepareCategories(categoriesData);
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

	let selectedCategoryId: string = $state(Object.keys(categories)[0]);
	let selectedCategory: Category = $derived(categories[selectedCategoryId]);

	let searchTerm = '';

	function addCategory(id: string, item: Category) {
		categories[id] = item;
	}

	function prepareCategories(dict: Dictionary<Category>) {
		for (let category in dict) {
			let usefulSet = prepareCategoryList(dict[category].useful);
			dict[category].useful = Array.from(usefulSet);

			let otherSet = prepareCategoryList(dict[category].other);
			dict[category].other = Array.from(otherSet.difference(usefulSet));
		}
	}

	function prepareCategoryList(list: string[]): Set<string> {
		let result: Set<string> = new Set();
		for (let item of list) {
			if (langKeys.includes(item)) {
				result.add(item);
				continue;
			}
			// abc.dbe.* -> abc.dbe.item
			// TODO: handle * in the middle
			if (item.endsWith('*')) {
				let term = item.slice(0, -1);
				let filtered = langKeys.filter((it) => it.startsWith(term));
				result = result.union(new Set(filtered));
			} else {
				console.warn(`${item} not found`);
			}
		}
		return result;
	}
</script>

<h1 class="m-2 text-center text-3xl font-bold">
	Search Crafting Language Learning
</h1>

<div
	class="inline-block w-full content-center border-2 bg-indigo-200
    p-2"
>
	<label for="lang-select">Language: </label>
	<Dropdown
		id="lang-select"
		bind:value={selectedLangName}
		contents={langNames}
		--outline-width="2px"
		--bg-color="var(--color-violet-200)"
	/>
	<label for="category-select">Category: </label>
	<Dropdown
		id="category-select"
		bind:value={selectedCategoryId}
		values={Object.keys(categories)}
		contents={Object.values(categories).map((it) => it.name)}
		--outline-width="2px"
		--bg-color="var(--color-violet-200)"
	/>
	<button class="bg-violet-200 px-[9px] py-[2px] outline-2"> + </button>
</div>

{#if selectedLangData}
	<ItemsSelect langData={selectedLangData} {engLangData} />
{/if}

<!-- {#if selectedLangData} -->
<!-- 	<p> -->
<!-- 		Loaded {selectedLangData['language.name']} -->
<!-- 		({selectedLangData['language.region']}) -->
<!-- 	</p> -->
<!---->
<!-- 	<br /> -->
<!-- 	<h1>Useful</h1> -->
<!-- 	{#each selectedCategory.useful as usefulItem} -->
<!-- 		<b>{usefulItem}:</b> -->
<!-- 		<div class="mc-font inline text-lg"> -->
<!-- 			{selectedLangData[usefulItem]} -->
<!-- 		</div> -->
<!-- 		<br /> -->
<!-- 	{/each} -->
<!-- 	<br /> -->
<!---->
<!-- 	<h1>Other</h1> -->
<!-- 	{#each selectedCategory.other as item} -->
<!-- 		<b>{item}:</b> -->
<!-- 		<div class="mc-font inline text-lg"> -->
<!-- 			{selectedLangData[item]} -->
<!-- 		</div> -->
<!-- 		<br /> -->
<!-- 	{/each} -->
<!-- {:else} -->
<!-- 	<p>Loading...</p> -->
<!-- {/if} -->
<!---->
<style>
	:root {
		margin: 5px;
		background-color: var(--color-violet-100);
	}

	@font-face {
		font-family: Minecraft;
		size-adjust: 130%;
		src: url(/fonts/MinecraftDefault-Regular.ttf);
	}
	@font-face {
		font-family: 'GNU Unifont';
		src: url(/fonts/unifont-17.0.03.otf);
	}
	@font-face {
		font-family: 'GNU Unifont Japanese';
		src: url(/fonts/unifont_jp-17.0.03.otf);
	}
	.mc-font {
		font-family: Minecraft, 'GNU Unifont', 'GNU Unifont Japanese';
	}
</style>

<script lang="ts">
	import langList from '$lib/data/all-mc-lang-list.json';
	import categoriesData from '$lib/data/categories.json';

	langList.sort();
	let categoryNames = categoriesData.map((it) => it.name);
	categoryNames.push('enchantments', 'custom');
    categoryNames.sort();

	let selectedLangName = $state(langList[0]);
	let selectedLang = $state(null);
	let selectedCategory = $state(categoryNames[0]);

	$effect(() => {
		fetch(`/all-mc-lang/${selectedLangName}`)
			.then((r) => r.json())
			.then((r) => {
				selectedLang = r;
			});
		return;
	});
</script>

<h1>Search Crafting Language Learning</h1>

<label for="lang-select">Language: </label>
<select
	id="lang-select"
	bind:value={selectedLangName}
	style:outline="2px solid"
>
	{#each langList as lang}
		<option value={lang}>{lang.split('.')[0]}</option>
	{/each}
</select>

<label for="category-select">Category: </label>
<select
	id="category-select"
	bind:value={selectedCategory}
	style:outline="2px solid"
>
	{#each categoryNames as categoryName}
		<option >{categoryName}</option>
	{/each}
</select>

{#if selectedLang}
	<p>
		Loaded {selectedLang['language.name']}
		({selectedLang['language.region']})
	</p>
	<p>
		Distract piglin:
		{selectedLang['advancements.nether.distract_piglin.title']}
	</p>
	<p>
		Crying obi: {selectedLang[
			'advancements.nether.obtain_crying_obsidian.title'
		]}
	</p>
{:else}
	<p>Loading...</p>
{/if}

<script lang="ts">
	import langList from '$lib/data/all-mc-lang-list.json';
	langList.sort();
	let selectedLangName = $state(langList[0]);
	let selectedLang = $state(null);

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

<select bind:value={selectedLangName} style:outline="2px solid">
	{#each langList as lang}
		<option value={lang}>{lang.split('.')[0]}</option>
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

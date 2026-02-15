<script>
	import ItemSearch from './ItemSearch.svelte';
	let { langData, engLangData } = $props();
</script>

<ItemSearch {langData} {engLangData} />

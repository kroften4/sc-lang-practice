<script lang="ts">
	let { name, englishVariant, translation } = $props();
</script>

<div class="flex my-1 py-1 border-2 bg-slate-200">
	<input type="checkbox" class="m-2 size-5 place-self-center"/>
	<div>
		<div class="text-slate-600 text-base font-medium">{name}</div>
		<div>{englishVariant}</div>
		<div>{translation}</div>
	</div>
</div>

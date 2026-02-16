# Linux Sys Admin - Card Template

This note type has one card template: Concept -> Meaning.

## Card Template

### Front
```
{{Concept}}
```

### Back
```
<div id="meaning">{{Meaning}}</div>
<script>
const el = document.getElementById("meaning");
el.innerHTML = el.textContent.replace(/\\n/g, "<br>").replace(/;\s*/g, "<br>");
</script>
```

## Notes

- Front shows only `Concept`
- Back shows only `Meaning`

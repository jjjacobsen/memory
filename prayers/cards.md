# Prayers - Card Templates

This note type has two card templates.

## 1. Prayer Name -> Prayer Text

### Front
```
<div class=prayer-title>{{Front}}</div>
```

### Back
```
{{FrontSide}}

<hr id=answer>

<div class=prayer-text id=card1-prayer>{{Back}}</div>
<script>
const el = document.getElementById(`card1-prayer`);
el.innerHTML = el.textContent.replace(/;;/g, `<br><br>`).replace(/;\s*/g, `<br>`);
</script>
```

## 2. Prayer Text -> Prayer Name

### Front
```
<div class=prayer-text id=card2-prayer>{{Back}}</div>
<script>
const el = document.getElementById(`card2-prayer`);
el.innerHTML = el.textContent.replace(/;;/g, `<br><br>`).replace(/;\s*/g, `<br>`);
</script>
```

### Back
```
{{FrontSide}}

<hr id=answer>

<div class=prayer-title>{{Front}}</div>
```

## Styling

```
.card {
  font-size: 24px;
  text-align: center;
}

.prayer-title {
  font-size: 1.2em;
  font-weight: 600;
}

.prayer-text {
  line-height: 1.5;
  text-align: left;
  white-space: normal;
}
```

## Notes

- Your current bare `{{Front}}` and `{{Back}}` setup will work
- This version is better for prayers because the name stays clean and the prayer body renders with real line breaks
- The reverse card stays useful without making the note type more complicated

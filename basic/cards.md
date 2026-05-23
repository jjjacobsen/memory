# Basic - Card Template

This note type has one card template: Front -> Back.

## Card Template

### Front
```
{{Front}}
```

### Back
```
{{FrontSide}}

<hr id=answer>

{{Back}}
```

### Styling
```css
.card {
  font-family: arial;
  font-size: 20px;
  text-align: center;
  color: black;
  background-color: white;
}
```

## Notes

- Front shows only `Front`
- Back shows the front side, the answer separator, then `Back`

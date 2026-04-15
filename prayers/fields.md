# Prayers - Field Structure

This note type stores prayer names and prayer text.

## Fields

1. **Front** - The prayer name or prompt
2. **Back** - The full prayer text

## Format

Each note follows the pipe-delimited format:
```
Front|Back
```

## Example

```
A Huguenot Prayer at Mealtime|Eternal Father, who commanded; “Take not tomorrow’s cares today”,; For this day’s bounty, freely granted,; Our simple, earnest, thanks we say.; And since it pleased You to convey; The earthly food and drink You’ve given,; So may it please You now, we pray,; To feed our souls with Bread from Heaven.;; Jacobus Clemens non Papa, 1510–1556; translated by Peter Maurice
```

## Notes

- Keep fields in this exact order: `Front|Back`
- Keep each note on one line for reliable import
- Use `;` inside `Back` for a line break
- Use `;;` inside `Back` for a blank line, such as before attribution
- Keep `Front` short and recognizable

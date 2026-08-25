# Design workflow evidence audit

Use this audit only when checking whether the complete design-adoption workflow occurred in real
artifacts. `planned`, `documented`, `visible`, and `verified` are different states.

## Canonical stage order

1. `user_request`: approved brief or original request
2. `director_direction`: purpose, hierarchy, distinct directions, exclusions
3. `reference_selection`: source, access date, license, selected part, do-not-copy
4. `draft_recipe`: stable Section IDs, selected properties, exclusions, source hashes
5. `visual_target`: real or approved fixture data, fixed viewport, visible result
6. `direction_approval`: explicit user decision and reason
7. `implementation_handoff`: approved Recipe and component/assets given to one implementer
8. `product_implementation`: product commit or isolated result artifact
9. `independent_verification`: Fidelity, interaction, console, responsive and unchanged-area checks
10. `final_user_approval`: explicit decision on the implemented result
11. `version_restore`: new applied Version and demonstrated Restore point

The Draft Recipe begins when references and properties are selected. Direction approval promotes the
same Recipe lineage; it does not create an unrelated Recipe after the decision.

## Required output

For every stage report:

```yaml
stage:
  status: proven | partial | not_proven | failed
  evidence_files: []
  input_hash_or_version:
  output_hash_or_version:
  user_decision:
  limits: []
```

The overall verdict is:

- `PASS`: all eleven stages are proven and hashes or Versions join adjacent stages;
- `PASS_WITH_FIX`: the product result is proven but a non-destructive record is incomplete;
- `BLOCKED`: implementation, independent verification, final approval, or Restore is missing;
- `FAIL`: an adjacent stage consumes a different unapproved input, or a regression is detected.

Never repair missing evidence by rewriting historical artifacts. Continue from the first missing
handoff in a new Draft or Run.

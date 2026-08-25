# Design finish gates

Technical and visual quality are separate. Mark a Gate `pass`, `fail`, or `not_required`; never infer missing evidence as `pass`.

## Design quality

- `design_specificity`: the result has a brief-specific visual point of view and does not look
  like an interchangeable AI dashboard template.
- `diversity_integrity`: when alternatives were requested, their Design DNA differs on at least
  three relevant axes rather than color alone.
- `information_priority`: the first task and primary action are visually obvious.
- `spacing_consistency`: spacing follows the selected scale without accidental gaps.
- `typography_hierarchy`: headings, labels, body, and metadata have distinct readable roles.
- `component_state_completeness`: default, hover, focus, disabled, loading, empty, error, and success states exist where applicable.
- `border_and_surface_clarity`: panels remain distinguishable without excessive decoration.
- `responsive_quality`: required viewports retain order, readable type, and usable actions.
- `motion_purpose`: motion explains state or spatial change and respects reduced motion, or is not required.
- `reference_fidelity`: only selected properties are carried from the source.
- `visual_target_fidelity`: implementation preserves the approved hierarchy, density, and composition.
- `user_task_completion`: the primary task can be completed without technical knowledge.
- `user_visual_approval`: the user has seen the actual result and approved it.

## Technical quality

- Build and type checks pass for the touched project.
- The rendered route loads at the fixed viewport.
- Primary interactions work.
- No fatal console error appears.
- Keyboard focus is visible and logical.
- Text contrast and accessible names meet the applicable baseline.
- No unrelated product, Core, Run, or Dirty file changed.
- Rollback or prior Version remains available.

## Delivery decision

- `design_pass` requires every applicable design-quality item to pass.
- `technical_pass` requires every applicable technical item to pass.
- `complete` requires both plus user approval.
- A rejected Visual Target remains evidence and cannot become the default Recipe.

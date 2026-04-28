---
name: Nordic Frost
colors:
  surface: '#f9f9ff'
  surface-dim: '#d8d9e3'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3fd'
  surface-container: '#ecedf7'
  surface-container-high: '#e6e7f2'
  surface-container-highest: '#e1e2ec'
  on-surface: '#191b23'
  on-surface-variant: '#424754'
  inverse-surface: '#2e3038'
  inverse-on-surface: '#eff0fa'
  outline: '#727785'
  outline-variant: '#c2c6d6'
  surface-tint: '#005ac2'
  primary: '#0058be'
  on-primary: '#ffffff'
  primary-container: '#2170e4'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#545f73'
  on-secondary: '#ffffff'
  secondary-container: '#d5e0f8'
  on-secondary-container: '#586377'
  tertiary: '#924700'
  on-tertiary: '#ffffff'
  tertiary-container: '#b75b00'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#004395'
  secondary-fixed: '#d8e3fb'
  secondary-fixed-dim: '#bcc7de'
  on-secondary-fixed: '#111c2d'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#ffdcc6'
  tertiary-fixed-dim: '#ffb786'
  on-tertiary-fixed: '#311400'
  on-tertiary-fixed-variant: '#723600'
  background: '#f9f9ff'
  on-background: '#191b23'
  surface-variant: '#e1e2ec'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  code-mono:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built for high-stakes enterprise environments where clarity, speed of cognition, and precision are paramount. The aesthetic is rooted in **Minimalism** with a strict adherence to functional logic, drawing inspiration from industrial drafting and Swiss precision. 

The brand personality is clinical, disciplined, and transparent. It avoids unnecessary ornamentation to reduce cognitive load, using vast amounts of negative space to organize complex data sets. The emotional response is one of calm control and professional reliability.

## Colors

The palette is restricted to a high-contrast clinical light mode. 
- **Background (#F8FAFC):** A cool, icy grey used for the application canvas to differentiate from actionable surfaces.
- **Surface (#FFFFFF):** Pure white reserved for cards, modals, and input areas to maximize legibility.
- **Accent (#3B82F6):** A precise blue used sparingly for primary actions, progress indicators, and active states.
- **Neutral/Text (#1E293B):** A deep slate for high-contrast typography, ensuring WCAG AAA compliance for core data.
- **Borders (#E2E8F0):** Subtle but sharp dividers used to define structure without adding visual weight.

## Typography

The design system utilizes **Inter** for its systematic, utilitarian qualities. The typeface is chosen for its exceptional legibility in dense data grids and its neutral, corporate tone.

- **Scale:** A tight typographic scale ensures that information density remains high without sacrificing hierarchy.
- **Weight:** Use `Bold (700)` for primary headings and `Semi-Bold (600)` for section headers. `Regular (400)` is the standard for all body and data entries.
- **Labels:** Meta-information and table headers use a bold, all-caps style with slight letter spacing to create a distinct visual "zone" for structural text.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy for core content areas, transitioning to a fluid model for dashboard widgets. 

- **The 4px Base:** All spacing—from padding inside buttons to the margins between sections—must be a multiple of 4px.
- **Grid:** A 12-column grid is standard. In complex enterprise views, sidebars are fixed at 240px, while the primary content area uses a 24px gutter.
- **Density:** The system leans towards "Compact" density for data-heavy views (12px vertical padding on rows) and "Comfortable" for settings or documentation (24px vertical padding).

## Elevation & Depth

To maintain the "Frost" aesthetic, the system rejects traditional soft shadows in favor of **Bold Borders** and **Tonal Layering**.

- **Depth via Contrast:** Elevation is communicated by placing #FFFFFF surfaces on the #F8FAFC background. 
- **Outlines:** Use 1px solid borders (#E2E8F0) to define all containers. 
- **Shadows:** Only one level of shadow is permitted: a "Hard Shadow" used exclusively for floating elements like dropdowns or modals. It should be 4px offset, 0px blur, at 5% opacity of the neutral color.
- **Focus States:** Active elements use a 2px solid #3B82F6 outline with a 2px offset to ensure clarity.

## Shapes

The shape language is strictly **Sharp (0px)**. Every element—buttons, input fields, cards, and tags—must have 90-degree corners. This reinforces the architectural and technical nature of the tool. 

Avoid any rounding even in icons; use "Square" or "Sharp" variants of icon sets to ensure stylistic continuity.

## Components

- **Buttons:** Primary buttons are solid #3B82F6 with white text. Secondary buttons are #FFFFFF with a 1px #E2E8F0 border. All buttons have 0px radius.
- **Input Fields:** Use #FFFFFF background with a 1px #E2E8F0 border. On focus, the border changes to #3B82F6. Labels are positioned above the field using `label-caps`.
- **Chips/Tags:** Small rectangular blocks with a light grey background (#F1F5F9) and 12px font size. No rounded corners.
- **Data Tables:** The core of the tool. Use a "Zebra" stripe pattern where every other row is #F8FAFC. Cell borders are horizontal only to emphasize row continuity.
- **Checkboxes & Radios:** Strictly square (0px radius). Use the #3B82F6 accent for the "checked" state.
- **Modals:** High-contrast containers with a heavy 2px #1E293B border and a minimal hard shadow. Header areas should be separated by a 1px divider.
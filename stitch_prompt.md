# Stitch Prompts — ComplianceAI UI Generation

> **Instructions:** Use each prompt below as a separate Stitch generation request.
> Attach `design.md` as context with every prompt.
> Generate one page at a time for best results.

---

## How to Use

1. Open [Stitch](https://stitch.withgoogle.com) (or your Stitch instance)
2. Upload / paste the entire `design.md` as the design context
3. Copy one prompt section below and submit it
4. Iterate on the result if needed
5. Move to the next page

---

## Prompt 1 — Landing Page

```
You are building the frontend for "ComplianceAI" — a compliance RAG assistant
that lets bank employees ask natural language questions and get answers
grounded in internal policy documents, powered by a local Llama 3.1 LLM.

I've attached the full design system (design.md). Use it as the single source
of truth for colors, typography, spacing, components, and layout.

Generate the LANDING PAGE (route: /).

Requirements:
- Dark theme using the exact color tokens from the design system
- Top navigation bar: shield logo + "ComplianceAI" left, nav links
  (Ask, Library, About) center, green status dot right
- Hero section: centered shield icon (64px, outlined, blue glow pulse),
  large headline "ComplianceAI", tagline "Institutional Knowledge, Instantly
  Grounded." below
- Description paragraph (max 540px, centered, secondary text color)
- Hero query bar: 560px wide glassmorphic input with "Ask →" primary button,
  blue glow shadow
- Suggestion chips row: "KYC Periodic Updation", "Account Freezing Rules",
  "High Risk Customer Protocol", "STR Filing Procedure" — pill-shaped,
  dark surface, hover to blue
- 3 feature cards: "13 Policy Documents Indexed", "Local Llama 3.1 Inference",
  "Every Answer Cited" — glass surface, blue icons, hover scale effect
- Footer: "Powered by Llama 3.1 · FAISS · Local inference" left, "v0.1" right
- Entry animations: staggered fade-up on hero text, query bar, then cards
- Subtle CSS-only animated background grid (faint drifting orthogonal lines)
- Use Inter font from Google Fonts, JetBrains Mono for any monospaced text
- Fully responsive (see breakpoints in design.md)
- Semantic HTML, WCAG AA contrast, proper heading hierarchy

Tech: Single HTML file with inline CSS. No frameworks. No JavaScript except
for suggestion chip click → navigate to /ask with query pre-filled.
```

---

## Prompt 2 — Ask / Chat Page (★ Core)

```
You are building the frontend for "ComplianceAI" — a compliance RAG assistant.
I've attached the full design system (design.md). Use it as the single source
of truth.

Generate the ASK PAGE (route: /ask) — the primary chat interface.

Layout: Split panel
- LEFT (60%): Conversation panel with message bubbles
- RIGHT (40%): Sources panel showing citation cards
- BOTTOM (sticky): Input bar with auto-expanding textarea

Conversation Panel details:
- System welcome message: purple left-border, italic, "Welcome to
  ComplianceAI. Ask any compliance or KYC question."
- User messages: right-aligned, blue background, white text, rounded
  (top-right square corner for bubble feel)
- AI responses: left-aligned, dark tertiary surface, supports bold text
  and bullet lists. At the bottom of each AI response, a clickable pill
  badge "📄 N sources cited"
- Typing indicator: 3 dots with staggered bounce animation in a
  placeholder AI bubble
- Smooth auto-scroll to bottom on new messages

Sources Panel details:
- Header: "Sources" with a count badge
- Citation cards (per design.md §3.4): colored left-border by risk level
  (red=HIGH, amber=MEDIUM, green=LOW), monospace chunk ID, department,
  topic, regulation citation, relevance score bar (blue→purple gradient)
- Empty state: "Ask a question to see cited sources" with muted doc icon
- Staggered entrance animation (100ms per card)
- On mobile (<1024px): collapses into a bottom drawer

Input Bar:
- Sticky bottom, auto-expanding textarea (1→4 rows), 48px min-height
- Circle submit button (arrow-up icon) right-aligned inside the input,
  blue accent, disabled when empty
- Enter to submit, Shift+Enter for newline
- Loading state: input disabled, button shows spinner

The page should include demo/mock data showing a sample conversation:
- User: "What is KYC?"
- AI: A multi-paragraph answer about KYC being Know Your Customer...
  with "📄 3 sources cited" badge
- Sources: 3 citation cards from definitions.txt, kyc_onboarding.txt,
  and compliance_manual.txt with realistic chunk IDs and metadata

Important:
- Use the exact design tokens from design.md
- Inter + JetBrains Mono fonts
- Glass/blur effects on citation cards
- Responsive: sources panel becomes bottom sheet on mobile
- All colors from the dark palette — NO white backgrounds anywhere

Tech: HTML + CSS + vanilla JavaScript. Fetch calls go to
http://localhost:8000/query with POST body {"question": "..."}.
Response shape: {"answer": "...", "sources": [{"chunk_id": "...",
"citation": "..."}]}
```

---

## Prompt 3 — Document Library Page

```
You are building the frontend for "ComplianceAI" — a compliance RAG assistant.
I've attached the full design system (design.md). Use it as the single source
of truth.

Generate the DOCUMENT LIBRARY PAGE (route: /library).

Purpose: Browse and search the 13 indexed compliance documents.

Layout:
- Page header: "Document Library" (text-2xl, left) + search input (right,
  280px, pill-shaped)
- Subtitle: "13 compliance documents indexed" in secondary text
- Filter bar: horizontal pill chips — All (active default), Compliance,
  Audit, KYC, Risk, Privacy, AML, Operations. Active = blue bg + white
  text. Inactive = dark tertiary + secondary text
- Document cards in a 2-column responsive grid

Each document card:
- Glass surface with subtle border
- Document icon + title (text-lg, semibold)
- Department name (secondary text)
- Metadata line: "N chunks · XX.X KB"
- "View Details →" ghost button
- Hover: blue glow border, translateY -2px, shadow

The 13 documents to display (real data):
1. Compliance Manual — Compliance Division — 17.9 KB
2. Audit Guidelines — Internal Audit — 12.7 KB
3. Reporting Guidelines — Reporting Dept — 13.3 KB
4. KYC Onboarding — Operations — 13.3 KB
5. Periodic Updation — Compliance Division — 11.6 KB
6. Customer Risk Classification — Risk Dept — 11.3 KB
7. Definitions — Compliance Division — 10.4 KB
8. Data Privacy Policy — Legal/Privacy — 11.5 KB
9. Incident Management — Security Operations — 14.4 KB
10. Roles & Responsibilities — Governance — 13.3 KB
11. STR/CTR Procedure — AML Division — 11.6 KB
12. Training & Assessment — HR/Training — 11.8 KB
13. Transaction Monitoring — AML Division — 13.6 KB

Document Detail Modal (on "View Details →" click):
- Slide-over panel from right (480px on desktop, full-screen mobile)
- Dark overlay with blur
- Shows document name, department, filename
- Lists chunks with: chunk ID (mono), topic, risk level badge, applicable
  roles, sample user queries, regulation source
- Bottom CTA: "Ask about this document →"
- Close [✕] button

Use mock chunk data for the detail modal — show 2 chunks with realistic
metadata matching the document's domain.

Entry animations: cards fade-in staggered row-by-row (80ms offset).
Client-side search: instant filter by document name and department.

Tech: HTML + CSS + vanilla JS. Dark theme only, using design.md tokens.
Inter + JetBrains Mono.
```

---

## Prompt 4 — About Page

```
You are building the frontend for "ComplianceAI" — a compliance RAG assistant.
I've attached the full design system (design.md). Use it as the single source
of truth.

Generate the ABOUT PAGE (route: /about).

Sections:

1. "How ComplianceAI Works" — Pipeline Visualization
   - 5 nodes in a horizontal flow connected by animated arrows
   - Nodes: Documents → Chunking → Embedding → FAISS Retrieval → LLM
   - Each node: 64px square card with icon and label, dark tertiary bg
   - Connecting arrows: SVG lines with animated dash-offset (flowing dots)
   - On page load, nodes highlight sequentially (300ms stagger, blue glow)
   - Below: numbered description list explaining each stage:
     1. "13 internal policy files are parsed"
     2. "Split into structured, metadata-rich blocks"
     3. "all-MiniLM-L6-v2 encodes into 384-d vectors"
     4. "FAISS finds the closest matching chunks"
     5. "Llama 3.1 synthesizes a grounded answer"

2. "System Status" — 3 status cards in a row
   - FAISS Index: green dot "Online", "26 vectors"
   - Ollama: green dot "Online", "llama3.1:8b"
   - API Server: green dot "Online", "localhost:8000"
   - Glass surface, subtle border
   (These are decorative/static — not live health checks)

3. "Built With" — horizontal list of tech names
   - FastAPI · FAISS · Sentence-Transformers · Ollama · Pixi
   - Monospace font, muted text color, separated by centered dots

Design:
- Dark theme using design.md tokens
- Generous vertical spacing between sections
- Each step description fades in synchronized with its pipeline node
- Inter + JetBrains Mono
- Responsive: pipeline flow wraps to vertical on mobile

Tech: HTML + CSS + minimal vanilla JS (for the staggered animations).
No frameworks.
```

---

## Prompt 5 — Full Navigation Shell (Shared Layout)

```
You are building the frontend for "ComplianceAI". I've attached design.md.

Generate the SHARED NAVIGATION SHELL that wraps all pages:

Top Navigation Bar (64px, fixed):
- Background: --bg-secondary (#111827) with 1px bottom border (--border-subtle)
- LEFT: Shield icon (inline SVG, 28px, blue stroke) + "ComplianceAI" text
  (semibold, text-lg). The shield should have a subtle glow-pulse CSS
  animation on the stroke
- CENTER: Nav links — "Ask", "Library", "About". Active page has a 2px
  blue underline that slides with a CSS transition when switching pages.
  Hover: text brightens to --text-primary
- RIGHT: Green pulsing dot (8px, --accent-emerald) with "System Online"
  tooltip on hover
- On scroll: add --shadow-sm to the nav bar (subtle elevation change)
- Mobile (<768px): hamburger icon replaces center links, opens a
  full-height slide-down drawer with nav links

Footer (40px):
- Background: --bg-secondary, border-top --border-subtle
- LEFT: "Powered by Llama 3.1 · FAISS · Local inference" in --text-muted,
  text-sm
- RIGHT: "v0.1" badge in --text-muted

Include a simple hash-based SPA router in vanilla JS:
- #/ → landing page content
- #/ask → chat page content
- #/library → library page content
- #/about → about page content
- Page transitions: content fades out (150ms) then fades in (150ms)

Tech: HTML + CSS + vanilla JS. This is the wrapper — page content areas
are placeholder divs that will be populated by page-specific scripts.
```

---

## Tips for Best Results

1. **Always attach `design.md`** — it has every token, spacing value, and specification
2. **Generate one page at a time** — don't try to do all 4 in one prompt
3. **Start with Prompt 5 (Shell)** — get the navigation and routing working first, then fill in pages
4. **Iterate** — if colors or spacing look off, ask Stitch: "Match the exact HSL values from the design.md color tokens"
5. **Merge** — after generating all pages individually, combine them into the SPA shell from Prompt 5

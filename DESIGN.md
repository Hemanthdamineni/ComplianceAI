# Compliance RAG — UI Design System & Page Specifications

> **Product Name:** ComplianceAI  
> **Tagline:** _Institutional Knowledge, Instantly Grounded._  
> **Backend:** FastAPI + FAISS + Llama 3.1 (local via Ollama)  
> **Target Users:** Branch Managers, Compliance Officers, Auditors, Frontline Bank Staff  

---

## 1 · Design Philosophy

This is a **trust-critical, internal enterprise tool**. Every pixel must communicate:

| Principle | Implementation |
|-----------|---------------|
| **Authority** | Deep navy/dark slate canvas — feels institutional, not playful |
| **Clarity** | Generous whitespace, strong typographic hierarchy, zero clutter |
| **Groundedness** | Every AI answer is visually tethered to its source documents |
| **Speed** | Skeleton loaders, streaming-style text reveal, instant feedback |
| **Precision** | Monospaced chunk IDs, structured citation cards, risk-level badges |

**Anti-patterns to avoid:**
- Chatbot-toy aesthetics (bubbly colors, cartoon avatars)
- Generic SaaS dashboards with meaningless charts
- Walls of unstyled text
- Any element that looks unfinished or placeholder-ish

---

## 2 · Design Tokens

### 2.1 Color Palette

```
── Surface ──────────────────────────────────────────────
--bg-primary:        hsl(222, 47%, 6%)        /* #0B0F1A  — deep void          */
--bg-secondary:      hsl(222, 35%, 10%)       /* #111827  — card surface        */
--bg-tertiary:       hsl(222, 30%, 14%)       /* #1A2035  — elevated surface    */
--bg-hover:          hsl(222, 25%, 18%)       /* #232B3E  — hover state         */

── Border & Divider ─────────────────────────────────────
--border-subtle:     hsl(222, 20%, 20%)       /* #2A3040  — hairline dividers   */
--border-active:     hsl(215, 70%, 50%)       /* #2E7DD1  — focused inputs      */

── Text ─────────────────────────────────────────────────
--text-primary:      hsl(210, 20%, 92%)       /* #E5E9F0  — body text           */
--text-secondary:    hsl(215, 15%, 60%)       /* #8B95A8  — captions, labels    */
--text-muted:        hsl(215, 10%, 40%)       /* #5C6370  — disabled, hints     */

── Accent ───────────────────────────────────────────────
--accent-blue:       hsl(215, 80%, 56%)       /* #3B82F6  — primary actions     */
--accent-blue-hover: hsl(215, 80%, 48%)       /* #2563EB  — button hover        */
--accent-blue-ghost: hsla(215, 80%, 56%, 0.1) /* — ghost button bg              */
--accent-amber:      hsl(38, 92%, 55%)        /* #F59E0B  — warnings, risk      */
--accent-emerald:    hsl(160, 70%, 42%)       /* #10B981  — success, low risk   */
--accent-red:        hsl(0, 72%, 55%)         /* #EF4444  — errors, high risk   */
--accent-purple:     hsl(270, 60%, 60%)       /* #8B5CF6  — info badges         */

── Glow / Glass ─────────────────────────────────────────
--glow-blue:         0 0 30px hsla(215, 80%, 56%, 0.15)
--glass-bg:          hsla(222, 35%, 12%, 0.7)
--glass-border:      hsla(215, 30%, 30%, 0.3)
--glass-blur:        blur(16px)
```

### 2.2 Typography

```
-- Font Stack ───────────────────────────────────────────
--font-sans:    'Inter', 'SF Pro Display', system-ui, sans-serif
--font-mono:    'JetBrains Mono', 'Fira Code', monospace

-- Scale (modular 1.25) ─────────────────────────────────
--text-xs:      0.75rem / 1rem        /* 12px — badge labels          */
--text-sm:      0.875rem / 1.25rem    /* 14px — captions, metadata    */
--text-base:    1rem / 1.5rem         /* 16px — body text             */
--text-lg:      1.25rem / 1.75rem     /* 20px — card titles           */
--text-xl:      1.5rem / 2rem         /* 24px — section headers       */
--text-2xl:     2rem / 2.5rem         /* 32px — page titles           */
--text-hero:    3rem / 3.5rem         /* 48px — hero headline         */

-- Weight ───────────────────────────────────────────────
--font-regular: 400
--font-medium:  500
--font-semibold:600
--font-bold:    700
```

### 2.3 Spacing & Radius

```
--space-1:  0.25rem    /* 4px  */
--space-2:  0.5rem     /* 8px  */
--space-3:  0.75rem    /* 12px */
--space-4:  1rem       /* 16px */
--space-6:  1.5rem     /* 24px */
--space-8:  2rem       /* 32px */
--space-12: 3rem       /* 48px */
--space-16: 4rem       /* 64px */

--radius-sm: 6px
--radius-md: 10px
--radius-lg: 16px
--radius-xl: 24px
--radius-full: 9999px
```

### 2.4 Shadows & Effects

```
--shadow-sm:   0 1px 2px hsla(0,0%,0%,0.3)
--shadow-md:   0 4px 12px hsla(0,0%,0%,0.4)
--shadow-lg:   0 8px 32px hsla(0,0%,0%,0.5)
--shadow-glow: 0 0 40px hsla(215, 80%, 56%, 0.12)

/* Glassmorphism mixin */
.glass {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  backdrop-filter: var(--glass-blur);
}
```

### 2.5 Motion

```
--ease-out:     cubic-bezier(0.16, 1, 0.3, 1)
--ease-spring:  cubic-bezier(0.34, 1.56, 0.64, 1)
--duration-fast:    150ms
--duration-normal:  250ms
--duration-slow:    400ms
--duration-reveal:  600ms
```

---

## 3 · Component Library

### 3.1 Global Shell

```
┌─────────────────────────────────────────────────────────────┐
│  ◉ ComplianceAI          [Ask]  [Library]  [About]    ● ⚙  │  ← Top nav (64px)
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                     [ Page Content ]                        │  ← Main area
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Powered by Llama 3.1 · FAISS · Local inference       v0.1 │  ← Footer (40px)
└─────────────────────────────────────────────────────────────┘
```

**Top Navigation Bar:**
- Fixed, 64px height, `--bg-secondary` with bottom `--border-subtle`
- Left: Logo icon (shield glyph) + "ComplianceAI" in `--font-semibold --text-lg`
- Center: Nav links — `Ask` (primary), `Library`, `About`
- Active link: underline with `--accent-blue`, 2px, animated slide
- Right: Status indicator (green dot if FAISS engine loaded) + settings gear icon
- Subtle `box-shadow: --shadow-sm` on scroll

### 3.2 Buttons

| Variant | Background | Text | Border | Use |
|---------|-----------|------|--------|-----|
| **Primary** | `--accent-blue` | white | none | Submit query, main CTAs |
| **Ghost** | `--accent-blue-ghost` | `--accent-blue` | `--accent-blue` 1px | Secondary actions |
| **Subtle** | transparent | `--text-secondary` | none | Tertiary, icon buttons |
| **Danger** | `--accent-red` | white | none | Destructive actions |

All buttons: `--radius-md`, `padding: --space-2 --space-4`, `--font-medium`, `--text-sm`  
Hover: brighten 8%, translate Y -1px, `--shadow-sm`  
Active: darken 4%, translate Y 0  
Transition: `all var(--duration-fast) var(--ease-out)`

### 3.3 Input Fields

- Background: `--bg-primary`
- Border: 1px `--border-subtle`, on focus → `--border-active` + `--glow-blue`
- Radius: `--radius-md`
- Text: `--text-primary`, placeholder `--text-muted`
- Padding: `--space-3 --space-4`
- Transition: `border-color var(--duration-fast), box-shadow var(--duration-fast)`

### 3.4 Citation Card

```
┌─────────────────────────────────────────────────────┐
│  📄 periodic_updation.txt                    [HIGH] │  ← risk badge
│  ─────────────────────────────────────────────────  │
│  Chunk: PERIUP_CHUNK01                              │  ← mono font
│  Dept: Compliance Division                          │
│  Topic: Workflow and Risk-Based Timelines for       │
│         KYC Refreshment                             │
│  ─────────────────────────────────────────────────  │
│  Citation: RBI Master Direction - KYC (2016),       │
│            Chapter VII, Section 38                  │
│                                                     │
│  Relevance Score: ████████░░ 0.3421                 │  ← visual bar
└─────────────────────────────────────────────────────┘
```

- Surface: `--bg-tertiary`, border-left 3px colored by risk level
- Risk badge colors: HIGH → `--accent-red`, MEDIUM → `--accent-amber`, LOW → `--accent-emerald`
- Chunk ID in `--font-mono --text-xs`
- Relevance score bar: gradient from `--accent-blue` to `--accent-purple`
- Hover: elevate with `--shadow-md`, border-left widens to 5px
- Entrance: fade-in + slide-up staggered by 100ms per card

### 3.5 Risk Level Badges

```css
.badge {
  padding: var(--space-1) var(--space-2);
  border-radius: var(--radius-full);
  font: var(--font-semibold) var(--text-xs) var(--font-mono);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.badge-high   { background: hsla(0,72%,55%,0.15);   color: var(--accent-red);     }
.badge-medium { background: hsla(38,92%,55%,0.15);   color: var(--accent-amber);   }
.badge-low    { background: hsla(160,70%,42%,0.15);   color: var(--accent-emerald); }
```

### 3.6 Loading / Skeleton States

**AI Thinking Indicator:**
- Three-dot pulse animation in `--accent-blue`
- Text: "Searching compliance corpus..." → "Generating grounded answer..."
- Subtle progress shimmer across the response area

**Skeleton Cards:**
- Pulsing rectangles matching citation card layout
- `background: linear-gradient(90deg, --bg-tertiary 25%, --bg-hover 50%, --bg-tertiary 75%)`
- `animation: shimmer 1.5s infinite`

---

## 4 · Page Specifications

---

### PAGE 1: Landing / Home

**Route:** `/`  
**Purpose:** First impression — communicate what this tool does, build trust, funnel to chat.

#### Layout

```
┌──────────────────────────────────────────────────────────────┐
│  NAV BAR                                                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│              🛡️                                              │
│         ComplianceAI                                         │
│                                                              │
│    Institutional Knowledge, Instantly Grounded.              │
│                                                              │
│    Ask any compliance question and receive answers           │
│    backed by your organization's actual policy               │
│    documents — powered by local AI, zero cloud exposure.     │
│                                                              │
│         ┌─────────────────────────────────────┐              │
│         │  "What is KYC?"              [Ask →]│              │  ← hero query bar
│         └─────────────────────────────────────┘              │
│                                                              │
│    ── or try: ───────────────────────────────                │
│    [KYC Periodic Updation] [Account Freezing Rules]          │  ← suggestion chips
│    [High Risk Customer Protocol] [STR Filing Procedure]      │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│   │  🔍 13     │  │  🧠 Local  │  │  📄 Cited  │            │
│   │  Policy    │  │  Llama 3.1 │  │  Every     │            │
│   │  Documents │  │  Inference │  │  Answer    │            │  ← feature cards
│   │  Indexed   │  │  No Cloud  │  │  Grounded  │            │
│   └────────────┘  └────────────┘  └────────────┘            │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  FOOTER                                                      │
└──────────────────────────────────────────────────────────────┘
```

#### Specifications

| Element | Detail |
|---------|--------|
| **Hero Background** | Radial gradient: `--bg-primary` center → `hsla(215,80%,56%,0.05)` outer ring. Subtle animated grid pattern (CSS only, no canvas) — faint orthogonal lines that slowly drift |
| **Shield Icon** | 64×64, outlined style, `--accent-blue` stroke, subtle glow pulse |
| **Headline** | `--text-hero`, `--font-bold`, `--text-primary`, letter-spacing -0.02em |
| **Subhead** | `--text-lg`, `--font-regular`, `--text-secondary`, max-width 540px, centered |
| **Query Bar** | 560px wide, 56px height, `--radius-lg`, glass effect, prominent `--glow-blue` shadow. Input left, "Ask →" primary button right |
| **Suggestion Chips** | `--radius-full`, `--bg-tertiary`, `--text-secondary`, hover → `--accent-blue-ghost` bg + `--accent-blue` text. 100ms transition |
| **Feature Cards** | 3-column grid, glass surface, icon top-center (`--accent-blue`), number/stat bold, descriptor below. Hover: scale 1.02 + shadow-glow |
| **Entry Animations** | Hero text: fade-up staggered 100ms. Query bar: fade-up 200ms delay. Cards: fade-up staggered from 400ms. All use `--ease-out --duration-reveal` |

---

### PAGE 2: Ask (Chat Interface) ★ Core Page

**Route:** `/ask`  
**Purpose:** Primary RAG query interface. User asks → system retrieves + generates → shows grounded answer with sources.

#### Layout (Split Panel)

```
┌──────────────────────────────────────────────────────────────────────┐
│  NAV BAR                                                             │
├────────────────────────────────────┬─────────────────────────────────┤
│                                    │                                 │
│        CONVERSATION PANEL          │        SOURCES PANEL            │
│        (flex: 3, ~60%)             │        (flex: 2, ~40%)          │
│                                    │                                 │
│   ┌─ System ──────────────────┐    │   Sources for current answer:   │
│   │ Welcome to ComplianceAI.  │    │                                 │
│   │ Ask any compliance or KYC │    │   ┌─ Citation Card 1 ────────┐ │
│   │ question.                 │    │   │ 📄 definitions.txt       │ │
│   └───────────────────────────┘    │   │ DEFN_CHUNK01             │ │
│                                    │   │ ...                      │ │
│   ┌─ User ────────────────────┐    │   └──────────────────────────┘ │
│   │ What is KYC?              │    │                                 │
│   └───────────────────────────┘    │   ┌─ Citation Card 2 ────────┐ │
│                                    │   │ 📄 kyc_onboarding.txt    │ │
│   ┌─ AI ──────────────────────┐    │   │ KYCON_CHUNK01            │ │
│   │ KYC (Know Your Customer)  │    │   │ ...                      │ │
│   │ is the mandatory process  │    │   └──────────────────────────┘ │
│   │ of verifying the identity │    │                                 │
│   │ ...                       │    │   ┌─ Citation Card 3 ────────┐ │
│   │                           │    │   │ 📄 compliance_manual.txt │ │
│   │ [📄 3 sources cited]      │    │   │ COMP_CHUNK02             │ │
│   └───────────────────────────┘    │   │ ...                      │ │
│                                    │   └──────────────────────────┘ │
│                                    │                                 │
├────────────────────────────────────┤                                 │
│ ┌────────────────────────────────┐ │                                 │
│ │  Ask a compliance question... │ │                                 │
│ │                          [⏎]  │ │                                 │
│ └────────────────────────────────┘ │                                 │
└────────────────────────────────────┴─────────────────────────────────┘
```

#### Conversation Panel (Left)

| Element | Detail |
|---------|--------|
| **System Message** | `--bg-tertiary`, `--radius-lg`, left-aligned, `--accent-purple` left-border 3px, italic subtext |
| **User Message** | Aligned right, `--accent-blue` background, white text, `--radius-lg` (top-right square corner for speech-bubble feel) |
| **AI Response** | Aligned left, `--bg-tertiary`, `--text-primary`, `--radius-lg`. Markdown rendering support (bold, lists, inline code) |
| **Source Badge** | Inside AI response bottom — pill badge: "📄 3 sources cited", clickable, scrolls source panel into view on mobile |
| **Typing Indicator** | Three dots with staggered bounce animation, appears in an AI-bubble placeholder |
| **Text Streaming** | AI answer text appears word-by-word with a subtle cursor-blink at the end (mimics typewriter), `--duration-fast` per token |
| **Auto-scroll** | Conversation container scrolls to bottom on new messages with smooth `scroll-behavior` |

#### Sources Panel (Right)

| Element | Detail |
|---------|--------|
| **Panel Header** | "Sources" with doc-count badge, `--text-secondary` |
| **Citation Cards** | As defined in §3.4. Staggered entrance (100ms each) when AI response completes |
| **Empty State** | Muted text "Ask a question to see cited sources" with a subtle document icon |
| **Panel Divider** | 1px `--border-subtle` vertical line. Resizable handle (optional) |
| **Collapsible** | On screens < 1024px, panel collapses into a bottom sheet / drawer activated by the "sources cited" badge |

#### Input Bar (Bottom, Sticky)

| Element | Detail |
|---------|--------|
| **Container** | Sticky bottom, full conversation-panel width, `--bg-secondary`, border-top `--border-subtle` |
| **Input** | Auto-expanding textarea (1→4 rows), `--bg-primary`, `--radius-lg`, 48px min-height |
| **Submit** | Circle icon button, `--accent-blue`, right-aligned inside input. Arrow-up icon. Disabled state when empty |
| **Keyboard** | Enter to submit, Shift+Enter for newline |
| **Loading State** | Input disabled, button shows spinner, placeholder text: "Generating..." |

---

### PAGE 3: Document Library

**Route:** `/library`  
**Purpose:** Browse and search the indexed compliance corpus. Understand what knowledge is available.

#### Layout

```
┌───────────────────────────────────────────────────────────────────┐
│  NAV BAR                                                          │
├───────────────────────────────────────────────────────────────────┤
│                                                                   │
│   Document Library                     [Search... 🔍]             │
│   13 compliance documents indexed                                 │
│                                                                   │
│   Filter: [All] [Compliance] [Audit] [KYC] [Risk] [Privacy]      │
│                                                                   │
│   ┌──────────────────────┐  ┌──────────────────────┐              │
│   │ 📋 Compliance Manual │  │ 📋 Audit Guidelines  │              │
│   │ Compliance Division  │  │ Internal Audit Dept  │              │
│   │ 3 chunks · 17.9 KB   │  │ 2 chunks · 12.7 KB   │              │
│   │ ●●●○ Coverage        │  │ ●●○○ Coverage        │              │
│   │ [View Details →]     │  │ [View Details →]     │              │
│   └──────────────────────┘  └──────────────────────┘              │
│                                                                   │
│   ┌──────────────────────┐  ┌──────────────────────┐              │
│   │ 📋 KYC Onboarding   │  │ 📋 Periodic Updation │              │
│   │ Operations           │  │ Compliance Division  │              │
│   │ 2 chunks · 13.3 KB   │  │ 2 chunks · 11.6 KB   │              │
│   │ ●●●● Coverage        │  │ ●●●○ Coverage        │              │
│   │ [View Details →]     │  │ [View Details →]     │              │
│   └──────────────────────┘  └──────────────────────┘              │
│                                                                   │
│   ... (remaining cards in 2-column responsive grid)               │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

#### Specifications

| Element | Detail |
|---------|--------|
| **Page Header** | `--text-2xl` left, search input right (280px, `--radius-full`) |
| **Subtitle** | "13 compliance documents indexed" — `--text-secondary` |
| **Filter Bar** | Horizontal scroll of pill chips. Active chip: `--accent-blue` bg, white text. Inactive: `--bg-tertiary`, `--text-secondary` |
| **Document Cards** | 2-column grid (gap `--space-6`), glass surface. Icon + title (`--text-lg --font-semibold`). Department in `--text-secondary`. Metadata: chunk count, file size. Coverage dots: 4 dots colored by index coverage. "View Details →" ghost button |
| **Card Hover** | Border glow `--glow-blue`, translateY -2px, `--shadow-md` |
| **Search** | Client-side instant filter by document name, department, keywords |
| **Entry** | Cards fade-in staggered grid pattern (row by row, 80ms offset) |

#### Document Detail (Expandable / Modal)

When clicking "View Details →":

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  📋 Periodic Updation                             [✕]  │
│  Compliance Division · periodic_updation.txt            │
│                                                         │
│  ── Chunks ────────────────────────────────────────────  │
│                                                         │
│  ┌─ PERIUP_CHUNK01 ─────────────────────────────────┐   │
│  │ Topic: Workflow and Risk-Based Timelines for      │   │
│  │        KYC Refreshment                            │   │
│  │ Risk Level: [MEDIUM]                              │   │
│  │ Applicable Roles: Branch Manager, Frontline Staff │   │
│  │                                                   │   │
│  │ Sample Queries:                                   │   │
│  │ • "How often do I need to update a Low Risk acct?"│   │
│  │ • "What triggers a KYC Periodic Updation notice?" │   │
│  │                                                   │   │
│  │ Regulation: RBI Master Direction - KYC (2016),    │   │
│  │             Chapter VII, Section 38               │   │
│  └───────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─ PERIUP_CHUNK02 ─────────────────────────────────┐   │
│  │ Topic: Audit Expectations and Enforcing Account   │   │
│  │        Restrictions                               │   │
│  │ Risk Level: [HIGH]                                │   │
│  │ ...                                               │   │
│  └───────────────────────────────────────────────────┘   │
│                                                         │
│               [Ask about this document →]               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- Modal/slide-over panel from right (480px width on desktop, full-screen on mobile)
- Dark overlay `hsla(0,0%,0%,0.6)` with blur
- Entrance: slide from right + fade, `--duration-slow --ease-out`
- "Ask about this document →" — navigates to `/ask` with the doc name pre-filled

---

### PAGE 4: About

**Route:** `/about`  
**Purpose:** System information, architecture overview, and technology credits.

#### Layout

```
┌───────────────────────────────────────────────────────────────┐
│  NAV BAR                                                      │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│   How ComplianceAI Works                                      │
│                                                               │
│   ┌────┐    ┌────┐    ┌────┐    ┌────┐    ┌────┐             │
│   │ 📄 │ →  │ ✂️ │ →  │ 🧮 │ →  │ 🔍 │ →  │ 🧠 │             │
│   │Docs│    │Chunk│   │Embed│   │FAISS│   │LLM │             │  ← pipeline viz
│   └────┘    └────┘    └────┘    └────┘    └────┘             │
│                                                               │
│   Your question flows through 5 stages:                       │
│                                                               │
│   1. Documents — 13 internal policy files are parsed          │
│   2. Chunking — Split into structured, metadata-rich blocks   │
│   3. Embedding — all-MiniLM-L6-v2 encodes into 384-d vectors │
│   4. Retrieval — FAISS finds the closest matching chunks      │
│   5. Generation — Llama 3.1 synthesizes a grounded answer     │
│                                                               │
│   ── System Status ───────────────────────────────────────    │
│                                                               │
│   ┌─────────────┐ ┌──────────────┐ ┌─────────────────┐       │
│   │ FAISS Index  │ │ Ollama       │ │ API Server      │       │
│   │ ● Online     │ │ ● Online     │ │ ● Online        │       │
│   │ 26 vectors   │ │ llama3.1:8b  │ │ localhost:8000  │       │
│   └─────────────┘ └──────────────┘ └─────────────────┘       │
│                                                               │
│   ── Built With ──────────────────────────────────────────    │
│   FastAPI · FAISS · Sentence-Transformers · Ollama · Pixi    │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

#### Specifications

| Element | Detail |
|---------|--------|
| **Pipeline Visualization** | 5-node horizontal flow with connecting arrows. Each node: 64px square icon card, `--bg-tertiary`, `--radius-md`. Arrows: SVG lines with animated dash-offset (flowing dots effect). Nodes highlight sequentially on page load (300ms stagger) |
| **Step Descriptions** | Numbered list, each step fades in synchronized with its pipeline node |
| **Status Cards** | 3-column grid. Green dot + "Online" or red dot + "Offline". Status is decorative/static (real health checks are a future enhancement). Glass surface |
| **Tech Credits** | Horizontal list of technology names in `--font-mono --text-sm`, subtle `--text-muted` |

---

## 5 · Interaction Patterns

### 5.1 Query Flow Animation Sequence

```
t=0ms     User presses Enter / clicks Submit
t=0ms     Input disables, button shows spinner
t=50ms    User message bubble appends with slide-up
t=100ms   AI placeholder bubble appears with typing indicator (3-dot bounce)
t=100ms   Sources panel shows 3 skeleton cards (shimmer)

          ... API call in progress ...

t=RTT     AI response text begins streaming (word-by-word typewriter, 30ms/word)
t=RTT     Sources panel: skeleton cards crossfade into real citation cards
          (staggered 100ms per card, slide-up + fade-in)
t=done    Typing cursor disappears
t=done    "📄 N sources cited" badge fades in at bottom of AI response
```

### 5.2 Keyboard Shortcuts

| Key | Action | Context |
|-----|--------|---------|
| `Enter` | Submit query | Input focused |
| `Shift+Enter` | New line | Input focused |
| `/` | Focus input | Anywhere on /ask |
| `Esc` | Close modal/drawer | Modal open |

### 5.3 Error States

| State | Display |
|-------|---------|
| **FAISS offline** | Banner at top: amber background, "⚠ Vector index not loaded. Run `pixi run build-index`" |
| **Ollama unreachable** | AI bubble shows: red-bordered card with "Could not connect to Ollama at localhost:11434" |
| **No results** | AI bubble with muted text: "No relevant documents found for this query." Sources panel empty state |
| **Network error** | Toast notification, bottom-right, auto-dismiss 5s, red accent |

---

## 6 · Responsive Breakpoints

| Breakpoint | Layout Changes |
|------------|---------------|
| **≥ 1280px** | Full split-panel (60/40) on `/ask`. 3-col feature cards. 2-col library grid |
| **1024–1279px** | Split-panel narrows to 65/35. Feature cards stay 3-col |
| **768–1023px** | Sources panel becomes collapsible bottom drawer. 2-col library grid. Feature cards 2-col |
| **< 768px** | Full single-column. Sources in bottom sheet. Library 1-col. Nav hamburger menu. Query bar full-width |

---

## 7 · Accessibility

| Requirement | Implementation |
|-------------|---------------|
| **Color contrast** | All text/bg combos meet WCAG 2.1 AA (4.5:1 minimum) |
| **Focus indicators** | 2px `--accent-blue` outline with 2px offset on all interactive elements |
| **Aria labels** | All icon-only buttons have `aria-label`. Citation cards use `role="article"` |
| **Screen reader** | AI responses marked with `aria-live="polite"`. Loading states use `aria-busy` |
| **Reduced motion** | Wrap all animations in `@media (prefers-reduced-motion: reduce)` — instant transitions |
| **Keyboard nav** | Full tab-order through all interactive elements. Enter/Space activate buttons |

---

## 8 · File & Asset Inventory

```
ui/
├── index.html                 # SPA entry point
├── styles/
│   ├── tokens.css             # All design tokens from §2
│   ├── reset.css              # Minimal CSS reset
│   ├── components.css         # Component styles from §3
│   └── pages.css              # Page-specific overrides
├── scripts/
│   ├── app.js                 # Router + page initialization
│   ├── api.js                 # Fetch wrapper for /query endpoint
│   ├── chat.js                # Chat interface logic
│   ├── library.js             # Library page logic
│   └── utils.js               # Helpers (markdown render, debounce, etc.)
├── assets/
│   ├── logo.svg               # Shield icon
│   └── icons/                 # UI icons (inline SVG preferred)
└── favicon.ico
```

---

## 9 · Document Corpus Reference

The 13 internal policy documents available in the system:

| # | Document | File | Domain |
|---|----------|------|--------|
| 1 | Compliance Manual | `compliance_manual.txt` | Core Policy |
| 2 | Audit Guidelines | `audit_guidelines.txt` | Audit |
| 3 | Reporting Guidelines | `reporting_guidelines.txt` | Reporting |
| 4 | KYC Onboarding | `kyc_onboarding.txt` | KYC |
| 5 | Periodic Updation | `periodic_updation.txt` | KYC |
| 6 | Customer Risk Classification | `customer_risk_classification.txt` | Risk |
| 7 | Definitions | `definitions.txt` | Reference |
| 8 | Data Privacy Policy | `data_privacy_policy.txt` | Privacy |
| 9 | Incident Management | `incident_management.txt` | Operations |
| 10 | Roles & Responsibilities | `roles_responsibilities.txt` | Governance |
| 11 | STR/CTR Procedure | `str_ctr_procedure.txt` | AML |
| 12 | Training & Assessment | `training_assessment.txt` | HR/Training |
| 13 | Transaction Monitoring | `transaction_monitoring.txt` | AML |

External regulatory sources: `rbi_kyc.pdf`, `sebi_act.pdf`

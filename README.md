Hi, I'm Ajay. I build products on top of LLMs, and most of my time goes into the unglamorous parts around the model: retrieval, agent workflows, job queues, and the backend that decides whether a demo survives real users.

I've shipped two products on my own, and I keep a lot of side projects running in private. Their code stays private, but I'm happy to walk through any of them on a call.

### Shipped

- **[PostGit](https://postgit.com)** - turns your GitHub activity into X posts, LinkedIn drafts and build-in-public updates, and schedules them. Built it, run it.
- **[Docminos](https://docminos.com)** - you give it your project details, it gives back a .docx report in the exact format your university or institution asks for.

### Built in private

- **reel-studio** - makes faceless, animated Instagram Reels with Remotion: research, script, word-timed animation, QA. Everything is plain files; there's no database and no server.
- **LeadPilot** - finds local businesses with weak websites, audits them, and drafts an outreach email with Claude. It only runs on localhost and starts in dry-run mode. To actually send anything you have to type `GO LIVE`.
- **jobpipe** - my job search, automated right up to the part that matters. It reads job boards, scores roles, and tailors my resume, then waits for me to approve every application.
- **BookLeaf Portal** - a support desk for an author platform, with AI triage, priority scoring and drafted replies. It still works with no API key. ([live demo](https://bookleaf-portal-tau-topaz.vercel.app))
- **PS5 Play** - a two-minute check-in on how you're feeling, then three PS Plus games to match.
- **portfolio** - my site, with a hand-written GLSL shader for the hero.

### Open source

| | |
|---|---|
| [dep-drift](https://github.com/Ajay702/dep-drift) | Tells you which of your dependencies your AI assistant probably doesn't know about, by comparing publish dates against the model's training cutoff. |
| [voice-first-demo](https://github.com/Ajay702/voice-first-demo) | Record the narration first; Playwright then records the screen to match your timing. No editing. |
| [claim-processing-langgraph](https://github.com/Ajay702/claim-processing-langgraph) | Multi-agent LangGraph pipeline that reads insurance-claim PDFs page by page and returns one structured result. |
| [Windcast](https://github.com/Ajay702/rqx4tn) | How good was the GB wind forecast at the moment a trader had to act on it? ([live](https://vqmzk.vercel.app)) |
| [Design-Sight](https://github.com/Ajay702/Design-Sight) | Upload a UI mockup, get a UI/UX and accessibility review back. |
| [Lead-Intent-Scoring](https://github.com/Ajay702/Lead-Intent-Scoring-Service-Backend-) | Scores B2B leads with plain rules first, then Gemini for the cases the rules can't decide. |

### Recently pushed

<!-- recent:start -->
<!-- recent:end -->

<samp>Mostly Python and TypeScript. Usually FastAPI or Flask on the back, Next.js on the front.</samp>

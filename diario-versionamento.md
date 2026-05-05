:root {
  --bg: #f7f7fb;
  --text: #1f2937;
  --muted: #6b7280;
  --primary: #a21caf;
  --primary-dark: #86198f;
  --card: #ffffff;
  --border: #e5e7eb;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: Arial, Helvetica, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  max-width: 1100px;
  margin: 0 auto;
  padding: 1.5rem;
}

.logo {
  font-size: 1.4rem;
}

.logo span {
  color: var(--primary);
  font-style: italic;
}

.menu {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.menu a,
.doc-list a,
.project a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 700;
}

.hero {
  min-height: 90vh;
  background: linear-gradient(135deg, #ffffff 0%, #fdf4ff 100%);
  border-bottom: 6px solid var(--primary);
}

.hero-content {
  max-width: 900px;
  margin: 0 auto;
  padding: 5rem 1.5rem;
  text-align: center;
}

.tag,
.label {
  color: var(--primary);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.85rem;
}

h1 {
  font-size: clamp(2.2rem, 6vw, 4.5rem);
  line-height: 1.1;
  margin: 1rem 0;
}

h2 {
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  margin-bottom: 1rem;
}

h3 {
  margin-bottom: 0.75rem;
}

.actions {
  margin-top: 2rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.btn {
  display: inline-block;
  padding: 0.85rem 1.2rem;
  border-radius: 999px;
  border: 2px solid var(--primary);
  text-decoration: none;
  font-weight: 700;
}

.btn.primary {
  background: var(--primary);
  color: white;
}

.btn.secondary {
  color: var(--primary);
}

.section {
  max-width: 1100px;
  margin: 0 auto;
  padding: 4rem 1.5rem;
}

.section.alt {
  max-width: 100%;
  background: #ffffff;
}

.section.alt > * {
  max-width: 1100px;
  margin-left: auto;
  margin-right: auto;
}

.cards {
  display: grid;
  gap: 1.25rem;
  margin-top: 2rem;
}

.cards.three {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.cards.two {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow: 0 10px 30px rgba(31, 41, 55, 0.08);
}

.alt .card {
  background: var(--bg);
}

.doc-list {
  margin-top: 1rem;
  padding-left: 1.5rem;
}

footer {
  text-align: center;
  padding: 2rem 1rem;
  background: #111827;
  color: white;
}

@media (max-width: 800px) {
  .navbar {
    align-items: flex-start;
    flex-direction: column;
  }

  .cards.three,
  .cards.two {
    grid-template-columns: 1fr;
  }
}

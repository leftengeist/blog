# Leftengeist Blog

[![pages-build-deployment](https://github.com/leftengeist/blog/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/leftengeist/blog/actions/workflows/pages/pages-build-deployment)  
[![Build and Deploy Pelican to GitHub Pages](https://github.com/leftengeist/blog/actions/workflows/deploy.yml/badge.svg)](https://github.com/leftengeist/blog/actions/workflows/deploy.yml)

A Simple Tech Blog

## Development

### 1. Setup Virtual Environment

```bash
python -m venv .venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Build Site

```bash
pelican content
```

### 4. Preview Site

```bash
pelican --listen

# Or to enable Auto-Reload mode for active development

pelican --autoreload --listen
```

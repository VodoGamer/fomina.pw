#!/usr/bin/env bash
set -e
npm run build
npm run serve -- --host

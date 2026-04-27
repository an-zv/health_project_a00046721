#!/usr/bin/env bash
gunicorn clinic_site.wsgi:application 
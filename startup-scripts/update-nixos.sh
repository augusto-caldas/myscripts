#!/usr/bin/env bash
sudo nix-channel --update
sudo nixos-rebuild boot
sudo nix-collect-garbage --delete-old

#!/usr/bin/env bash
# Update and ebuild
sudo nixos-rebuild boot --upgrade
sudo nix-collect-garbage --delete-old

# Prompt the user for a reboot
read -p "Reboot now? (y/N): " reboot
if [[ "${reboot,,}" == "y" || "${reboot,,}" == "yes" ]]; then
    sudo reboot
else
    echo "Reboot skipped."
fi

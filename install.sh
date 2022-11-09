echo "NOTE: install.sh needs the Github CLI to be installed for it to work!"
cd $HOME
gh repo clone Oddsie/OddsiePlusPlus
cd OddsiePlusPlus
chmod +x oddsie
echo 'export PATH="$HOME/OddsiePlusPlus:$PATH"' >> ~/.bashrc

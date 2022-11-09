echo "NOTE: install.sh needs the Github CLI to be installed for it to work!"
cd $HOME
mkdir Oddsie
cd Oddsie
gh repo clone Oddsie/OddsiePlusPlus
cd OddsiePlusPlus
chmod +x oddsie
echo 'export PATH="$HOME/Oddsie/OddsiePlusPlus:$PATH"' >> ~/.bashrc

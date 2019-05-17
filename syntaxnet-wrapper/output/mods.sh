# run the following two commands from the docker image terminal 
#   > chmod +x output/mods.sh
#   > ./output/mods.sh

cp output/demo_mod.sh output/parser.sh
mv output/parser.sh syntaxnet/
chmod +x syntaxnet/parser.sh
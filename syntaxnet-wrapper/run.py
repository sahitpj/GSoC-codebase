import os
command1 = 'docker run -v /Users/jayakrishnasahit/Documents/GSoC2019/syntaxnet-wrapper/output:/opt/tensorflow/syntaxnet/output --rm -ti -p 8888:8888 tensorflow/syntaxnet bash'
os.system(command1)



'''
Do mount a local directory to the following docker image, so that outputs can be extracted from the following.

# run the following two commands from the docker image terminal 
#   > chmod +x output/mods.sh
#   > ./output/mods.sh


To parse the following output, do the following,

    echo 'sentence-you-wish-to-parse' | syntaxnet/demo.sh  -- for a tree like structure


    echo 'sentence-you-wish-to-parse' | syntaxnet/parser.sh -- for a conll parse tree
    
'''
cat testbymiro | grep -v Offset: | grep versionId| cut -c 4-| rev | cut -c 4- | rev

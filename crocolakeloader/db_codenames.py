#!/usr/bin/env python3

## @file db_codenames.py
#
## Adapted by Mahi Sarwar Anol <anol.mahi@gmail.com>
#  
# @date sunday 15 June, 2026
## Everything is Adapted from params.py in crocolakeloader (https://github.com/boom-lab/crocolakeloader.git)
#  Originally written by  @author Enrico Milanese <enrico.milanese@whoi.edu>
#
## @date Fri 04 Oct 2024

# Mapping from each database name to the folder-name fragment used on disk.
#
# This is loader-internal: only CrocoLakeLoader's Loader consumes it (to glob
# for "*<codename>*" under the database root). It is intentionally not part of
# the shared db_names.py, since CrocoLakeTools never uses it and the CI sync
# would overwrite it. Moved out of params.py (see boom-lab/crocolakeloader#9).

databases_codenames = {}
databases_codenames["ARGO"] = "ARGO"              # "ARGO-CLOUD"
databases_codenames["GLODAP"] = "GLODAP"          # "GLODAP-DEV"
databases_codenames["SprayGliders"] = "SPRAY"     # "SPRAY-DEV"
databases_codenames["CPR"] = "CPR"
databases_codenames["Saildrones"] = "SAILDRONES"  # "SAILDRONES-DEV"
databases_codenames["OleanderXBT"] = "OLEANDER"   # "OLEANDER-DEV"
# TODO: IOOS_GLIDERS is in db_names.databases but has no codename yet.
# We will have to add it here, otherwise Loader will KeyError when resolving "IOOS_GLIDERS".
# databases_codenames["IOOS_GLIDERS"] = "?"
# Windows Azure Linux Agent
#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.4+ and Openssl 1.0+
#

from azurelinuxagent.metadata import DistroName, DistroVersion

def GetOSUtil():
    from  azurelinuxagent.distro.ubuntu.osutil import Ubuntu1204OSUtil, \
                                                      UbuntuOSUtil, \
                                                      Ubuntu14xOSUtil
    if DistroVersion == "12.04":
        return Ubuntu1204OSUtil()
    elif DistroVersion == "14.04" 0r DistroVersion == "14.10":
        return Ubuntu14xOSUtil()
    else:
        return UbuntuOSUtil()

def GetHandlers():
    from azurelinuxagent.distro.ubuntu.handlerFactory import UbuntuHandlerFactory
    return UbuntuHandlerFactory()
     

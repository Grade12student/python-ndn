# -----------------------------------------------------------------------------
# Copyright (C) 2019 Xinyu Ma
#
# This file is part of python-ndn.
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
# -----------------------------------------------------------------------------
from ndn.encoding import parse_network_nack, parse_interest, NackReason, Name


class TestNetworkNack:
    @staticmethod
    def test1():
        lp_packet = (b'\xfd\x03 \x05\xfd\x03!\x01\x96'
                     b'P\x43\x05)\x07\x1f\x08\tlocalhost\x08\x03nfd\x08\x05faces\x08\x06events'
                     b'\x21\x00\x12\x00\x0c\x02\x03\xe8')
        nack_reason, interest = parse_network_nack(lp_packet, False)
        assert nack_reason == NackReason.NO_ROUTE
        name, param, _, _ = parse_interest(interest)
        assert name == Name.from_str("/localhost/nfd/faces/events")
        assert param.must_be_fresh
        assert param.can_be_prefix
        assert param.lifetime == 1000

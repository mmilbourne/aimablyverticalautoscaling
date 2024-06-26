"""
This file is part of "Aimably Vertical Autoscaling".

"Aimably Vertical Autoscaling" is free software: you can redistribute it and/or modify it under the terms 
of the GNU General Public License as published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

Aimably Vertical Autoscaling is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along with Foobar. 
If not, see <https://www.gnu.org/licenses/>.
"""
class ScalingTag(object):
    __slots__ = ()
    LowerInstanceClass = "rds_scaling_low_instanceclass"
    UpperInstanceClass = "rds_scaling_high_instanceclass"
    AlertActionTag = 'rds_scaling_action'
    BlueGreenTag = "rds_vertical_scaling_bluegreen"
    AuroraScalingTag = "rds_aurora_scaling"
    AuroraScalingTargetTag = "rds_aurora_scaling_target"
    
class AuroraTagValue(object):
    __slots__ = ()
    Read_Replica = 'read_replica'
    Original_Writer = 'original_writer'
    FailingOver = 'failing_over'

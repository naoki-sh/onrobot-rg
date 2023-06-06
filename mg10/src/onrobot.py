#!/usr/bin/env python3

from pymodbus.client.sync import ModbusTcpClient as ModbusClient


class MG():

    def __init__(self, ip, port):
        self.client = ModbusClient(
            ip,
            port=port,
            stopbits=1,
            bytesize=8,
            parity='E',
            baudrate=115200,
            timeout=1)
        self.open_connection()

    def open_connection(self):
        """Opens the connection with a gripper."""
        ret = self.client.connect()

    def close_connection(self):
        """Closes the connection with the gripper."""
        ret = self.client.close()

    def get_current_strength(self):
        """Reads the current magnetic strength in percent.
        """
        result = self.client.read_holding_registers(
            address=258, count=1, unit=65)
        strength = result.registers[0]
        return strength

    '''
    def get_magnetic_flux_density(self):
        """Reads current width between gripper fingers in 1/10 millimeters.
        Please note that the width is provided without any fingertip offset,
        as it is measured between the insides of the aluminum fingers.
        """
        result = self.client.read_holding_registers(
            address=259, count=1, unit=65)
        width_mm = result.registers[0]
        return width_mm
    '''

    def get_status(self):
        """Reads current device status.
        This status field indicates the status of the gripper and its motion.
        It is composed of 7 flags, described in the table below.
        Bit      Name            Description
        0 (LSB): busy            High (1) when a motion is ongoing,
                                  low (0) when not.
                                  The gripper will only accept new commands
                                  when this flag is low.
        1:       grip detected   High (1) when an internal- or
                                  external grip is detected.
        2:       work detected 
        3:       work dropped ?
        4:       smart grip failed ?
        5: ?
        6: ?
        -16:   reserved        Not used.
        """
        result = self.client.read_holding_registers(
            address=256, count=1, unit=65)
        status = format(result.registers[0], '016b')
        status_list = [0] * 7
        if int(status[-1]):
            print("grasp detected.")
            status_list[0] = 1
        if int(status[-2]):
            print("work detected.")
            status_list[1] = 1
        if int(status[-3]):
            print("busy.")
            status_list[2] = 1
        if int(status[-4]):
            #print("?")
            status_list[3] = 1
        if int(status[-5]):
            #print("?")
            status_list[4] = 1
        if int(status[-6]):
            print("smart grip failed")
            status_list[5] = 1
        if int(status[-7]):
            print("work dropped")
            status_list[6] = 1

        return status_list

    def set_command(self, command):
        """Sends the command to change grasp mode of MG10 gripper.
        Mode 1 (grasp) is only available when the target strength is not zero.
        0: release
        1: grasp
        2: smart_grasp
        """
        if command == 0:
            print("release")
        elif command == 1:
            print("grasp")
        elif command == 2:
            print("smart grip")
        else: 
            print("command value must be 0 ~ 2")
            return 
        result = self.client.write_register(
            address=0, value=command, unit=65)

    def set_target_strength(self, strength_val):
        """Writes the target strength (0 ~ 100 percent)
        """
        result = self.client.write_register(
            address=1, value=strength_val, unit=65)
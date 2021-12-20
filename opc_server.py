from datetime import date, datetime
import logging
import asyncio
import sys
sys.path.insert(0, "..")

from asyncua import Server


async def main():
    _logger = logging.getLogger('asyncua')
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint('opc.tcp://0.0.0.0:4840/freeopcua/server/')

    # populating our address space
    myvar_list = await initialize_nodes(server)


    # read input from previous cyckle of BOY
    f = open('BOY_DATA_2021-12-17-14-35-37.txt', 'r')
    readings = f.readlines()
    sorted_readings = []

    for reading in readings:
        sorted_readings.append(reading.split(','))

    convert_list(sorted_readings)

    _logger.info('Starting server!')
    async with server:
        today = str(date.today())

        _logger.info(type(today))
        _logger.info(type(today))
        _logger.info(type(today))
        _logger.info(today)
        _logger.info(today)
        _logger.info(today)
        _logger.info(today)
        await myvar_list[39].write_value(today)
        await myvar_list[40].write_value(datetime.now().strftime("%H:%M:%S"))
        for reading in sorted_readings:
            for i in range(len(myvar_list) - 10):
                idk2 = reading[i]
                await myvar_list[i].write_value(idk2)
            await myvar_list[40].write_value(datetime.now().strftime("%H:%M:%S"))
            _logger.info('written new line')
            await asyncio.sleep(1)


def convert_list(list_to_sort):
    for i in range(len(list_to_sort)):
        newlist = [convert(x) for x in list_to_sort[i]]
        list_to_sort[i] = newlist


def convert(val):
    constructors = [int, float, str]
    for c in constructors:
        try:
            return c(val)
        except ValueError:
            pass


async def initialize_nodes(server):
    myobj2 = await server.nodes.objects.add_object('ns=2;i=20000', 'TestObject')
    myvar1 = await myobj2.add_variable('ns=2;i=20001', 'ActAverageCycleTime', 0)
    myvar2 = await myobj2.add_variable('ns=2;i=20002', 'ActBackPressure', 0)
    myvar3 = await myobj2.add_variable('ns=2;i=20003', 'ActBackPressureTime', 0)
    myvar4 = await myobj2.add_variable('ns=2;i=20004', 'ActClampingForce', 0)
    myvar5 = await myobj2.add_variable('ns=2;i=20005', 'ActCyclesDone', 0)
    myvar6 = await myobj2.add_variable('ns=2;i=20006', 'ActCycleTime', 0)
    myvar7 = await myobj2.add_variable('ns=2;i=20007', 'ActEffectivity', 0)
    myvar8 = await myobj2.add_variable('ns=2;i=20008', 'ActEnergyTotalPerCycle', 0.0)
    myvar9 = await myobj2.add_variable('ns=2;i=20009', 'ActEnergyTotalPerHour', 0.0)
    myvar10 = await myobj2.add_variable('ns=2;i=20010', 'ActInjectHoldPress', 0)
    myvar11 = await myobj2.add_variable('ns=2;i=20011', 'ActInjectionPressure', 0)
    myvar12 = await myobj2.add_variable('ns=2;i=20012', 'ActLotSize', 0)
    myvar13 = await myobj2.add_variable('ns=2;i=20013', 'ActOPMode', 0)
    myvar14 = await myobj2.add_variable('ns=2;i=20014', 'ActPartsBad', 0)
    myvar15 = await myobj2.add_variable('ns=2;i=20015', 'ActPartsGood', 0)
    myvar16 = await myobj2.add_variable('ns=2;i=20016', 'ActTempEnterZone', 0)
    myvar17 = await myobj2.add_variable('ns=2;i=20017', 'ActTemperatureZone_1', 0)
    myvar18 = await myobj2.add_variable('ns=2;i=20018', 'ActTemperatureZone_10', 0)
    myvar19 = await myobj2.add_variable('ns=2;i=20019', 'ActTemperatureZone_2', 0)
    myvar20 = await myobj2.add_variable('ns=2;i=20020', 'ActTemperatureZone_3', 0)
    myvar21 = await myobj2.add_variable('ns=2;i=20021', 'ActTemperatureZone_4', 0)
    myvar22 = await myobj2.add_variable('ns=2;i=20022', 'ActTemperatureZone_5', 0)
    myvar23 = await myobj2.add_variable('ns=2;i=20023', 'ActTemperatureZone_6', 0)
    myvar24 = await myobj2.add_variable('ns=2;i=20024', 'ActTemperatureZone_7', 0)
    myvar25 = await myobj2.add_variable('ns=2;i=20025', 'ActTemperatureZone_8', 0)
    myvar26 = await myobj2.add_variable('ns=2;i=20026', 'ActTemperatureZone_9', 0)
    myvar27 = await myobj2.add_variable('ns=2;i=20027', 'ActTotalParts', 0)
    myvar28 = await myobj2.add_variable('ns=2;i=20028', 'LastCycleTime', 0)
    myvar29 = await myobj2.add_variable('ns=2;i=20029', 'PDEActDosingTime', 0)
    myvar30 = await myobj2.add_variable('ns=2;i=20030', 'PDEActDosingVolumen', 0)
    myvar31 = await myobj2.add_variable('ns=2;i=20031', 'PDEActInjectionTime', 0)
    myvar32 = await myobj2.add_variable('ns=2;i=20032', 'PDEActMaxInjectionPressure', 0)
    myvar33 = await myobj2.add_variable('ns=2;i=20033', 'PDEActMeltCushion', 0)
    myvar34 = await myobj2.add_variable('ns=2;i=20034', 'PDEActSystemPressureSwitchPoint', 0)
    myvar35 = await myobj2.add_variable('ns=2;i=20035', 'ProductionTimeForecast', 0)
    myvar36 = await myobj2.add_variable('ns=2;i=20036', 'SetCyclesCompleteToDo', 0)
    myvar37 = await myobj2.add_variable('ns=2;i=20037', 'SetLotSize', 0)
    myvar38 = await myobj2.add_variable('ns=2;i=20038', 'SetNumberOfCavities', 0)
    myvar39 = await myobj2.add_variable('ns=2;i=20039', 'SetPieceCounter', 0)
    myvar40 = await myobj2.add_variable('ns=2;i=20040', 'SysDate', 'string')
    myvar41 = await myobj2.add_variable('ns=2;i=20041', 'SysTime', 'string')
    myvar42 = await myobj2.add_variable('ns=2;i=20042', 'StringMaterial.Data', 'string')
    myvar43 = await myobj2.add_variable('ns=2;i=20043', 'StringOrder.Data', 'string')
    myvar44 = await myobj2.add_variable('ns=2;i=20044', 'StringToolName.Data', 'string')
    myvar45 = await myobj2.add_variable('ns=2;i=20045', 'MoldCatActualFilename.Data', 'string')
    myvar46 = await myobj2.add_variable('ns=2;i=20046', 'MoldCatDescription.Data', 'string')
    myvar47 = await myobj2.add_variable('ns=2;i=20047', 'MoldCatFilename.Data', 'string')
    myvar_list = [myvar47, myvar46, myvar45, myvar44, myvar43, myvar42, myvar41, myvar40,
                  myvar39, myvar38, myvar37, myvar36, myvar35, myvar34, myvar33, myvar32,
                  myvar31, myvar30, myvar29, myvar28, myvar27, myvar26, myvar25, myvar24,
                  myvar23, myvar22, myvar21, myvar20, myvar19, myvar18, myvar17, myvar16,
                  myvar15, myvar14, myvar13, myvar12, myvar11, myvar10, myvar9, myvar8,
                  myvar7, myvar6, myvar5, myvar4, myvar3, myvar2, myvar1]
    myvar_list.reverse()

    for myvar in myvar_list:
        await myvar.set_writable()

    return myvar_list


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)

from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers


import pybindgen.settings
import warnings

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        warnings.warn("exception %r in wrapper %s" % (exception, wrapper))
        return True
pybindgen.settings.error_handler = ErrorHandler()


import sys

def module_init():
    root_module = Module('ns.cognitive', cpp_namespace='::ns3')
    return root_module

def register_types(module):
    root_module = module.get_root()
    
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacType [enumeration]
    module.add_enum('WifiMacType', ['WIFI_MAC_CTL_RTS', 'WIFI_MAC_CTL_CTS', 'WIFI_MAC_CTL_ACK', 'WIFI_MAC_CTL_BACKREQ', 'WIFI_MAC_CTL_BACKRESP', 'WIFI_MAC_CTL_CTLWRAPPER', 'WIFI_MAC_MGT_BEACON', 'WIFI_MAC_MGT_ASSOCIATION_REQUEST', 'WIFI_MAC_MGT_ASSOCIATION_RESPONSE', 'WIFI_MAC_MGT_DISASSOCIATION', 'WIFI_MAC_MGT_REASSOCIATION_REQUEST', 'WIFI_MAC_MGT_REASSOCIATION_RESPONSE', 'WIFI_MAC_MGT_PROBE_REQUEST', 'WIFI_MAC_MGT_PROBE_RESPONSE', 'WIFI_MAC_MGT_AUTHENTICATION', 'WIFI_MAC_MGT_DEAUTHENTICATION', 'WIFI_MAC_MGT_ACTION', 'WIFI_MAC_MGT_ACTION_NO_ACK', 'WIFI_MAC_MGT_MULTIHOP_ACTION', 'WIFI_MAC_DATA', 'WIFI_MAC_DATA_CFACK', 'WIFI_MAC_DATA_CFPOLL', 'WIFI_MAC_DATA_CFACK_CFPOLL', 'WIFI_MAC_DATA_NULL', 'WIFI_MAC_DATA_NULL_CFACK', 'WIFI_MAC_DATA_NULL_CFPOLL', 'WIFI_MAC_DATA_NULL_CFACK_CFPOLL', 'WIFI_MAC_QOSDATA', 'WIFI_MAC_QOSDATA_CFACK', 'WIFI_MAC_QOSDATA_CFPOLL', 'WIFI_MAC_QOSDATA_CFACK_CFPOLL', 'WIFI_MAC_QOSDATA_NULL', 'WIFI_MAC_QOSDATA_NULL_CFPOLL', 'WIFI_MAC_QOSDATA_NULL_CFACK_CFPOLL'], import_from_module='ns.wifi')
    ## wifi-preamble.h (module 'wifi'): ns3::WifiPreamble [enumeration]
    module.add_enum('WifiPreamble', ['WIFI_PREAMBLE_LONG', 'WIFI_PREAMBLE_SHORT', 'WIFI_PREAMBLE_HT_MF', 'WIFI_PREAMBLE_HT_GF', 'WIFI_PREAMBLE_VHT', 'WIFI_PREAMBLE_NONE'], import_from_module='ns.wifi')
    ## log.h (module 'core'): ns3::LogLevel [enumeration]
    module.add_enum('LogLevel', ['LOG_NONE', 'LOG_ERROR', 'LOG_LEVEL_ERROR', 'LOG_WARN', 'LOG_LEVEL_WARN', 'LOG_DEBUG', 'LOG_LEVEL_DEBUG', 'LOG_INFO', 'LOG_LEVEL_INFO', 'LOG_FUNCTION', 'LOG_LEVEL_FUNCTION', 'LOG_LOGIC', 'LOG_LEVEL_LOGIC', 'LOG_ALL', 'LOG_LEVEL_ALL', 'LOG_PREFIX_FUNC', 'LOG_PREFIX_TIME', 'LOG_PREFIX_NODE', 'LOG_PREFIX_LEVEL', 'LOG_PREFIX_ALL'], import_from_module='ns.core')
    ## wifi-mode.h (module 'wifi'): ns3::WifiModulationClass [enumeration]
    module.add_enum('WifiModulationClass', ['WIFI_MOD_CLASS_UNKNOWN', 'WIFI_MOD_CLASS_IR', 'WIFI_MOD_CLASS_FHSS', 'WIFI_MOD_CLASS_DSSS', 'WIFI_MOD_CLASS_HR_DSSS', 'WIFI_MOD_CLASS_ERP_PBCC', 'WIFI_MOD_CLASS_DSSS_OFDM', 'WIFI_MOD_CLASS_ERP_OFDM', 'WIFI_MOD_CLASS_OFDM', 'WIFI_MOD_CLASS_HT', 'WIFI_MOD_CLASS_VHT'], import_from_module='ns.wifi')
    ## wifi-phy-standard.h (module 'wifi'): ns3::WifiPhyStandard [enumeration]
    module.add_enum('WifiPhyStandard', ['WIFI_PHY_STANDARD_80211a', 'WIFI_PHY_STANDARD_80211b', 'WIFI_PHY_STANDARD_80211g', 'WIFI_PHY_STANDARD_80211_10MHZ', 'WIFI_PHY_STANDARD_80211_5MHZ', 'WIFI_PHY_STANDARD_holland', 'WIFI_PHY_STANDARD_80211n_2_4GHZ', 'WIFI_PHY_STANDARD_80211n_5GHZ', 'WIFI_PHY_STANDARD_80211ac'], import_from_module='ns.wifi')
    ## wifi-mode.h (module 'wifi'): ns3::WifiCodeRate [enumeration]
    module.add_enum('WifiCodeRate', ['WIFI_CODE_RATE_UNDEFINED', 'WIFI_CODE_RATE_3_4', 'WIFI_CODE_RATE_2_3', 'WIFI_CODE_RATE_1_2', 'WIFI_CODE_RATE_5_6'], import_from_module='ns.wifi')
    ## qos-utils.h (module 'wifi'): ns3::AcIndex [enumeration]
    module.add_enum('AcIndex', ['AC_BE', 'AC_BK', 'AC_VI', 'AC_VO', 'AC_BE_NQOS', 'AC_UNDEF'], import_from_module='ns.wifi')
    ## edca-txop-n.h (module 'wifi'): ns3::TypeOfStation [enumeration]
    module.add_enum('TypeOfStation', ['STA', 'AP', 'ADHOC_STA', 'MESH', 'HT_STA', 'HT_AP', 'HT_ADHOC_STA', 'OCB'], import_from_module='ns.wifi')
    ## ctrl-headers.h (module 'wifi'): ns3::BlockAckType [enumeration]
    module.add_enum('BlockAckType', ['BASIC_BLOCK_ACK', 'COMPRESSED_BLOCK_ACK', 'MULTI_TID_BLOCK_ACK'], import_from_module='ns.wifi')
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketType [enumeration]
    module.add_enum('PacketType', ['CTRL_PACKET', 'DATA_PACKET'])
    ## address.h (module 'network'): ns3::Address [class]
    module.add_class('Address', import_from_module='ns.network')
    ## address.h (module 'network'): ns3::Address::MaxSize_e [enumeration]
    module.add_enum('MaxSize_e', ['MAX_SIZE'], outer_class=root_module['ns3::Address'], import_from_module='ns.network')
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList [class]
    module.add_class('AttributeConstructionList', import_from_module='ns.core')
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item [struct]
    module.add_class('Item', import_from_module='ns.core', outer_class=root_module['ns3::AttributeConstructionList'])
    ## block-ack-manager.h (module 'wifi'): ns3::Bar [struct]
    module.add_class('Bar', import_from_module='ns.wifi')
    ## block-ack-agreement.h (module 'wifi'): ns3::BlockAckAgreement [class]
    module.add_class('BlockAckAgreement', import_from_module='ns.wifi')
    ## block-ack-manager.h (module 'wifi'): ns3::BlockAckManager [class]
    module.add_class('BlockAckManager', import_from_module='ns.wifi')
    ## buffer.h (module 'network'): ns3::Buffer [class]
    module.add_class('Buffer', import_from_module='ns.network')
    ## buffer.h (module 'network'): ns3::Buffer::Iterator [class]
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::Buffer'])
    ## packet.h (module 'network'): ns3::ByteTagIterator [class]
    module.add_class('ByteTagIterator', import_from_module='ns.network')
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item [class]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagIterator'])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList [class]
    module.add_class('ByteTagList', import_from_module='ns.network')
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator [class]
    module.add_class('Iterator', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList'])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item [struct]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::ByteTagList::Iterator'])
    ## callback.h (module 'core'): ns3::CallbackBase [class]
    module.add_class('CallbackBase', import_from_module='ns.core')
    ## command-line.h (module 'core'): ns3::CommandLine [class]
    module.add_class('CommandLine', allow_subclassing=True, import_from_module='ns.core')
    ## system-mutex.h (module 'core'): ns3::CriticalSection [class]
    module.add_class('CriticalSection', import_from_module='ns.core')
    ## event-garbage-collector.h (module 'core'): ns3::EventGarbageCollector [class]
    module.add_class('EventGarbageCollector', import_from_module='ns.core')
    ## event-id.h (module 'core'): ns3::EventId [class]
    module.add_class('EventId', import_from_module='ns.core')
    ## global-value.h (module 'core'): ns3::GlobalValue [class]
    module.add_class('GlobalValue', import_from_module='ns.core')
    ## hash.h (module 'core'): ns3::Hasher [class]
    module.add_class('Hasher', import_from_module='ns.core')
    ## int-to-type.h (module 'core'): ns3::IntToType<0> [struct]
    module.add_class('IntToType', import_from_module='ns.core', template_parameters=['0'])
    ## int-to-type.h (module 'core'): ns3::IntToType<0>::v_e [enumeration]
    module.add_enum('v_e', ['value'], outer_class=root_module['ns3::IntToType< 0 >'], import_from_module='ns.core')
    ## int-to-type.h (module 'core'): ns3::IntToType<1> [struct]
    module.add_class('IntToType', import_from_module='ns.core', template_parameters=['1'])
    ## int-to-type.h (module 'core'): ns3::IntToType<1>::v_e [enumeration]
    module.add_enum('v_e', ['value'], outer_class=root_module['ns3::IntToType< 1 >'], import_from_module='ns.core')
    ## int-to-type.h (module 'core'): ns3::IntToType<2> [struct]
    module.add_class('IntToType', import_from_module='ns.core', template_parameters=['2'])
    ## int-to-type.h (module 'core'): ns3::IntToType<2>::v_e [enumeration]
    module.add_enum('v_e', ['value'], outer_class=root_module['ns3::IntToType< 2 >'], import_from_module='ns.core')
    ## int-to-type.h (module 'core'): ns3::IntToType<3> [struct]
    module.add_class('IntToType', import_from_module='ns.core', template_parameters=['3'])
    ## int-to-type.h (module 'core'): ns3::IntToType<3>::v_e [enumeration]
    module.add_enum('v_e', ['value'], outer_class=root_module['ns3::IntToType< 3 >'], import_from_module='ns.core')
    ## int-to-type.h (module 'core'): ns3::IntToType<4> [struct]
    module.add_class('IntToType', import_from_module='ns.core', template_parameters=['4'])
    ## int-to-type.h (module 'core'): ns3::IntToType<4>::v_e [enumeration]
    module.add_enum('v_e', ['value'], outer_class=root_module['ns3::IntToType< 4 >'], import_from_module='ns.core')
    ## int-to-type.h (module 'core'): ns3::IntToType<5> [struct]
    module.add_class('IntToType', import_from_module='ns.core', template_parameters=['5'])
    ## int-to-type.h (module 'core'): ns3::IntToType<5>::v_e [enumeration]
    module.add_enum('v_e', ['value'], outer_class=root_module['ns3::IntToType< 5 >'], import_from_module='ns.core')
    ## int-to-type.h (module 'core'): ns3::IntToType<6> [struct]
    module.add_class('IntToType', import_from_module='ns.core', template_parameters=['6'])
    ## int-to-type.h (module 'core'): ns3::IntToType<6>::v_e [enumeration]
    module.add_enum('v_e', ['value'], outer_class=root_module['ns3::IntToType< 6 >'], import_from_module='ns.core')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address [class]
    module.add_class('Ipv4Address', import_from_module='ns.network')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address [class]
    root_module['ns3::Ipv4Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask [class]
    module.add_class('Ipv4Mask', import_from_module='ns.network')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address [class]
    module.add_class('Ipv6Address', import_from_module='ns.network')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address [class]
    root_module['ns3::Ipv6Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix [class]
    module.add_class('Ipv6Prefix', import_from_module='ns.network')
    ## log.h (module 'core'): ns3::LogComponent [class]
    module.add_class('LogComponent', import_from_module='ns.core')
    ## mac48-address.h (module 'network'): ns3::Mac48Address [class]
    module.add_class('Mac48Address', import_from_module='ns.network')
    ## mac48-address.h (module 'network'): ns3::Mac48Address [class]
    root_module['ns3::Mac48Address'].implicitly_converts_to(root_module['ns3::Address'])
    ## names.h (module 'core'): ns3::Names [class]
    module.add_class('Names', import_from_module='ns.core')
    ## node-container.h (module 'network'): ns3::NodeContainer [class]
    module.add_class('NodeContainer', import_from_module='ns.network')
    ## non-copyable.h (module 'core'): ns3::NonCopyable [class]
    module.add_class('NonCopyable', destructor_visibility='protected', import_from_module='ns.core')
    ## object-base.h (module 'core'): ns3::ObjectBase [class]
    module.add_class('ObjectBase', allow_subclassing=True, import_from_module='ns.core')
    ## object.h (module 'core'): ns3::ObjectDeleter [struct]
    module.add_class('ObjectDeleter', import_from_module='ns.core')
    ## object-factory.h (module 'core'): ns3::ObjectFactory [class]
    module.add_class('ObjectFactory', import_from_module='ns.core')
    ## originator-block-ack-agreement.h (module 'wifi'): ns3::OriginatorBlockAckAgreement [class]
    module.add_class('OriginatorBlockAckAgreement', import_from_module='ns.wifi', parent=root_module['ns3::BlockAckAgreement'])
    ## originator-block-ack-agreement.h (module 'wifi'): ns3::OriginatorBlockAckAgreement::State [enumeration]
    module.add_enum('State', ['PENDING', 'ESTABLISHED', 'INACTIVE', 'UNSUCCESSFUL'], outer_class=root_module['ns3::OriginatorBlockAckAgreement'], import_from_module='ns.wifi')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata [class]
    module.add_class('PacketMetadata', import_from_module='ns.network')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item [struct]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item [enumeration]
    module.add_enum('', ['PAYLOAD', 'HEADER', 'TRAILER'], outer_class=root_module['ns3::PacketMetadata::Item'], import_from_module='ns.network')
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator [class]
    module.add_class('ItemIterator', import_from_module='ns.network', outer_class=root_module['ns3::PacketMetadata'])
    ## packet.h (module 'network'): ns3::PacketTagIterator [class]
    module.add_class('PacketTagIterator', import_from_module='ns.network')
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item [class]
    module.add_class('Item', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagIterator'])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList [class]
    module.add_class('PacketTagList', import_from_module='ns.network')
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData [struct]
    module.add_class('TagData', import_from_module='ns.network', outer_class=root_module['ns3::PacketTagList'])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData_e [enumeration]
    module.add_enum('TagData_e', ['MAX_SIZE'], outer_class=root_module['ns3::PacketTagList::TagData'], import_from_module='ns.network')
    ## log.h (module 'core'): ns3::ParameterLogger [class]
    module.add_class('ParameterLogger', import_from_module='ns.core')
    ## pu-model.h (module 'cognitive'): ns3::PuActivity [struct]
    module.add_class('PuActivity')
    ## random-variable-stream-helper.h (module 'core'): ns3::RandomVariableStreamHelper [class]
    module.add_class('RandomVariableStreamHelper', import_from_module='ns.core')
    ## repository.h (module 'cognitive'): ns3::RepositoryEntryRecv [struct]
    module.add_class('RepositoryEntryRecv')
    ## repository.h (module 'cognitive'): ns3::RepositoryEntrySend [struct]
    module.add_class('RepositoryEntrySend')
    ## rng-seed-manager.h (module 'core'): ns3::RngSeedManager [class]
    module.add_class('RngSeedManager', import_from_module='ns.core')
    ## rng-stream.h (module 'core'): ns3::RngStream [class]
    module.add_class('RngStream', import_from_module='ns.core')
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter> [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Object', 'ns3::ObjectBase', 'ns3::ObjectDeleter'], parent=root_module['ns3::ObjectBase'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simulator.h (module 'core'): ns3::Simulator [class]
    module.add_class('Simulator', destructor_visibility='private', import_from_module='ns.core')
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumEntry [struct]
    module.add_class('SpectrumEntry')
    ## spectrum-manager.h (module 'cognitive'): ns3::SpectrumManager [class]
    module.add_class('SpectrumManager')
    ## spectrum-sensing.h (module 'cognitive'): ns3::SpectrumSensing [class]
    module.add_class('SpectrumSensing')
    ## system-condition.h (module 'core'): ns3::SystemCondition [class]
    module.add_class('SystemCondition', import_from_module='ns.core')
    ## system-mutex.h (module 'core'): ns3::SystemMutex [class]
    module.add_class('SystemMutex', import_from_module='ns.core')
    ## system-wall-clock-ms.h (module 'core'): ns3::SystemWallClockMs [class]
    module.add_class('SystemWallClockMs', import_from_module='ns.core')
    ## tag.h (module 'network'): ns3::Tag [class]
    module.add_class('Tag', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    ## tag-buffer.h (module 'network'): ns3::TagBuffer [class]
    module.add_class('TagBuffer', import_from_module='ns.network')
    ## nstime.h (module 'core'): ns3::TimeWithUnit [class]
    module.add_class('TimeWithUnit', import_from_module='ns.core')
    ## timer.h (module 'core'): ns3::Timer [class]
    module.add_class('Timer', import_from_module='ns.core')
    ## timer.h (module 'core'): ns3::Timer::DestroyPolicy [enumeration]
    module.add_enum('DestroyPolicy', ['CANCEL_ON_DESTROY', 'REMOVE_ON_DESTROY', 'CHECK_ON_DESTROY'], outer_class=root_module['ns3::Timer'], import_from_module='ns.core')
    ## timer.h (module 'core'): ns3::Timer::State [enumeration]
    module.add_enum('State', ['RUNNING', 'EXPIRED', 'SUSPENDED'], outer_class=root_module['ns3::Timer'], import_from_module='ns.core')
    ## timer-impl.h (module 'core'): ns3::TimerImpl [class]
    module.add_class('TimerImpl', allow_subclassing=True, import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId [class]
    module.add_class('TypeId', import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId::AttributeFlag [enumeration]
    module.add_enum('AttributeFlag', ['ATTR_GET', 'ATTR_SET', 'ATTR_CONSTRUCT', 'ATTR_SGC'], outer_class=root_module['ns3::TypeId'], import_from_module='ns.core')
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation [struct]
    module.add_class('AttributeInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation [struct]
    module.add_class('TraceSourceInformation', import_from_module='ns.core', outer_class=root_module['ns3::TypeId'])
    ## vector.h (module 'core'): ns3::Vector2D [class]
    module.add_class('Vector2D', import_from_module='ns.core')
    ## vector.h (module 'core'): ns3::Vector3D [class]
    module.add_class('Vector3D', import_from_module='ns.core')
    ## watchdog.h (module 'core'): ns3::Watchdog [class]
    module.add_class('Watchdog', import_from_module='ns.core')
    ## wifi-mode.h (module 'wifi'): ns3::WifiMode [class]
    module.add_class('WifiMode', import_from_module='ns.wifi')
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeFactory [class]
    module.add_class('WifiModeFactory', import_from_module='ns.wifi')
    ## wifi-phy.h (module 'wifi'): ns3::WifiPhyListener [class]
    module.add_class('WifiPhyListener', allow_subclassing=True, import_from_module='ns.wifi')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation [struct]
    module.add_class('WifiRemoteStation', import_from_module='ns.wifi')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationInfo [class]
    module.add_class('WifiRemoteStationInfo', import_from_module='ns.wifi')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState [struct]
    module.add_class('WifiRemoteStationState', import_from_module='ns.wifi')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState [enumeration]
    module.add_enum('', ['BRAND_NEW', 'DISASSOC', 'WAIT_ASSOC_TX_OK', 'GOT_ASSOC_TX_OK'], outer_class=root_module['ns3::WifiRemoteStationState'], import_from_module='ns.wifi')
    ## wifi-tx-vector.h (module 'wifi'): ns3::WifiTxVector [class]
    module.add_class('WifiTxVector', import_from_module='ns.wifi')
    ## empty.h (module 'core'): ns3::empty [class]
    module.add_class('empty', import_from_module='ns.core')
    ## int64x64-double.h (module 'core'): ns3::int64x64_t [class]
    module.add_class('int64x64_t', import_from_module='ns.core')
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::impl_type [enumeration]
    module.add_enum('impl_type', ['int128_impl', 'cairo_impl', 'ld_impl'], outer_class=root_module['ns3::int64x64_t'], import_from_module='ns.core')
    ## wifi-phy.h (module 'wifi'): ns3::mpduInfo [struct]
    module.add_class('mpduInfo', import_from_module='ns.wifi')
    ## wifi-phy.h (module 'wifi'): ns3::signalNoiseDbm [struct]
    module.add_class('signalNoiseDbm', import_from_module='ns.wifi')
    ## chunk.h (module 'network'): ns3::Chunk [class]
    module.add_class('Chunk', import_from_module='ns.network', parent=root_module['ns3::ObjectBase'])
    ## header.h (module 'network'): ns3::Header [class]
    module.add_class('Header', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    ## object.h (module 'core'): ns3::Object [class]
    module.add_class('Object', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    ## object.h (module 'core'): ns3::Object::AggregateIterator [class]
    module.add_class('AggregateIterator', import_from_module='ns.core', outer_class=root_module['ns3::Object'])
    ## pu-model.h (module 'cognitive'): ns3::PUModel [class]
    module.add_class('PUModel', parent=root_module['ns3::Object'])
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketChannelPacketTag [class]
    module.add_class('PacketChannelPacketTag', parent=root_module['ns3::Tag'])
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketTypePacketTag [class]
    module.add_class('PacketTypePacketTag', parent=root_module['ns3::Tag'])
    ## random-variable-stream.h (module 'core'): ns3::RandomVariableStream [class]
    module.add_class('RandomVariableStream', import_from_module='ns.core', parent=root_module['ns3::Object'])
    ## repository.h (module 'cognitive'): ns3::Repository [class]
    module.add_class('Repository', parent=root_module['ns3::Object'])
    ## scheduler.h (module 'core'): ns3::Scheduler [class]
    module.add_class('Scheduler', import_from_module='ns.core', parent=root_module['ns3::Object'])
    ## scheduler.h (module 'core'): ns3::Scheduler::Event [struct]
    module.add_class('Event', import_from_module='ns.core', outer_class=root_module['ns3::Scheduler'])
    ## scheduler.h (module 'core'): ns3::Scheduler::EventKey [struct]
    module.add_class('EventKey', import_from_module='ns.core', outer_class=root_module['ns3::Scheduler'])
    ## random-variable-stream.h (module 'core'): ns3::SequentialRandomVariable [class]
    module.add_class('SequentialRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeChecker', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeChecker>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::AttributeValue', 'ns3::empty', 'ns3::DefaultDeleter<ns3::AttributeValue>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::CallbackImplBase', 'ns3::empty', 'ns3::DefaultDeleter<ns3::CallbackImplBase>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::EventImpl', 'ns3::empty', 'ns3::DefaultDeleter<ns3::EventImpl>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::FdReader, ns3::empty, ns3::DefaultDeleter<ns3::FdReader> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::FdReader', 'ns3::empty', 'ns3::DefaultDeleter<ns3::FdReader>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Hash::Implementation', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Hash::Implementation>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::NixVector', 'ns3::empty', 'ns3::DefaultDeleter<ns3::NixVector>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::Packet', 'ns3::empty', 'ns3::DefaultDeleter<ns3::Packet>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter<ns3::RefCountBase> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::RefCountBase', 'ns3::empty', 'ns3::DefaultDeleter<ns3::RefCountBase>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SystemThread, ns3::empty, ns3::DefaultDeleter<ns3::SystemThread> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::SystemThread', 'ns3::empty', 'ns3::DefaultDeleter<ns3::SystemThread>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::TraceSourceAccessor', 'ns3::empty', 'ns3::DefaultDeleter<ns3::TraceSourceAccessor>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter<ns3::WifiInformationElement> > [class]
    module.add_class('SimpleRefCount', automatic_type_narrowing=True, import_from_module='ns.core', template_parameters=['ns3::WifiInformationElement', 'ns3::empty', 'ns3::DefaultDeleter<ns3::WifiInformationElement>'], parent=root_module['ns3::empty'], memory_policy=cppclass.ReferenceCountingMethodsPolicy(incref_method='Ref', decref_method='Unref', peekref_method='GetReferenceCount'))
    ## simulator-impl.h (module 'core'): ns3::SimulatorImpl [class]
    module.add_class('SimulatorImpl', import_from_module='ns.core', parent=root_module['ns3::Object'])
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumData [class]
    module.add_class('SpectrumData', parent=root_module['ns3::Object'])
    ## spectrum-decision.h (module 'cognitive'): ns3::SpectrumDecision [class]
    module.add_class('SpectrumDecision', parent=root_module['ns3::Object'])
    ## synchronizer.h (module 'core'): ns3::Synchronizer [class]
    module.add_class('Synchronizer', import_from_module='ns.core', parent=root_module['ns3::Object'])
    ## system-thread.h (module 'core'): ns3::SystemThread [class]
    module.add_class('SystemThread', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::SystemThread, ns3::empty, ns3::DefaultDeleter<ns3::SystemThread> >'])
    ## nstime.h (module 'core'): ns3::Time [class]
    module.add_class('Time', import_from_module='ns.core')
    ## nstime.h (module 'core'): ns3::Time::Unit [enumeration]
    module.add_enum('Unit', ['Y', 'D', 'H', 'MIN', 'S', 'MS', 'US', 'NS', 'PS', 'FS', 'LAST'], outer_class=root_module['ns3::Time'], import_from_module='ns.core')
    ## nstime.h (module 'core'): ns3::Time [class]
    root_module['ns3::Time'].implicitly_converts_to(root_module['ns3::int64x64_t'])
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor [class]
    module.add_class('TraceSourceAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    ## trailer.h (module 'network'): ns3::Trailer [class]
    module.add_class('Trailer', import_from_module='ns.network', parent=root_module['ns3::Chunk'])
    ## random-variable-stream.h (module 'core'): ns3::TriangularRandomVariable [class]
    module.add_class('TriangularRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::UniformRandomVariable [class]
    module.add_class('UniformRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## wall-clock-synchronizer.h (module 'core'): ns3::WallClockSynchronizer [class]
    module.add_class('WallClockSynchronizer', import_from_module='ns.core', parent=root_module['ns3::Synchronizer'])
    ## random-variable-stream.h (module 'core'): ns3::WeibullRandomVariable [class]
    module.add_class('WeibullRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## wifi-information-element.h (module 'wifi'): ns3::WifiInformationElement [class]
    module.add_class('WifiInformationElement', import_from_module='ns.wifi', parent=root_module['ns3::SimpleRefCount< ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter<ns3::WifiInformationElement> >'])
    ## wifi-mac.h (module 'wifi'): ns3::WifiMac [class]
    module.add_class('WifiMac', import_from_module='ns.wifi', parent=root_module['ns3::Object'])
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacHeader [class]
    module.add_class('WifiMacHeader', import_from_module='ns.wifi', parent=root_module['ns3::Header'])
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacHeader::QosAckPolicy [enumeration]
    module.add_enum('QosAckPolicy', ['NORMAL_ACK', 'NO_ACK', 'NO_EXPLICIT_ACK', 'BLOCK_ACK'], outer_class=root_module['ns3::WifiMacHeader'], import_from_module='ns.wifi')
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacHeader::AddressType [enumeration]
    module.add_enum('AddressType', ['ADDR1', 'ADDR2', 'ADDR3', 'ADDR4'], outer_class=root_module['ns3::WifiMacHeader'], import_from_module='ns.wifi')
    ## wifi-phy.h (module 'wifi'): ns3::WifiPhy [class]
    module.add_class('WifiPhy', import_from_module='ns.wifi', parent=root_module['ns3::Object'])
    ## wifi-phy.h (module 'wifi'): ns3::WifiPhy::State [enumeration]
    module.add_enum('State', ['IDLE', 'CCA_BUSY', 'TX', 'RX', 'SWITCHING', 'SENSING', 'SLEEP'], outer_class=root_module['ns3::WifiPhy'], import_from_module='ns.wifi')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationManager [class]
    module.add_class('WifiRemoteStationManager', import_from_module='ns.wifi', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::ZetaRandomVariable [class]
    module.add_class('ZetaRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## random-variable-stream.h (module 'core'): ns3::ZipfRandomVariable [class]
    module.add_class('ZipfRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## attribute.h (module 'core'): ns3::AttributeAccessor [class]
    module.add_class('AttributeAccessor', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    ## attribute.h (module 'core'): ns3::AttributeChecker [class]
    module.add_class('AttributeChecker', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    ## attribute.h (module 'core'): ns3::AttributeValue [class]
    module.add_class('AttributeValue', allow_subclassing=False, automatic_type_narrowing=True, import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    ## boolean.h (module 'core'): ns3::BooleanChecker [class]
    module.add_class('BooleanChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## boolean.h (module 'core'): ns3::BooleanValue [class]
    module.add_class('BooleanValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## calendar-scheduler.h (module 'core'): ns3::CalendarScheduler [class]
    module.add_class('CalendarScheduler', import_from_module='ns.core', parent=root_module['ns3::Scheduler'])
    ## callback.h (module 'core'): ns3::CallbackChecker [class]
    module.add_class('CallbackChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## callback.h (module 'core'): ns3::CallbackImplBase [class]
    module.add_class('CallbackImplBase', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    ## callback.h (module 'core'): ns3::CallbackValue [class]
    module.add_class('CallbackValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## random-variable-stream.h (module 'core'): ns3::ConstantRandomVariable [class]
    module.add_class('ConstantRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## ctrl-headers.h (module 'wifi'): ns3::CtrlBAckRequestHeader [class]
    module.add_class('CtrlBAckRequestHeader', import_from_module='ns.wifi', parent=root_module['ns3::Header'])
    ## ctrl-headers.h (module 'wifi'): ns3::CtrlBAckResponseHeader [class]
    module.add_class('CtrlBAckResponseHeader', import_from_module='ns.wifi', parent=root_module['ns3::Header'])
    ## dcf.h (module 'wifi'): ns3::Dcf [class]
    module.add_class('Dcf', import_from_module='ns.wifi', parent=root_module['ns3::Object'])
    ## default-simulator-impl.h (module 'core'): ns3::DefaultSimulatorImpl [class]
    module.add_class('DefaultSimulatorImpl', import_from_module='ns.core', parent=root_module['ns3::SimulatorImpl'])
    ## random-variable-stream.h (module 'core'): ns3::DeterministicRandomVariable [class]
    module.add_class('DeterministicRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## double.h (module 'core'): ns3::DoubleValue [class]
    module.add_class('DoubleValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## edca-txop-n.h (module 'wifi'): ns3::EdcaTxopN [class]
    module.add_class('EdcaTxopN', import_from_module='ns.wifi', parent=root_module['ns3::Dcf'])
    ## random-variable-stream.h (module 'core'): ns3::EmpiricalRandomVariable [class]
    module.add_class('EmpiricalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue [class]
    module.add_class('EmptyAttributeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## enum.h (module 'core'): ns3::EnumChecker [class]
    module.add_class('EnumChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## enum.h (module 'core'): ns3::EnumValue [class]
    module.add_class('EnumValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## random-variable-stream.h (module 'core'): ns3::ErlangRandomVariable [class]
    module.add_class('ErlangRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## event-impl.h (module 'core'): ns3::EventImpl [class]
    module.add_class('EventImpl', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    ## random-variable-stream.h (module 'core'): ns3::ExponentialRandomVariable [class]
    module.add_class('ExponentialRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## unix-fd-reader.h (module 'core'): ns3::FdReader [class]
    module.add_class('FdReader', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::FdReader, ns3::empty, ns3::DefaultDeleter<ns3::FdReader> >'])
    ## random-variable-stream.h (module 'core'): ns3::GammaRandomVariable [class]
    module.add_class('GammaRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## heap-scheduler.h (module 'core'): ns3::HeapScheduler [class]
    module.add_class('HeapScheduler', import_from_module='ns.core', parent=root_module['ns3::Scheduler'])
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilities [class]
    module.add_class('HtCapabilities', import_from_module='ns.wifi', parent=root_module['ns3::WifiInformationElement'])
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilitiesChecker [class]
    module.add_class('HtCapabilitiesChecker', import_from_module='ns.wifi', parent=root_module['ns3::AttributeChecker'])
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilitiesValue [class]
    module.add_class('HtCapabilitiesValue', import_from_module='ns.wifi', parent=root_module['ns3::AttributeValue'])
    ## integer.h (module 'core'): ns3::IntegerValue [class]
    module.add_class('IntegerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker [class]
    module.add_class('Ipv4AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue [class]
    module.add_class('Ipv4AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker [class]
    module.add_class('Ipv4MaskChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue [class]
    module.add_class('Ipv4MaskValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker [class]
    module.add_class('Ipv6AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue [class]
    module.add_class('Ipv6AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker [class]
    module.add_class('Ipv6PrefixChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue [class]
    module.add_class('Ipv6PrefixValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## list-scheduler.h (module 'core'): ns3::ListScheduler [class]
    module.add_class('ListScheduler', import_from_module='ns.core', parent=root_module['ns3::Scheduler'])
    ## random-variable-stream.h (module 'core'): ns3::LogNormalRandomVariable [class]
    module.add_class('LogNormalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker [class]
    module.add_class('Mac48AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue [class]
    module.add_class('Mac48AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## map-scheduler.h (module 'core'): ns3::MapScheduler [class]
    module.add_class('MapScheduler', import_from_module='ns.core', parent=root_module['ns3::Scheduler'])
    ## net-device.h (module 'network'): ns3::NetDevice [class]
    module.add_class('NetDevice', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## net-device.h (module 'network'): ns3::NetDevice::PacketType [enumeration]
    module.add_enum('PacketType', ['PACKET_HOST', 'NS3_PACKET_HOST', 'PACKET_BROADCAST', 'NS3_PACKET_BROADCAST', 'PACKET_MULTICAST', 'NS3_PACKET_MULTICAST', 'PACKET_OTHERHOST', 'NS3_PACKET_OTHERHOST'], outer_class=root_module['ns3::NetDevice'], import_from_module='ns.network')
    ## nix-vector.h (module 'network'): ns3::NixVector [class]
    module.add_class('NixVector', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    ## node.h (module 'network'): ns3::Node [class]
    module.add_class('Node', import_from_module='ns.network', parent=root_module['ns3::Object'])
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable [class]
    module.add_class('NormalRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker [class]
    module.add_class('ObjectFactoryChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue [class]
    module.add_class('ObjectFactoryValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerAccessor [class]
    module.add_class('ObjectPtrContainerAccessor', import_from_module='ns.core', parent=root_module['ns3::AttributeAccessor'])
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerChecker [class]
    module.add_class('ObjectPtrContainerChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerValue [class]
    module.add_class('ObjectPtrContainerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## packet.h (module 'network'): ns3::Packet [class]
    module.add_class('Packet', import_from_module='ns.network', parent=root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    ## random-variable-stream.h (module 'core'): ns3::ParetoRandomVariable [class]
    module.add_class('ParetoRandomVariable', import_from_module='ns.core', parent=root_module['ns3::RandomVariableStream'])
    ## pointer.h (module 'core'): ns3::PointerChecker [class]
    module.add_class('PointerChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## pointer.h (module 'core'): ns3::PointerValue [class]
    module.add_class('PointerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## realtime-simulator-impl.h (module 'core'): ns3::RealtimeSimulatorImpl [class]
    module.add_class('RealtimeSimulatorImpl', import_from_module='ns.core', parent=root_module['ns3::SimulatorImpl'])
    ## realtime-simulator-impl.h (module 'core'): ns3::RealtimeSimulatorImpl::SynchronizationMode [enumeration]
    module.add_enum('SynchronizationMode', ['SYNC_BEST_EFFORT', 'SYNC_HARD_LIMIT'], outer_class=root_module['ns3::RealtimeSimulatorImpl'], import_from_module='ns.core')
    ## ref-count-base.h (module 'core'): ns3::RefCountBase [class]
    module.add_class('RefCountBase', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter<ns3::RefCountBase> >'])
    ## regular-wifi-mac.h (module 'wifi'): ns3::RegularWifiMac [class]
    module.add_class('RegularWifiMac', import_from_module='ns.wifi', parent=root_module['ns3::WifiMac'])
    ## ssid.h (module 'wifi'): ns3::Ssid [class]
    module.add_class('Ssid', import_from_module='ns.wifi', parent=root_module['ns3::WifiInformationElement'])
    ## ssid.h (module 'wifi'): ns3::SsidChecker [class]
    module.add_class('SsidChecker', import_from_module='ns.wifi', parent=root_module['ns3::AttributeChecker'])
    ## ssid.h (module 'wifi'): ns3::SsidValue [class]
    module.add_class('SsidValue', import_from_module='ns.wifi', parent=root_module['ns3::AttributeValue'])
    ## string.h (module 'core'): ns3::StringChecker [class]
    module.add_class('StringChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## string.h (module 'core'): ns3::StringValue [class]
    module.add_class('StringValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## nstime.h (module 'core'): ns3::TimeValue [class]
    module.add_class('TimeValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## type-id.h (module 'core'): ns3::TypeIdChecker [class]
    module.add_class('TypeIdChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## type-id.h (module 'core'): ns3::TypeIdValue [class]
    module.add_class('TypeIdValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## uinteger.h (module 'core'): ns3::UintegerValue [class]
    module.add_class('UintegerValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## vector.h (module 'core'): ns3::Vector2DChecker [class]
    module.add_class('Vector2DChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## vector.h (module 'core'): ns3::Vector2DValue [class]
    module.add_class('Vector2DValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## vector.h (module 'core'): ns3::Vector3DChecker [class]
    module.add_class('Vector3DChecker', import_from_module='ns.core', parent=root_module['ns3::AttributeChecker'])
    ## vector.h (module 'core'): ns3::Vector3DValue [class]
    module.add_class('Vector3DValue', import_from_module='ns.core', parent=root_module['ns3::AttributeValue'])
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilities [class]
    module.add_class('VhtCapabilities', import_from_module='ns.wifi', parent=root_module['ns3::WifiInformationElement'])
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilitiesChecker [class]
    module.add_class('VhtCapabilitiesChecker', import_from_module='ns.wifi', parent=root_module['ns3::AttributeChecker'])
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilitiesValue [class]
    module.add_class('VhtCapabilitiesValue', import_from_module='ns.wifi', parent=root_module['ns3::AttributeValue'])
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeChecker [class]
    module.add_class('WifiModeChecker', import_from_module='ns.wifi', parent=root_module['ns3::AttributeChecker'])
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeValue [class]
    module.add_class('WifiModeValue', import_from_module='ns.wifi', parent=root_module['ns3::AttributeValue'])
    ## address.h (module 'network'): ns3::AddressChecker [class]
    module.add_class('AddressChecker', import_from_module='ns.network', parent=root_module['ns3::AttributeChecker'])
    ## address.h (module 'network'): ns3::AddressValue [class]
    module.add_class('AddressValue', import_from_module='ns.network', parent=root_module['ns3::AttributeValue'])
    ## dca-txop.h (module 'wifi'): ns3::DcaTxop [class]
    module.add_class('DcaTxop', import_from_module='ns.wifi', parent=root_module['ns3::Dcf'])
    module.add_container('std::map< std::string, ns3::LogComponent * >', ('std::string', 'ns3::LogComponent *'), container_type=u'map')
    module.add_container('ns3::WifiModeList', 'ns3::WifiMode', container_type=u'vector')
    typehandlers.add_type_alias(u'ns3::RngSeedManager', u'ns3::SeedManager')
    typehandlers.add_type_alias(u'ns3::RngSeedManager*', u'ns3::SeedManager*')
    typehandlers.add_type_alias(u'ns3::RngSeedManager&', u'ns3::SeedManager&')
    module.add_typedef(root_module['ns3::RngSeedManager'], 'SeedManager')
    typehandlers.add_type_alias(u'ns3::ObjectPtrContainerValue', u'ns3::ObjectVectorValue')
    typehandlers.add_type_alias(u'ns3::ObjectPtrContainerValue*', u'ns3::ObjectVectorValue*')
    typehandlers.add_type_alias(u'ns3::ObjectPtrContainerValue&', u'ns3::ObjectVectorValue&')
    module.add_typedef(root_module['ns3::ObjectPtrContainerValue'], 'ObjectVectorValue')
    typehandlers.add_type_alias(u'uint8_t', u'ns3::WifiInformationElementId')
    typehandlers.add_type_alias(u'uint8_t*', u'ns3::WifiInformationElementId*')
    typehandlers.add_type_alias(u'uint8_t&', u'ns3::WifiInformationElementId&')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *', u'ns3::LogNodePrinter')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) **', u'ns3::LogNodePrinter*')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *&', u'ns3::LogNodePrinter&')
    typehandlers.add_type_alias(u'ns3::Vector3D', u'ns3::Vector')
    typehandlers.add_type_alias(u'ns3::Vector3D*', u'ns3::Vector*')
    typehandlers.add_type_alias(u'ns3::Vector3D&', u'ns3::Vector&')
    module.add_typedef(root_module['ns3::Vector3D'], 'Vector')
    typehandlers.add_type_alias(u'std::vector< ns3::WifiMode, std::allocator< ns3::WifiMode > >', u'ns3::WifiModeList')
    typehandlers.add_type_alias(u'std::vector< ns3::WifiMode, std::allocator< ns3::WifiMode > >*', u'ns3::WifiModeList*')
    typehandlers.add_type_alias(u'std::vector< ns3::WifiMode, std::allocator< ns3::WifiMode > >&', u'ns3::WifiModeList&')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *', u'ns3::LogTimePrinter')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) **', u'ns3::LogTimePrinter*')
    typehandlers.add_type_alias(u'void ( * ) ( std::ostream & ) *&', u'ns3::LogTimePrinter&')
    typehandlers.add_type_alias(u'ns3::Vector3DValue', u'ns3::VectorValue')
    typehandlers.add_type_alias(u'ns3::Vector3DValue*', u'ns3::VectorValue*')
    typehandlers.add_type_alias(u'ns3::Vector3DValue&', u'ns3::VectorValue&')
    module.add_typedef(root_module['ns3::Vector3DValue'], 'VectorValue')
    typehandlers.add_type_alias(u'ns3::ObjectPtrContainerValue', u'ns3::ObjectMapValue')
    typehandlers.add_type_alias(u'ns3::ObjectPtrContainerValue*', u'ns3::ObjectMapValue*')
    typehandlers.add_type_alias(u'ns3::ObjectPtrContainerValue&', u'ns3::ObjectMapValue&')
    module.add_typedef(root_module['ns3::ObjectPtrContainerValue'], 'ObjectMapValue')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker', u'ns3::VectorChecker')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker*', u'ns3::VectorChecker*')
    typehandlers.add_type_alias(u'ns3::Vector3DChecker&', u'ns3::VectorChecker&')
    module.add_typedef(root_module['ns3::Vector3DChecker'], 'VectorChecker')
    typehandlers.add_type_alias(u'__gnu_cxx::__normal_iterator< ns3::WifiMode const *, std::vector< ns3::WifiMode, std::allocator< ns3::WifiMode > > >', u'ns3::WifiModeListIterator')
    typehandlers.add_type_alias(u'__gnu_cxx::__normal_iterator< ns3::WifiMode const *, std::vector< ns3::WifiMode, std::allocator< ns3::WifiMode > > >*', u'ns3::WifiModeListIterator*')
    typehandlers.add_type_alias(u'__gnu_cxx::__normal_iterator< ns3::WifiMode const *, std::vector< ns3::WifiMode, std::allocator< ns3::WifiMode > > >&', u'ns3::WifiModeListIterator&')
    
    ## Register a nested module for the namespace CommandLineHelper
    
    nested_module = module.add_cpp_namespace('CommandLineHelper')
    register_types_ns3_CommandLineHelper(nested_module)
    
    
    ## Register a nested module for the namespace Config
    
    nested_module = module.add_cpp_namespace('Config')
    register_types_ns3_Config(nested_module)
    
    
    ## Register a nested module for the namespace FatalImpl
    
    nested_module = module.add_cpp_namespace('FatalImpl')
    register_types_ns3_FatalImpl(nested_module)
    
    
    ## Register a nested module for the namespace Hash
    
    nested_module = module.add_cpp_namespace('Hash')
    register_types_ns3_Hash(nested_module)
    
    
    ## Register a nested module for the namespace SystemPath
    
    nested_module = module.add_cpp_namespace('SystemPath')
    register_types_ns3_SystemPath(nested_module)
    
    
    ## Register a nested module for the namespace TracedValueCallback
    
    nested_module = module.add_cpp_namespace('TracedValueCallback')
    register_types_ns3_TracedValueCallback(nested_module)
    
    
    ## Register a nested module for the namespace internal
    
    nested_module = module.add_cpp_namespace('internal')
    register_types_ns3_internal(nested_module)
    

def register_types_ns3_CommandLineHelper(module):
    root_module = module.get_root()
    

def register_types_ns3_Config(module):
    root_module = module.get_root()
    
    ## config.h (module 'core'): ns3::Config::MatchContainer [class]
    module.add_class('MatchContainer', import_from_module='ns.core')
    module.add_container('std::vector< ns3::Ptr< ns3::Object > >', 'ns3::Ptr< ns3::Object >', container_type=u'vector')
    module.add_container('std::vector< std::string >', 'std::string', container_type=u'vector')

def register_types_ns3_FatalImpl(module):
    root_module = module.get_root()
    

def register_types_ns3_Hash(module):
    root_module = module.get_root()
    
    ## hash-function.h (module 'core'): ns3::Hash::Implementation [class]
    module.add_class('Implementation', import_from_module='ns.core', parent=root_module['ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >'])
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, size_t ) *', u'ns3::Hash::Hash32Function_ptr')
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, size_t ) **', u'ns3::Hash::Hash32Function_ptr*')
    typehandlers.add_type_alias(u'uint32_t ( * ) ( char const *, size_t ) *&', u'ns3::Hash::Hash32Function_ptr&')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, size_t ) *', u'ns3::Hash::Hash64Function_ptr')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, size_t ) **', u'ns3::Hash::Hash64Function_ptr*')
    typehandlers.add_type_alias(u'uint64_t ( * ) ( char const *, size_t ) *&', u'ns3::Hash::Hash64Function_ptr&')
    
    ## Register a nested module for the namespace Function
    
    nested_module = module.add_cpp_namespace('Function')
    register_types_ns3_Hash_Function(nested_module)
    

def register_types_ns3_Hash_Function(module):
    root_module = module.get_root()
    
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a [class]
    module.add_class('Fnv1a', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32 [class]
    module.add_class('Hash32', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64 [class]
    module.add_class('Hash64', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3 [class]
    module.add_class('Murmur3', import_from_module='ns.core', parent=root_module['ns3::Hash::Implementation'])

def register_types_ns3_SystemPath(module):
    root_module = module.get_root()
    
    module.add_container('std::list< std::string >', 'std::string', container_type=u'list')

def register_types_ns3_TracedValueCallback(module):
    root_module = module.get_root()
    
    typehandlers.add_type_alias(u'void ( * ) ( double, double ) *', u'ns3::TracedValueCallback::Double')
    typehandlers.add_type_alias(u'void ( * ) ( double, double ) **', u'ns3::TracedValueCallback::Double*')
    typehandlers.add_type_alias(u'void ( * ) ( double, double ) *&', u'ns3::TracedValueCallback::Double&')
    typehandlers.add_type_alias(u'void ( * ) ( uint8_t, uint8_t ) *', u'ns3::TracedValueCallback::Uint8')
    typehandlers.add_type_alias(u'void ( * ) ( uint8_t, uint8_t ) **', u'ns3::TracedValueCallback::Uint8*')
    typehandlers.add_type_alias(u'void ( * ) ( uint8_t, uint8_t ) *&', u'ns3::TracedValueCallback::Uint8&')
    typehandlers.add_type_alias(u'void ( * ) ( int32_t, int32_t ) *', u'ns3::TracedValueCallback::Int32')
    typehandlers.add_type_alias(u'void ( * ) ( int32_t, int32_t ) **', u'ns3::TracedValueCallback::Int32*')
    typehandlers.add_type_alias(u'void ( * ) ( int32_t, int32_t ) *&', u'ns3::TracedValueCallback::Int32&')
    typehandlers.add_type_alias(u'void ( * ) ( bool, bool ) *', u'ns3::TracedValueCallback::Bool')
    typehandlers.add_type_alias(u'void ( * ) ( bool, bool ) **', u'ns3::TracedValueCallback::Bool*')
    typehandlers.add_type_alias(u'void ( * ) ( bool, bool ) *&', u'ns3::TracedValueCallback::Bool&')
    typehandlers.add_type_alias(u'void ( * ) ( int8_t, int8_t ) *', u'ns3::TracedValueCallback::Int8')
    typehandlers.add_type_alias(u'void ( * ) ( int8_t, int8_t ) **', u'ns3::TracedValueCallback::Int8*')
    typehandlers.add_type_alias(u'void ( * ) ( int8_t, int8_t ) *&', u'ns3::TracedValueCallback::Int8&')
    typehandlers.add_type_alias(u'void ( * ) ( uint16_t, uint16_t ) *', u'ns3::TracedValueCallback::Uint16')
    typehandlers.add_type_alias(u'void ( * ) ( uint16_t, uint16_t ) **', u'ns3::TracedValueCallback::Uint16*')
    typehandlers.add_type_alias(u'void ( * ) ( uint16_t, uint16_t ) *&', u'ns3::TracedValueCallback::Uint16&')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t ) *', u'ns3::TracedValueCallback::Uint32')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t ) **', u'ns3::TracedValueCallback::Uint32*')
    typehandlers.add_type_alias(u'void ( * ) ( uint32_t, uint32_t ) *&', u'ns3::TracedValueCallback::Uint32&')
    typehandlers.add_type_alias(u'void ( * ) ( int16_t, int16_t ) *', u'ns3::TracedValueCallback::Int16')
    typehandlers.add_type_alias(u'void ( * ) ( int16_t, int16_t ) **', u'ns3::TracedValueCallback::Int16*')
    typehandlers.add_type_alias(u'void ( * ) ( int16_t, int16_t ) *&', u'ns3::TracedValueCallback::Int16&')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time, ns3::Time ) *', u'ns3::TracedValueCallback::Time')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time, ns3::Time ) **', u'ns3::TracedValueCallback::Time*')
    typehandlers.add_type_alias(u'void ( * ) ( ns3::Time, ns3::Time ) *&', u'ns3::TracedValueCallback::Time&')

def register_types_ns3_internal(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    register_Ns3Address_methods(root_module, root_module['ns3::Address'])
    register_Ns3AttributeConstructionList_methods(root_module, root_module['ns3::AttributeConstructionList'])
    register_Ns3AttributeConstructionListItem_methods(root_module, root_module['ns3::AttributeConstructionList::Item'])
    register_Ns3Bar_methods(root_module, root_module['ns3::Bar'])
    register_Ns3BlockAckAgreement_methods(root_module, root_module['ns3::BlockAckAgreement'])
    register_Ns3BlockAckManager_methods(root_module, root_module['ns3::BlockAckManager'])
    register_Ns3Buffer_methods(root_module, root_module['ns3::Buffer'])
    register_Ns3BufferIterator_methods(root_module, root_module['ns3::Buffer::Iterator'])
    register_Ns3ByteTagIterator_methods(root_module, root_module['ns3::ByteTagIterator'])
    register_Ns3ByteTagIteratorItem_methods(root_module, root_module['ns3::ByteTagIterator::Item'])
    register_Ns3ByteTagList_methods(root_module, root_module['ns3::ByteTagList'])
    register_Ns3ByteTagListIterator_methods(root_module, root_module['ns3::ByteTagList::Iterator'])
    register_Ns3ByteTagListIteratorItem_methods(root_module, root_module['ns3::ByteTagList::Iterator::Item'])
    register_Ns3CallbackBase_methods(root_module, root_module['ns3::CallbackBase'])
    register_Ns3CommandLine_methods(root_module, root_module['ns3::CommandLine'])
    register_Ns3CriticalSection_methods(root_module, root_module['ns3::CriticalSection'])
    register_Ns3EventGarbageCollector_methods(root_module, root_module['ns3::EventGarbageCollector'])
    register_Ns3EventId_methods(root_module, root_module['ns3::EventId'])
    register_Ns3GlobalValue_methods(root_module, root_module['ns3::GlobalValue'])
    register_Ns3Hasher_methods(root_module, root_module['ns3::Hasher'])
    register_Ns3IntToType__0_methods(root_module, root_module['ns3::IntToType< 0 >'])
    register_Ns3IntToType__1_methods(root_module, root_module['ns3::IntToType< 1 >'])
    register_Ns3IntToType__2_methods(root_module, root_module['ns3::IntToType< 2 >'])
    register_Ns3IntToType__3_methods(root_module, root_module['ns3::IntToType< 3 >'])
    register_Ns3IntToType__4_methods(root_module, root_module['ns3::IntToType< 4 >'])
    register_Ns3IntToType__5_methods(root_module, root_module['ns3::IntToType< 5 >'])
    register_Ns3IntToType__6_methods(root_module, root_module['ns3::IntToType< 6 >'])
    register_Ns3Ipv4Address_methods(root_module, root_module['ns3::Ipv4Address'])
    register_Ns3Ipv4Mask_methods(root_module, root_module['ns3::Ipv4Mask'])
    register_Ns3Ipv6Address_methods(root_module, root_module['ns3::Ipv6Address'])
    register_Ns3Ipv6Prefix_methods(root_module, root_module['ns3::Ipv6Prefix'])
    register_Ns3LogComponent_methods(root_module, root_module['ns3::LogComponent'])
    register_Ns3Mac48Address_methods(root_module, root_module['ns3::Mac48Address'])
    register_Ns3Names_methods(root_module, root_module['ns3::Names'])
    register_Ns3NodeContainer_methods(root_module, root_module['ns3::NodeContainer'])
    register_Ns3NonCopyable_methods(root_module, root_module['ns3::NonCopyable'])
    register_Ns3ObjectBase_methods(root_module, root_module['ns3::ObjectBase'])
    register_Ns3ObjectDeleter_methods(root_module, root_module['ns3::ObjectDeleter'])
    register_Ns3ObjectFactory_methods(root_module, root_module['ns3::ObjectFactory'])
    register_Ns3OriginatorBlockAckAgreement_methods(root_module, root_module['ns3::OriginatorBlockAckAgreement'])
    register_Ns3PacketMetadata_methods(root_module, root_module['ns3::PacketMetadata'])
    register_Ns3PacketMetadataItem_methods(root_module, root_module['ns3::PacketMetadata::Item'])
    register_Ns3PacketMetadataItemIterator_methods(root_module, root_module['ns3::PacketMetadata::ItemIterator'])
    register_Ns3PacketTagIterator_methods(root_module, root_module['ns3::PacketTagIterator'])
    register_Ns3PacketTagIteratorItem_methods(root_module, root_module['ns3::PacketTagIterator::Item'])
    register_Ns3PacketTagList_methods(root_module, root_module['ns3::PacketTagList'])
    register_Ns3PacketTagListTagData_methods(root_module, root_module['ns3::PacketTagList::TagData'])
    register_Ns3ParameterLogger_methods(root_module, root_module['ns3::ParameterLogger'])
    register_Ns3PuActivity_methods(root_module, root_module['ns3::PuActivity'])
    register_Ns3RandomVariableStreamHelper_methods(root_module, root_module['ns3::RandomVariableStreamHelper'])
    register_Ns3RepositoryEntryRecv_methods(root_module, root_module['ns3::RepositoryEntryRecv'])
    register_Ns3RepositoryEntrySend_methods(root_module, root_module['ns3::RepositoryEntrySend'])
    register_Ns3RngSeedManager_methods(root_module, root_module['ns3::RngSeedManager'])
    register_Ns3RngStream_methods(root_module, root_module['ns3::RngStream'])
    register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, root_module['ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter >'])
    register_Ns3Simulator_methods(root_module, root_module['ns3::Simulator'])
    register_Ns3SpectrumEntry_methods(root_module, root_module['ns3::SpectrumEntry'])
    register_Ns3SpectrumManager_methods(root_module, root_module['ns3::SpectrumManager'])
    register_Ns3SpectrumSensing_methods(root_module, root_module['ns3::SpectrumSensing'])
    register_Ns3SystemCondition_methods(root_module, root_module['ns3::SystemCondition'])
    register_Ns3SystemMutex_methods(root_module, root_module['ns3::SystemMutex'])
    register_Ns3SystemWallClockMs_methods(root_module, root_module['ns3::SystemWallClockMs'])
    register_Ns3Tag_methods(root_module, root_module['ns3::Tag'])
    register_Ns3TagBuffer_methods(root_module, root_module['ns3::TagBuffer'])
    register_Ns3TimeWithUnit_methods(root_module, root_module['ns3::TimeWithUnit'])
    register_Ns3Timer_methods(root_module, root_module['ns3::Timer'])
    register_Ns3TimerImpl_methods(root_module, root_module['ns3::TimerImpl'])
    register_Ns3TypeId_methods(root_module, root_module['ns3::TypeId'])
    register_Ns3TypeIdAttributeInformation_methods(root_module, root_module['ns3::TypeId::AttributeInformation'])
    register_Ns3TypeIdTraceSourceInformation_methods(root_module, root_module['ns3::TypeId::TraceSourceInformation'])
    register_Ns3Vector2D_methods(root_module, root_module['ns3::Vector2D'])
    register_Ns3Vector3D_methods(root_module, root_module['ns3::Vector3D'])
    register_Ns3Watchdog_methods(root_module, root_module['ns3::Watchdog'])
    register_Ns3WifiMode_methods(root_module, root_module['ns3::WifiMode'])
    register_Ns3WifiModeFactory_methods(root_module, root_module['ns3::WifiModeFactory'])
    register_Ns3WifiPhyListener_methods(root_module, root_module['ns3::WifiPhyListener'])
    register_Ns3WifiRemoteStation_methods(root_module, root_module['ns3::WifiRemoteStation'])
    register_Ns3WifiRemoteStationInfo_methods(root_module, root_module['ns3::WifiRemoteStationInfo'])
    register_Ns3WifiRemoteStationState_methods(root_module, root_module['ns3::WifiRemoteStationState'])
    register_Ns3WifiTxVector_methods(root_module, root_module['ns3::WifiTxVector'])
    register_Ns3Empty_methods(root_module, root_module['ns3::empty'])
    register_Ns3Int64x64_t_methods(root_module, root_module['ns3::int64x64_t'])
    register_Ns3MpduInfo_methods(root_module, root_module['ns3::mpduInfo'])
    register_Ns3SignalNoiseDbm_methods(root_module, root_module['ns3::signalNoiseDbm'])
    register_Ns3Chunk_methods(root_module, root_module['ns3::Chunk'])
    register_Ns3Header_methods(root_module, root_module['ns3::Header'])
    register_Ns3Object_methods(root_module, root_module['ns3::Object'])
    register_Ns3ObjectAggregateIterator_methods(root_module, root_module['ns3::Object::AggregateIterator'])
    register_Ns3PUModel_methods(root_module, root_module['ns3::PUModel'])
    register_Ns3PacketChannelPacketTag_methods(root_module, root_module['ns3::PacketChannelPacketTag'])
    register_Ns3PacketTypePacketTag_methods(root_module, root_module['ns3::PacketTypePacketTag'])
    register_Ns3RandomVariableStream_methods(root_module, root_module['ns3::RandomVariableStream'])
    register_Ns3Repository_methods(root_module, root_module['ns3::Repository'])
    register_Ns3Scheduler_methods(root_module, root_module['ns3::Scheduler'])
    register_Ns3SchedulerEvent_methods(root_module, root_module['ns3::Scheduler::Event'])
    register_Ns3SchedulerEventKey_methods(root_module, root_module['ns3::Scheduler::EventKey'])
    register_Ns3SequentialRandomVariable_methods(root_module, root_module['ns3::SequentialRandomVariable'])
    register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >'])
    register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >'])
    register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >'])
    register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >'])
    register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >'])
    register_Ns3SimpleRefCount__Ns3FdReader_Ns3Empty_Ns3DefaultDeleter__lt__ns3FdReader__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::FdReader, ns3::empty, ns3::DefaultDeleter<ns3::FdReader> >'])
    register_Ns3SimpleRefCount__Ns3HashImplementation_Ns3Empty_Ns3DefaultDeleter__lt__ns3HashImplementation__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >'])
    register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >'])
    register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >'])
    register_Ns3SimpleRefCount__Ns3RefCountBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3RefCountBase__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter<ns3::RefCountBase> >'])
    register_Ns3SimpleRefCount__Ns3SystemThread_Ns3Empty_Ns3DefaultDeleter__lt__ns3SystemThread__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::SystemThread, ns3::empty, ns3::DefaultDeleter<ns3::SystemThread> >'])
    register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >'])
    register_Ns3SimpleRefCount__Ns3WifiInformationElement_Ns3Empty_Ns3DefaultDeleter__lt__ns3WifiInformationElement__gt___methods(root_module, root_module['ns3::SimpleRefCount< ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter<ns3::WifiInformationElement> >'])
    register_Ns3SimulatorImpl_methods(root_module, root_module['ns3::SimulatorImpl'])
    register_Ns3SpectrumData_methods(root_module, root_module['ns3::SpectrumData'])
    register_Ns3SpectrumDecision_methods(root_module, root_module['ns3::SpectrumDecision'])
    register_Ns3Synchronizer_methods(root_module, root_module['ns3::Synchronizer'])
    register_Ns3SystemThread_methods(root_module, root_module['ns3::SystemThread'])
    register_Ns3Time_methods(root_module, root_module['ns3::Time'])
    register_Ns3TraceSourceAccessor_methods(root_module, root_module['ns3::TraceSourceAccessor'])
    register_Ns3Trailer_methods(root_module, root_module['ns3::Trailer'])
    register_Ns3TriangularRandomVariable_methods(root_module, root_module['ns3::TriangularRandomVariable'])
    register_Ns3UniformRandomVariable_methods(root_module, root_module['ns3::UniformRandomVariable'])
    register_Ns3WallClockSynchronizer_methods(root_module, root_module['ns3::WallClockSynchronizer'])
    register_Ns3WeibullRandomVariable_methods(root_module, root_module['ns3::WeibullRandomVariable'])
    register_Ns3WifiInformationElement_methods(root_module, root_module['ns3::WifiInformationElement'])
    register_Ns3WifiMac_methods(root_module, root_module['ns3::WifiMac'])
    register_Ns3WifiMacHeader_methods(root_module, root_module['ns3::WifiMacHeader'])
    register_Ns3WifiPhy_methods(root_module, root_module['ns3::WifiPhy'])
    register_Ns3WifiRemoteStationManager_methods(root_module, root_module['ns3::WifiRemoteStationManager'])
    register_Ns3ZetaRandomVariable_methods(root_module, root_module['ns3::ZetaRandomVariable'])
    register_Ns3ZipfRandomVariable_methods(root_module, root_module['ns3::ZipfRandomVariable'])
    register_Ns3AttributeAccessor_methods(root_module, root_module['ns3::AttributeAccessor'])
    register_Ns3AttributeChecker_methods(root_module, root_module['ns3::AttributeChecker'])
    register_Ns3AttributeValue_methods(root_module, root_module['ns3::AttributeValue'])
    register_Ns3BooleanChecker_methods(root_module, root_module['ns3::BooleanChecker'])
    register_Ns3BooleanValue_methods(root_module, root_module['ns3::BooleanValue'])
    register_Ns3CalendarScheduler_methods(root_module, root_module['ns3::CalendarScheduler'])
    register_Ns3CallbackChecker_methods(root_module, root_module['ns3::CallbackChecker'])
    register_Ns3CallbackImplBase_methods(root_module, root_module['ns3::CallbackImplBase'])
    register_Ns3CallbackValue_methods(root_module, root_module['ns3::CallbackValue'])
    register_Ns3ConstantRandomVariable_methods(root_module, root_module['ns3::ConstantRandomVariable'])
    register_Ns3CtrlBAckRequestHeader_methods(root_module, root_module['ns3::CtrlBAckRequestHeader'])
    register_Ns3CtrlBAckResponseHeader_methods(root_module, root_module['ns3::CtrlBAckResponseHeader'])
    register_Ns3Dcf_methods(root_module, root_module['ns3::Dcf'])
    register_Ns3DefaultSimulatorImpl_methods(root_module, root_module['ns3::DefaultSimulatorImpl'])
    register_Ns3DeterministicRandomVariable_methods(root_module, root_module['ns3::DeterministicRandomVariable'])
    register_Ns3DoubleValue_methods(root_module, root_module['ns3::DoubleValue'])
    register_Ns3EdcaTxopN_methods(root_module, root_module['ns3::EdcaTxopN'])
    register_Ns3EmpiricalRandomVariable_methods(root_module, root_module['ns3::EmpiricalRandomVariable'])
    register_Ns3EmptyAttributeValue_methods(root_module, root_module['ns3::EmptyAttributeValue'])
    register_Ns3EnumChecker_methods(root_module, root_module['ns3::EnumChecker'])
    register_Ns3EnumValue_methods(root_module, root_module['ns3::EnumValue'])
    register_Ns3ErlangRandomVariable_methods(root_module, root_module['ns3::ErlangRandomVariable'])
    register_Ns3EventImpl_methods(root_module, root_module['ns3::EventImpl'])
    register_Ns3ExponentialRandomVariable_methods(root_module, root_module['ns3::ExponentialRandomVariable'])
    register_Ns3FdReader_methods(root_module, root_module['ns3::FdReader'])
    register_Ns3GammaRandomVariable_methods(root_module, root_module['ns3::GammaRandomVariable'])
    register_Ns3HeapScheduler_methods(root_module, root_module['ns3::HeapScheduler'])
    register_Ns3HtCapabilities_methods(root_module, root_module['ns3::HtCapabilities'])
    register_Ns3HtCapabilitiesChecker_methods(root_module, root_module['ns3::HtCapabilitiesChecker'])
    register_Ns3HtCapabilitiesValue_methods(root_module, root_module['ns3::HtCapabilitiesValue'])
    register_Ns3IntegerValue_methods(root_module, root_module['ns3::IntegerValue'])
    register_Ns3Ipv4AddressChecker_methods(root_module, root_module['ns3::Ipv4AddressChecker'])
    register_Ns3Ipv4AddressValue_methods(root_module, root_module['ns3::Ipv4AddressValue'])
    register_Ns3Ipv4MaskChecker_methods(root_module, root_module['ns3::Ipv4MaskChecker'])
    register_Ns3Ipv4MaskValue_methods(root_module, root_module['ns3::Ipv4MaskValue'])
    register_Ns3Ipv6AddressChecker_methods(root_module, root_module['ns3::Ipv6AddressChecker'])
    register_Ns3Ipv6AddressValue_methods(root_module, root_module['ns3::Ipv6AddressValue'])
    register_Ns3Ipv6PrefixChecker_methods(root_module, root_module['ns3::Ipv6PrefixChecker'])
    register_Ns3Ipv6PrefixValue_methods(root_module, root_module['ns3::Ipv6PrefixValue'])
    register_Ns3ListScheduler_methods(root_module, root_module['ns3::ListScheduler'])
    register_Ns3LogNormalRandomVariable_methods(root_module, root_module['ns3::LogNormalRandomVariable'])
    register_Ns3Mac48AddressChecker_methods(root_module, root_module['ns3::Mac48AddressChecker'])
    register_Ns3Mac48AddressValue_methods(root_module, root_module['ns3::Mac48AddressValue'])
    register_Ns3MapScheduler_methods(root_module, root_module['ns3::MapScheduler'])
    register_Ns3NetDevice_methods(root_module, root_module['ns3::NetDevice'])
    register_Ns3NixVector_methods(root_module, root_module['ns3::NixVector'])
    register_Ns3Node_methods(root_module, root_module['ns3::Node'])
    register_Ns3NormalRandomVariable_methods(root_module, root_module['ns3::NormalRandomVariable'])
    register_Ns3ObjectFactoryChecker_methods(root_module, root_module['ns3::ObjectFactoryChecker'])
    register_Ns3ObjectFactoryValue_methods(root_module, root_module['ns3::ObjectFactoryValue'])
    register_Ns3ObjectPtrContainerAccessor_methods(root_module, root_module['ns3::ObjectPtrContainerAccessor'])
    register_Ns3ObjectPtrContainerChecker_methods(root_module, root_module['ns3::ObjectPtrContainerChecker'])
    register_Ns3ObjectPtrContainerValue_methods(root_module, root_module['ns3::ObjectPtrContainerValue'])
    register_Ns3Packet_methods(root_module, root_module['ns3::Packet'])
    register_Ns3ParetoRandomVariable_methods(root_module, root_module['ns3::ParetoRandomVariable'])
    register_Ns3PointerChecker_methods(root_module, root_module['ns3::PointerChecker'])
    register_Ns3PointerValue_methods(root_module, root_module['ns3::PointerValue'])
    register_Ns3RealtimeSimulatorImpl_methods(root_module, root_module['ns3::RealtimeSimulatorImpl'])
    register_Ns3RefCountBase_methods(root_module, root_module['ns3::RefCountBase'])
    register_Ns3RegularWifiMac_methods(root_module, root_module['ns3::RegularWifiMac'])
    register_Ns3Ssid_methods(root_module, root_module['ns3::Ssid'])
    register_Ns3SsidChecker_methods(root_module, root_module['ns3::SsidChecker'])
    register_Ns3SsidValue_methods(root_module, root_module['ns3::SsidValue'])
    register_Ns3StringChecker_methods(root_module, root_module['ns3::StringChecker'])
    register_Ns3StringValue_methods(root_module, root_module['ns3::StringValue'])
    register_Ns3TimeValue_methods(root_module, root_module['ns3::TimeValue'])
    register_Ns3TypeIdChecker_methods(root_module, root_module['ns3::TypeIdChecker'])
    register_Ns3TypeIdValue_methods(root_module, root_module['ns3::TypeIdValue'])
    register_Ns3UintegerValue_methods(root_module, root_module['ns3::UintegerValue'])
    register_Ns3Vector2DChecker_methods(root_module, root_module['ns3::Vector2DChecker'])
    register_Ns3Vector2DValue_methods(root_module, root_module['ns3::Vector2DValue'])
    register_Ns3Vector3DChecker_methods(root_module, root_module['ns3::Vector3DChecker'])
    register_Ns3Vector3DValue_methods(root_module, root_module['ns3::Vector3DValue'])
    register_Ns3VhtCapabilities_methods(root_module, root_module['ns3::VhtCapabilities'])
    register_Ns3VhtCapabilitiesChecker_methods(root_module, root_module['ns3::VhtCapabilitiesChecker'])
    register_Ns3VhtCapabilitiesValue_methods(root_module, root_module['ns3::VhtCapabilitiesValue'])
    register_Ns3WifiModeChecker_methods(root_module, root_module['ns3::WifiModeChecker'])
    register_Ns3WifiModeValue_methods(root_module, root_module['ns3::WifiModeValue'])
    register_Ns3AddressChecker_methods(root_module, root_module['ns3::AddressChecker'])
    register_Ns3AddressValue_methods(root_module, root_module['ns3::AddressValue'])
    register_Ns3DcaTxop_methods(root_module, root_module['ns3::DcaTxop'])
    register_Ns3ConfigMatchContainer_methods(root_module, root_module['ns3::Config::MatchContainer'])
    register_Ns3HashImplementation_methods(root_module, root_module['ns3::Hash::Implementation'])
    register_Ns3HashFunctionFnv1a_methods(root_module, root_module['ns3::Hash::Function::Fnv1a'])
    register_Ns3HashFunctionHash32_methods(root_module, root_module['ns3::Hash::Function::Hash32'])
    register_Ns3HashFunctionHash64_methods(root_module, root_module['ns3::Hash::Function::Hash64'])
    register_Ns3HashFunctionMurmur3_methods(root_module, root_module['ns3::Hash::Function::Murmur3'])
    return

def register_Ns3Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_numeric_operator('+', root_module['ns3::Address'], root_module['ns3::Address'], param('int const', u'right'))
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## address.h (module 'network'): ns3::Address::Address() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::Address::Address(uint8_t type, uint8_t const * buffer, uint8_t len) [constructor]
    cls.add_constructor([param('uint8_t', 'type'), param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): ns3::Address::Address(ns3::Address const & address) [copy constructor]
    cls.add_constructor([param('ns3::Address const &', 'address')])
    ## address.h (module 'network'): bool ns3::Address::CheckCompatible(uint8_t type, uint8_t len) const [member function]
    cls.add_method('CheckCompatible', 
                   'bool', 
                   [param('uint8_t', 'type'), param('uint8_t', 'len')], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::CopyAllFrom(uint8_t const * buffer, uint8_t len) [member function]
    cls.add_method('CopyAllFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): uint32_t ns3::Address::CopyAllTo(uint8_t * buffer, uint8_t len) const [member function]
    cls.add_method('CopyAllTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint8_t', 'len')], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::CopyFrom(uint8_t const * buffer, uint8_t len) [member function]
    cls.add_method('CopyFrom', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint8_t', 'len')])
    ## address.h (module 'network'): uint32_t ns3::Address::CopyTo(uint8_t * buffer) const [member function]
    cls.add_method('CopyTo', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    ## address.h (module 'network'): void ns3::Address::Deserialize(ns3::TagBuffer buffer) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')])
    ## address.h (module 'network'): uint8_t ns3::Address::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): uint32_t ns3::Address::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): bool ns3::Address::IsInvalid() const [member function]
    cls.add_method('IsInvalid', 
                   'bool', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): bool ns3::Address::IsMatchingType(uint8_t type) const [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('uint8_t', 'type')], 
                   is_const=True)
    ## address.h (module 'network'): static uint8_t ns3::Address::Register() [member function]
    cls.add_method('Register', 
                   'uint8_t', 
                   [], 
                   is_static=True)
    ## address.h (module 'network'): void ns3::Address::Serialize(ns3::TagBuffer buffer) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'buffer')], 
                   is_const=True)
    return

def register_Ns3AttributeConstructionList_methods(root_module, cls):
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::AttributeConstructionList(ns3::AttributeConstructionList const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeConstructionList const &', 'arg0')])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::AttributeConstructionList() [constructor]
    cls.add_constructor([])
    ## attribute-construction-list.h (module 'core'): void ns3::AttributeConstructionList::Add(std::string name, ns3::Ptr<ns3::AttributeChecker const> checker, ns3::Ptr<ns3::AttributeValue> value) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker'), param('ns3::Ptr< ns3::AttributeValue >', 'value')])
    ## attribute-construction-list.h (module 'core'): std::_List_const_iterator<ns3::AttributeConstructionList::Item> ns3::AttributeConstructionList::Begin() const [member function]
    cls.add_method('Begin', 
                   'std::_List_const_iterator< ns3::AttributeConstructionList::Item >', 
                   [], 
                   is_const=True)
    ## attribute-construction-list.h (module 'core'): std::_List_const_iterator<ns3::AttributeConstructionList::Item> ns3::AttributeConstructionList::End() const [member function]
    cls.add_method('End', 
                   'std::_List_const_iterator< ns3::AttributeConstructionList::Item >', 
                   [], 
                   is_const=True)
    ## attribute-construction-list.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeConstructionList::Find(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('Find', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True)
    return

def register_Ns3AttributeConstructionListItem_methods(root_module, cls):
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::Item() [constructor]
    cls.add_constructor([])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::Item(ns3::AttributeConstructionList::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeConstructionList::Item const &', 'arg0')])
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::checker [variable]
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    ## attribute-construction-list.h (module 'core'): ns3::AttributeConstructionList::Item::value [variable]
    cls.add_instance_attribute('value', 'ns3::Ptr< ns3::AttributeValue >', is_const=False)
    return

def register_Ns3Bar_methods(root_module, cls):
    ## block-ack-manager.h (module 'wifi'): ns3::Bar::Bar(ns3::Bar const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Bar const &', 'arg0')])
    ## block-ack-manager.h (module 'wifi'): ns3::Bar::Bar() [constructor]
    cls.add_constructor([])
    ## block-ack-manager.h (module 'wifi'): ns3::Bar::Bar(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address recipient, uint8_t tid, bool immediate) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid'), param('bool', 'immediate')])
    ## block-ack-manager.h (module 'wifi'): ns3::Bar::bar [variable]
    cls.add_instance_attribute('bar', 'ns3::Ptr< ns3::Packet const >', is_const=False)
    ## block-ack-manager.h (module 'wifi'): ns3::Bar::immediate [variable]
    cls.add_instance_attribute('immediate', 'bool', is_const=False)
    ## block-ack-manager.h (module 'wifi'): ns3::Bar::recipient [variable]
    cls.add_instance_attribute('recipient', 'ns3::Mac48Address', is_const=False)
    ## block-ack-manager.h (module 'wifi'): ns3::Bar::tid [variable]
    cls.add_instance_attribute('tid', 'uint8_t', is_const=False)
    return

def register_Ns3BlockAckAgreement_methods(root_module, cls):
    ## block-ack-agreement.h (module 'wifi'): ns3::BlockAckAgreement::BlockAckAgreement(ns3::BlockAckAgreement const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BlockAckAgreement const &', 'arg0')])
    ## block-ack-agreement.h (module 'wifi'): ns3::BlockAckAgreement::BlockAckAgreement() [constructor]
    cls.add_constructor([])
    ## block-ack-agreement.h (module 'wifi'): ns3::BlockAckAgreement::BlockAckAgreement(ns3::Mac48Address peer, uint8_t tid) [constructor]
    cls.add_constructor([param('ns3::Mac48Address', 'peer'), param('uint8_t', 'tid')])
    ## block-ack-agreement.h (module 'wifi'): uint16_t ns3::BlockAckAgreement::GetBufferSize() const [member function]
    cls.add_method('GetBufferSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): ns3::Mac48Address ns3::BlockAckAgreement::GetPeer() const [member function]
    cls.add_method('GetPeer', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): uint16_t ns3::BlockAckAgreement::GetStartingSequence() const [member function]
    cls.add_method('GetStartingSequence', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): uint16_t ns3::BlockAckAgreement::GetStartingSequenceControl() const [member function]
    cls.add_method('GetStartingSequenceControl', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): uint8_t ns3::BlockAckAgreement::GetTid() const [member function]
    cls.add_method('GetTid', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): uint16_t ns3::BlockAckAgreement::GetTimeout() const [member function]
    cls.add_method('GetTimeout', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): uint16_t ns3::BlockAckAgreement::GetWinEnd() const [member function]
    cls.add_method('GetWinEnd', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): bool ns3::BlockAckAgreement::IsAmsduSupported() const [member function]
    cls.add_method('IsAmsduSupported', 
                   'bool', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): bool ns3::BlockAckAgreement::IsHtSupported() const [member function]
    cls.add_method('IsHtSupported', 
                   'bool', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): bool ns3::BlockAckAgreement::IsImmediateBlockAck() const [member function]
    cls.add_method('IsImmediateBlockAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetAmsduSupport(bool supported) [member function]
    cls.add_method('SetAmsduSupport', 
                   'void', 
                   [param('bool', 'supported')])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetBufferSize(uint16_t bufferSize) [member function]
    cls.add_method('SetBufferSize', 
                   'void', 
                   [param('uint16_t', 'bufferSize')])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetDelayedBlockAck() [member function]
    cls.add_method('SetDelayedBlockAck', 
                   'void', 
                   [])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetHtSupported(bool htSupported) [member function]
    cls.add_method('SetHtSupported', 
                   'void', 
                   [param('bool', 'htSupported')])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetImmediateBlockAck() [member function]
    cls.add_method('SetImmediateBlockAck', 
                   'void', 
                   [])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetStartingSequence(uint16_t seq) [member function]
    cls.add_method('SetStartingSequence', 
                   'void', 
                   [param('uint16_t', 'seq')])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetStartingSequenceControl(uint16_t seq) [member function]
    cls.add_method('SetStartingSequenceControl', 
                   'void', 
                   [param('uint16_t', 'seq')])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetTimeout(uint16_t timeout) [member function]
    cls.add_method('SetTimeout', 
                   'void', 
                   [param('uint16_t', 'timeout')])
    ## block-ack-agreement.h (module 'wifi'): void ns3::BlockAckAgreement::SetWinEnd(uint16_t seq) [member function]
    cls.add_method('SetWinEnd', 
                   'void', 
                   [param('uint16_t', 'seq')])
    return

def register_Ns3BlockAckManager_methods(root_module, cls):
    ## block-ack-manager.h (module 'wifi'): ns3::BlockAckManager::BlockAckManager() [constructor]
    cls.add_constructor([])
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::AlreadyExists(uint16_t currentSeq, ns3::Mac48Address recipient, uint8_t tid) [member function]
    cls.add_method('AlreadyExists', 
                   'bool', 
                   [param('uint16_t', 'currentSeq'), param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::CompleteAmpduExchange(ns3::Mac48Address recipient, uint8_t tid) [member function]
    cls.add_method('CompleteAmpduExchange', 
                   'void', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::CreateAgreement(ns3::MgtAddBaRequestHeader const * reqHdr, ns3::Mac48Address recipient) [member function]
    cls.add_method('CreateAgreement', 
                   'void', 
                   [param('ns3::MgtAddBaRequestHeader const *', 'reqHdr'), param('ns3::Mac48Address', 'recipient')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::DestroyAgreement(ns3::Mac48Address recipient, uint8_t tid) [member function]
    cls.add_method('DestroyAgreement', 
                   'void', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')])
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::ExistsAgreement(ns3::Mac48Address recipient, uint8_t tid) const [member function]
    cls.add_method('ExistsAgreement', 
                   'bool', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::ExistsAgreementInState(ns3::Mac48Address recipient, uint8_t tid, ns3::OriginatorBlockAckAgreement::State state) const [member function]
    cls.add_method('ExistsAgreementInState', 
                   'bool', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid'), param('ns3::OriginatorBlockAckAgreement::State', 'state')], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): uint32_t ns3::BlockAckManager::GetNBufferedPackets(ns3::Mac48Address recipient, uint8_t tid) const [member function]
    cls.add_method('GetNBufferedPackets', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): uint32_t ns3::BlockAckManager::GetNRetryNeededPackets(ns3::Mac48Address recipient, uint8_t tid) const [member function]
    cls.add_method('GetNRetryNeededPackets', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): ns3::Ptr<ns3::Packet const> ns3::BlockAckManager::GetNextPacket(ns3::WifiMacHeader & hdr) [member function]
    cls.add_method('GetNextPacket', 
                   'ns3::Ptr< ns3::Packet const >', 
                   [param('ns3::WifiMacHeader &', 'hdr')])
    ## block-ack-manager.h (module 'wifi'): uint32_t ns3::BlockAckManager::GetNextPacketSize() const [member function]
    cls.add_method('GetNextPacketSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): uint16_t ns3::BlockAckManager::GetSeqNumOfNextRetryPacket(ns3::Mac48Address recipient, uint8_t tid) const [member function]
    cls.add_method('GetSeqNumOfNextRetryPacket', 
                   'uint16_t', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::HasBar(ns3::Bar & bar) [member function]
    cls.add_method('HasBar', 
                   'bool', 
                   [param('ns3::Bar &', 'bar')])
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::HasOtherFragments(uint16_t sequenceNumber) const [member function]
    cls.add_method('HasOtherFragments', 
                   'bool', 
                   [param('uint16_t', 'sequenceNumber')], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::HasPackets() const [member function]
    cls.add_method('HasPackets', 
                   'bool', 
                   [], 
                   is_const=True)
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::NeedBarRetransmission(uint8_t tid, uint16_t seqNumber, ns3::Mac48Address recipient) [member function]
    cls.add_method('NeedBarRetransmission', 
                   'bool', 
                   [param('uint8_t', 'tid'), param('uint16_t', 'seqNumber'), param('ns3::Mac48Address', 'recipient')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::NotifyAgreementEstablished(ns3::Mac48Address recipient, uint8_t tid, uint16_t startingSeq) [member function]
    cls.add_method('NotifyAgreementEstablished', 
                   'void', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid'), param('uint16_t', 'startingSeq')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::NotifyAgreementUnsuccessful(ns3::Mac48Address recipient, uint8_t tid) [member function]
    cls.add_method('NotifyAgreementUnsuccessful', 
                   'void', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::NotifyGotBlockAck(ns3::CtrlBAckResponseHeader const * blockAck, ns3::Mac48Address recipient, ns3::WifiMode txMode) [member function]
    cls.add_method('NotifyGotBlockAck', 
                   'void', 
                   [param('ns3::CtrlBAckResponseHeader const *', 'blockAck'), param('ns3::Mac48Address', 'recipient'), param('ns3::WifiMode', 'txMode')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::NotifyMpduTransmission(ns3::Mac48Address recipient, uint8_t tid, uint16_t nextSeqNumber, ns3::WifiMacHeader::QosAckPolicy policy) [member function]
    cls.add_method('NotifyMpduTransmission', 
                   'void', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid'), param('uint16_t', 'nextSeqNumber'), param('ns3::WifiMacHeader::QosAckPolicy', 'policy')])
    ## block-ack-manager.h (module 'wifi'): ns3::Ptr<ns3::Packet const> ns3::BlockAckManager::PeekNextPacket(ns3::WifiMacHeader & hdr, ns3::Mac48Address recipient, uint8_t tid, ns3::Time * timestamp) [member function]
    cls.add_method('PeekNextPacket', 
                   'ns3::Ptr< ns3::Packet const >', 
                   [param('ns3::WifiMacHeader &', 'hdr'), param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid'), param('ns3::Time *', 'timestamp')])
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::RemovePacket(uint8_t tid, ns3::Mac48Address recipient, uint16_t seqnumber) [member function]
    cls.add_method('RemovePacket', 
                   'bool', 
                   [param('uint8_t', 'tid'), param('ns3::Mac48Address', 'recipient'), param('uint16_t', 'seqnumber')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetBlockAckInactivityCallback(ns3::Callback<void, ns3::Mac48Address, unsigned char, bool, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetBlockAckInactivityCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Mac48Address, unsigned char, bool, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetBlockAckThreshold(uint8_t nPackets) [member function]
    cls.add_method('SetBlockAckThreshold', 
                   'void', 
                   [param('uint8_t', 'nPackets')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetBlockAckType(ns3::BlockAckType bAckType) [member function]
    cls.add_method('SetBlockAckType', 
                   'void', 
                   [param('ns3::BlockAckType', 'bAckType')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetBlockDestinationCallback(ns3::Callback<void, ns3::Mac48Address, unsigned char, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetBlockDestinationCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Mac48Address, unsigned char, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetMaxPacketDelay(ns3::Time maxDelay) [member function]
    cls.add_method('SetMaxPacketDelay', 
                   'void', 
                   [param('ns3::Time', 'maxDelay')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetQueue(ns3::Ptr<ns3::WifiMacQueue> queue) [member function]
    cls.add_method('SetQueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiMacQueue >', 'queue')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetTxFailedCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxFailedCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetTxMiddle(ns3::MacTxMiddle * txMiddle) [member function]
    cls.add_method('SetTxMiddle', 
                   'void', 
                   [param('ns3::MacTxMiddle *', 'txMiddle')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetTxOkCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetUnblockDestinationCallback(ns3::Callback<void, ns3::Mac48Address, unsigned char, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetUnblockDestinationCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Mac48Address, unsigned char, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> manager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'manager')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::StorePacket(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const & hdr, ns3::Time tStamp) [member function]
    cls.add_method('StorePacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const &', 'hdr'), param('ns3::Time', 'tStamp')])
    ## block-ack-manager.h (module 'wifi'): bool ns3::BlockAckManager::SwitchToBlockAckIfNeeded(ns3::Mac48Address recipient, uint8_t tid, uint16_t startingSeq) [member function]
    cls.add_method('SwitchToBlockAckIfNeeded', 
                   'bool', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid'), param('uint16_t', 'startingSeq')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::TearDownBlockAck(ns3::Mac48Address recipient, uint8_t tid) [member function]
    cls.add_method('TearDownBlockAck', 
                   'void', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')])
    ## block-ack-manager.h (module 'wifi'): void ns3::BlockAckManager::UpdateAgreement(ns3::MgtAddBaResponseHeader const * respHdr, ns3::Mac48Address recipient) [member function]
    cls.add_method('UpdateAgreement', 
                   'void', 
                   [param('ns3::MgtAddBaResponseHeader const *', 'respHdr'), param('ns3::Mac48Address', 'recipient')])
    return

def register_Ns3Buffer_methods(root_module, cls):
    ## buffer.h (module 'network'): ns3::Buffer::Buffer() [constructor]
    cls.add_constructor([])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(uint32_t dataSize) [constructor]
    cls.add_constructor([param('uint32_t', 'dataSize')])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(uint32_t dataSize, bool initialize) [constructor]
    cls.add_constructor([param('uint32_t', 'dataSize'), param('bool', 'initialize')])
    ## buffer.h (module 'network'): ns3::Buffer::Buffer(ns3::Buffer const & o) [copy constructor]
    cls.add_constructor([param('ns3::Buffer const &', 'o')])
    ## buffer.h (module 'network'): void ns3::Buffer::AddAtEnd(uint32_t end) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::AddAtEnd(ns3::Buffer const & o) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Buffer const &', 'o')])
    ## buffer.h (module 'network'): void ns3::Buffer::AddAtStart(uint32_t start) [member function]
    cls.add_method('AddAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator ns3::Buffer::Begin() const [member function]
    cls.add_method('Begin', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::CopyData(std::ostream * os, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::CopyData(uint8_t * buffer, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    ## buffer.h (module 'network'): ns3::Buffer ns3::Buffer::CreateFragment(uint32_t start, uint32_t length) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::Buffer', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Deserialize(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator ns3::Buffer::End() const [member function]
    cls.add_method('End', 
                   'ns3::Buffer::Iterator', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): uint8_t const * ns3::Buffer::PeekData() const [member function]
    cls.add_method('PeekData', 
                   'uint8_t const *', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::RemoveAtEnd(uint32_t end) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::RemoveAtStart(uint32_t start) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3BufferIterator_methods(root_module, cls):
    ## buffer.h (module 'network'): ns3::Buffer::Iterator::Iterator(ns3::Buffer::Iterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Buffer::Iterator const &', 'arg0')])
    ## buffer.h (module 'network'): ns3::Buffer::Iterator::Iterator() [constructor]
    cls.add_constructor([])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::CalculateIpChecksum(uint16_t size) [member function]
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size')])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::CalculateIpChecksum(uint16_t size, uint32_t initialChecksum) [member function]
    cls.add_method('CalculateIpChecksum', 
                   'uint16_t', 
                   [param('uint16_t', 'size'), param('uint32_t', 'initialChecksum')])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::GetDistanceFrom(ns3::Buffer::Iterator const & o) const [member function]
    cls.add_method('GetDistanceFrom', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator const &', 'o')], 
                   is_const=True)
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): bool ns3::Buffer::Iterator::IsEnd() const [member function]
    cls.add_method('IsEnd', 
                   'bool', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): bool ns3::Buffer::Iterator::IsStart() const [member function]
    cls.add_method('IsStart', 
                   'bool', 
                   [], 
                   is_const=True)
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Next() [member function]
    cls.add_method('Next', 
                   'void', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Next(uint32_t delta) [member function]
    cls.add_method('Next', 
                   'void', 
                   [param('uint32_t', 'delta')])
    ## buffer.h (module 'network'): uint8_t ns3::Buffer::Iterator::PeekU8() [member function]
    cls.add_method('PeekU8', 
                   'uint8_t', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Prev() [member function]
    cls.add_method('Prev', 
                   'void', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Prev(uint32_t delta) [member function]
    cls.add_method('Prev', 
                   'void', 
                   [param('uint32_t', 'delta')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Read(uint8_t * buffer, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Read(ns3::Buffer::Iterator start, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadLsbtohU16() [member function]
    cls.add_method('ReadLsbtohU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadLsbtohU32() [member function]
    cls.add_method('ReadLsbtohU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadLsbtohU64() [member function]
    cls.add_method('ReadLsbtohU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadNtohU16() [member function]
    cls.add_method('ReadNtohU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadNtohU32() [member function]
    cls.add_method('ReadNtohU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadNtohU64() [member function]
    cls.add_method('ReadNtohU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint16_t ns3::Buffer::Iterator::ReadU16() [member function]
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    ## buffer.h (module 'network'): uint32_t ns3::Buffer::Iterator::ReadU32() [member function]
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    ## buffer.h (module 'network'): uint64_t ns3::Buffer::Iterator::ReadU64() [member function]
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    ## buffer.h (module 'network'): uint8_t ns3::Buffer::Iterator::ReadU8() [member function]
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Write(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::Write(ns3::Buffer::Iterator start, ns3::Buffer::Iterator end) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start'), param('ns3::Buffer::Iterator', 'end')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU16(uint16_t data) [member function]
    cls.add_method('WriteHtolsbU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU32(uint32_t data) [member function]
    cls.add_method('WriteHtolsbU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtolsbU64(uint64_t data) [member function]
    cls.add_method('WriteHtolsbU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU16(uint16_t data) [member function]
    cls.add_method('WriteHtonU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU32(uint32_t data) [member function]
    cls.add_method('WriteHtonU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteHtonU64(uint64_t data) [member function]
    cls.add_method('WriteHtonU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU16(uint16_t data) [member function]
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU32(uint32_t data) [member function]
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU64(uint64_t data) [member function]
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU8(uint8_t data) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data')])
    ## buffer.h (module 'network'): void ns3::Buffer::Iterator::WriteU8(uint8_t data, uint32_t len) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'data'), param('uint32_t', 'len')])
    return

def register_Ns3ByteTagIterator_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::ByteTagIterator::ByteTagIterator(ns3::ByteTagIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagIterator const &', 'arg0')])
    ## packet.h (module 'network'): bool ns3::ByteTagIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item ns3::ByteTagIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::ByteTagIterator::Item', 
                   [])
    return

def register_Ns3ByteTagIteratorItem_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::ByteTagIterator::Item::Item(ns3::ByteTagIterator::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagIterator::Item const &', 'arg0')])
    ## packet.h (module 'network'): uint32_t ns3::ByteTagIterator::Item::GetEnd() const [member function]
    cls.add_method('GetEnd', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::ByteTagIterator::Item::GetStart() const [member function]
    cls.add_method('GetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::ByteTagIterator::Item::GetTag(ns3::Tag & tag) const [member function]
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::TypeId ns3::ByteTagIterator::Item::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3ByteTagList_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::ByteTagList() [constructor]
    cls.add_constructor([])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::ByteTagList(ns3::ByteTagList const & o) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagList const &', 'o')])
    ## byte-tag-list.h (module 'network'): ns3::TagBuffer ns3::ByteTagList::Add(ns3::TypeId tid, uint32_t bufferSize, int32_t start, int32_t end) [member function]
    cls.add_method('Add', 
                   'ns3::TagBuffer', 
                   [param('ns3::TypeId', 'tid'), param('uint32_t', 'bufferSize'), param('int32_t', 'start'), param('int32_t', 'end')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::Add(ns3::ByteTagList const & o) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::ByteTagList const &', 'o')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::AddAtEnd(int32_t appendOffset) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('int32_t', 'appendOffset')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::AddAtStart(int32_t prependOffset) [member function]
    cls.add_method('AddAtStart', 
                   'void', 
                   [param('int32_t', 'prependOffset')])
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::Adjust(int32_t adjustment) [member function]
    cls.add_method('Adjust', 
                   'void', 
                   [param('int32_t', 'adjustment')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator ns3::ByteTagList::Begin(int32_t offsetStart, int32_t offsetEnd) const [member function]
    cls.add_method('Begin', 
                   'ns3::ByteTagList::Iterator', 
                   [param('int32_t', 'offsetStart'), param('int32_t', 'offsetEnd')], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): void ns3::ByteTagList::RemoveAll() [member function]
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    return

def register_Ns3ByteTagListIterator_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Iterator(ns3::ByteTagList::Iterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagList::Iterator const &', 'arg0')])
    ## byte-tag-list.h (module 'network'): uint32_t ns3::ByteTagList::Iterator::GetOffsetStart() const [member function]
    cls.add_method('GetOffsetStart', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): bool ns3::ByteTagList::Iterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item ns3::ByteTagList::Iterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::ByteTagList::Iterator::Item', 
                   [])
    return

def register_Ns3ByteTagListIteratorItem_methods(root_module, cls):
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::Item(ns3::ByteTagList::Iterator::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ByteTagList::Iterator::Item const &', 'arg0')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::Item(ns3::TagBuffer buf) [constructor]
    cls.add_constructor([param('ns3::TagBuffer', 'buf')])
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::buf [variable]
    cls.add_instance_attribute('buf', 'ns3::TagBuffer', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::end [variable]
    cls.add_instance_attribute('end', 'int32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::size [variable]
    cls.add_instance_attribute('size', 'uint32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::start [variable]
    cls.add_instance_attribute('start', 'int32_t', is_const=False)
    ## byte-tag-list.h (module 'network'): ns3::ByteTagList::Iterator::Item::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3CallbackBase_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase(ns3::CallbackBase const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackBase const &', 'arg0')])
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::Ptr<ns3::CallbackImplBase> ns3::CallbackBase::GetImpl() const [member function]
    cls.add_method('GetImpl', 
                   'ns3::Ptr< ns3::CallbackImplBase >', 
                   [], 
                   is_const=True)
    ## callback.h (module 'core'): ns3::CallbackBase::CallbackBase(ns3::Ptr<ns3::CallbackImplBase> impl) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::CallbackImplBase >', 'impl')], 
                        visibility='protected')
    return

def register_Ns3CommandLine_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## command-line.h (module 'core'): ns3::CommandLine::CommandLine() [constructor]
    cls.add_constructor([])
    ## command-line.h (module 'core'): ns3::CommandLine::CommandLine(ns3::CommandLine const & cmd) [copy constructor]
    cls.add_constructor([param('ns3::CommandLine const &', 'cmd')])
    ## command-line.h (module 'core'): void ns3::CommandLine::AddValue(std::string const & name, std::string const & help, ns3::Callback<bool, std::string, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('AddValue', 
                   'void', 
                   [param('std::string const &', 'name'), param('std::string const &', 'help'), param('ns3::Callback< bool, std::string, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## command-line.h (module 'core'): void ns3::CommandLine::AddValue(std::string const & name, std::string const & attributePath) [member function]
    cls.add_method('AddValue', 
                   'void', 
                   [param('std::string const &', 'name'), param('std::string const &', 'attributePath')])
    ## command-line.h (module 'core'): std::string ns3::CommandLine::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## command-line.h (module 'core'): void ns3::CommandLine::Parse(int argc, char * * argv) [member function]
    cls.add_method('Parse', 
                   'void', 
                   [param('int', 'argc'), param('char * *', 'argv')])
    ## command-line.h (module 'core'): void ns3::CommandLine::PrintHelp(std::ostream & os) const [member function]
    cls.add_method('PrintHelp', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## command-line.h (module 'core'): void ns3::CommandLine::Usage(std::string const usage) [member function]
    cls.add_method('Usage', 
                   'void', 
                   [param('std::string const', 'usage')])
    return

def register_Ns3CriticalSection_methods(root_module, cls):
    ## system-mutex.h (module 'core'): ns3::CriticalSection::CriticalSection(ns3::CriticalSection const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CriticalSection const &', 'arg0')])
    ## system-mutex.h (module 'core'): ns3::CriticalSection::CriticalSection(ns3::SystemMutex & mutex) [constructor]
    cls.add_constructor([param('ns3::SystemMutex &', 'mutex')])
    return

def register_Ns3EventGarbageCollector_methods(root_module, cls):
    ## event-garbage-collector.h (module 'core'): ns3::EventGarbageCollector::EventGarbageCollector(ns3::EventGarbageCollector const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EventGarbageCollector const &', 'arg0')])
    ## event-garbage-collector.h (module 'core'): ns3::EventGarbageCollector::EventGarbageCollector() [constructor]
    cls.add_constructor([])
    ## event-garbage-collector.h (module 'core'): void ns3::EventGarbageCollector::Track(ns3::EventId event) [member function]
    cls.add_method('Track', 
                   'void', 
                   [param('ns3::EventId', 'event')])
    return

def register_Ns3EventId_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('==')
    ## event-id.h (module 'core'): ns3::EventId::EventId(ns3::EventId const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EventId const &', 'arg0')])
    ## event-id.h (module 'core'): ns3::EventId::EventId() [constructor]
    cls.add_constructor([])
    ## event-id.h (module 'core'): ns3::EventId::EventId(ns3::Ptr<ns3::EventImpl> const & impl, uint64_t ts, uint32_t context, uint32_t uid) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::EventImpl > const &', 'impl'), param('uint64_t', 'ts'), param('uint32_t', 'context'), param('uint32_t', 'uid')])
    ## event-id.h (module 'core'): void ns3::EventId::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## event-id.h (module 'core'): uint32_t ns3::EventId::GetContext() const [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): uint64_t ns3::EventId::GetTs() const [member function]
    cls.add_method('GetTs', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): uint32_t ns3::EventId::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): bool ns3::EventId::IsExpired() const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): bool ns3::EventId::IsRunning() const [member function]
    cls.add_method('IsRunning', 
                   'bool', 
                   [], 
                   is_const=True)
    ## event-id.h (module 'core'): ns3::EventImpl * ns3::EventId::PeekEventImpl() const [member function]
    cls.add_method('PeekEventImpl', 
                   'ns3::EventImpl *', 
                   [], 
                   is_const=True)
    return

def register_Ns3GlobalValue_methods(root_module, cls):
    ## global-value.h (module 'core'): ns3::GlobalValue::GlobalValue(ns3::GlobalValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::GlobalValue const &', 'arg0')])
    ## global-value.h (module 'core'): ns3::GlobalValue::GlobalValue(std::string name, std::string help, ns3::AttributeValue const & initialValue, ns3::Ptr<ns3::AttributeChecker const> checker) [constructor]
    cls.add_constructor([param('std::string', 'name'), param('std::string', 'help'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')])
    ## global-value.h (module 'core'): static __gnu_cxx::__normal_iterator<ns3::GlobalValue* const*,std::vector<ns3::GlobalValue*, std::allocator<ns3::GlobalValue*> > > ns3::GlobalValue::Begin() [member function]
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::GlobalValue * const *, std::vector< ns3::GlobalValue * > >', 
                   [], 
                   is_static=True)
    ## global-value.h (module 'core'): static void ns3::GlobalValue::Bind(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('Bind', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')], 
                   is_static=True)
    ## global-value.h (module 'core'): static bool ns3::GlobalValue::BindFailSafe(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('BindFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')], 
                   is_static=True)
    ## global-value.h (module 'core'): static __gnu_cxx::__normal_iterator<ns3::GlobalValue* const*,std::vector<ns3::GlobalValue*, std::allocator<ns3::GlobalValue*> > > ns3::GlobalValue::End() [member function]
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::GlobalValue * const *, std::vector< ns3::GlobalValue * > >', 
                   [], 
                   is_static=True)
    ## global-value.h (module 'core'): ns3::Ptr<ns3::AttributeChecker const> ns3::GlobalValue::GetChecker() const [member function]
    cls.add_method('GetChecker', 
                   'ns3::Ptr< ns3::AttributeChecker const >', 
                   [], 
                   is_const=True)
    ## global-value.h (module 'core'): std::string ns3::GlobalValue::GetHelp() const [member function]
    cls.add_method('GetHelp', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## global-value.h (module 'core'): std::string ns3::GlobalValue::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## global-value.h (module 'core'): void ns3::GlobalValue::GetValue(ns3::AttributeValue & value) const [member function]
    cls.add_method('GetValue', 
                   'void', 
                   [param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    ## global-value.h (module 'core'): static void ns3::GlobalValue::GetValueByName(std::string name, ns3::AttributeValue & value) [member function]
    cls.add_method('GetValueByName', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_static=True)
    ## global-value.h (module 'core'): static bool ns3::GlobalValue::GetValueByNameFailSafe(std::string name, ns3::AttributeValue & value) [member function]
    cls.add_method('GetValueByNameFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_static=True)
    ## global-value.h (module 'core'): void ns3::GlobalValue::ResetInitialValue() [member function]
    cls.add_method('ResetInitialValue', 
                   'void', 
                   [])
    ## global-value.h (module 'core'): bool ns3::GlobalValue::SetValue(ns3::AttributeValue const & value) [member function]
    cls.add_method('SetValue', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')])
    return

def register_Ns3Hasher_methods(root_module, cls):
    ## hash.h (module 'core'): ns3::Hasher::Hasher(ns3::Hasher const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hasher const &', 'arg0')])
    ## hash.h (module 'core'): ns3::Hasher::Hasher() [constructor]
    cls.add_constructor([])
    ## hash.h (module 'core'): ns3::Hasher::Hasher(ns3::Ptr<ns3::Hash::Implementation> hp) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Hash::Implementation >', 'hp')])
    ## hash.h (module 'core'): uint32_t ns3::Hasher::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')])
    ## hash.h (module 'core'): uint32_t ns3::Hasher::GetHash32(std::string const s) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('std::string const', 's')])
    ## hash.h (module 'core'): uint64_t ns3::Hasher::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')])
    ## hash.h (module 'core'): uint64_t ns3::Hasher::GetHash64(std::string const s) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('std::string const', 's')])
    ## hash.h (module 'core'): ns3::Hasher & ns3::Hasher::clear() [member function]
    cls.add_method('clear', 
                   'ns3::Hasher &', 
                   [])
    return

def register_Ns3IntToType__0_methods(root_module, cls):
    ## int-to-type.h (module 'core'): ns3::IntToType<0>::IntToType() [constructor]
    cls.add_constructor([])
    ## int-to-type.h (module 'core'): ns3::IntToType<0>::IntToType(ns3::IntToType<0> const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntToType< 0 > const &', 'arg0')])
    return

def register_Ns3IntToType__1_methods(root_module, cls):
    ## int-to-type.h (module 'core'): ns3::IntToType<1>::IntToType() [constructor]
    cls.add_constructor([])
    ## int-to-type.h (module 'core'): ns3::IntToType<1>::IntToType(ns3::IntToType<1> const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntToType< 1 > const &', 'arg0')])
    return

def register_Ns3IntToType__2_methods(root_module, cls):
    ## int-to-type.h (module 'core'): ns3::IntToType<2>::IntToType() [constructor]
    cls.add_constructor([])
    ## int-to-type.h (module 'core'): ns3::IntToType<2>::IntToType(ns3::IntToType<2> const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntToType< 2 > const &', 'arg0')])
    return

def register_Ns3IntToType__3_methods(root_module, cls):
    ## int-to-type.h (module 'core'): ns3::IntToType<3>::IntToType() [constructor]
    cls.add_constructor([])
    ## int-to-type.h (module 'core'): ns3::IntToType<3>::IntToType(ns3::IntToType<3> const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntToType< 3 > const &', 'arg0')])
    return

def register_Ns3IntToType__4_methods(root_module, cls):
    ## int-to-type.h (module 'core'): ns3::IntToType<4>::IntToType() [constructor]
    cls.add_constructor([])
    ## int-to-type.h (module 'core'): ns3::IntToType<4>::IntToType(ns3::IntToType<4> const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntToType< 4 > const &', 'arg0')])
    return

def register_Ns3IntToType__5_methods(root_module, cls):
    ## int-to-type.h (module 'core'): ns3::IntToType<5>::IntToType() [constructor]
    cls.add_constructor([])
    ## int-to-type.h (module 'core'): ns3::IntToType<5>::IntToType(ns3::IntToType<5> const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntToType< 5 > const &', 'arg0')])
    return

def register_Ns3IntToType__6_methods(root_module, cls):
    ## int-to-type.h (module 'core'): ns3::IntToType<6>::IntToType() [constructor]
    cls.add_constructor([])
    ## int-to-type.h (module 'core'): ns3::IntToType<6>::IntToType(ns3::IntToType<6> const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntToType< 6 > const &', 'arg0')])
    return

def register_Ns3Ipv4Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(ns3::Ipv4Address const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4Address const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(uint32_t address) [constructor]
    cls.add_constructor([param('uint32_t', 'address')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address::Ipv4Address(char const * address) [constructor]
    cls.add_constructor([param('char const *', 'address')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4Address::CombineMask(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('CombineMask', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::Deserialize(uint8_t const * buf) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Ipv4Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Address::Get() const [member function]
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetAny() [member function]
    cls.add_method('GetAny', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4Address::GetSubnetDirectedBroadcast(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('GetSubnetDirectedBroadcast', 
                   'ns3::Ipv4Address', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Address ns3::Ipv4Address::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsEqual(ns3::Ipv4Address const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Address const &', 'other')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsLocalMulticast() const [member function]
    cls.add_method('IsLocalMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static bool ns3::Ipv4Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Address::IsSubnetDirectedBroadcast(ns3::Ipv4Mask const & mask) const [member function]
    cls.add_method('IsSubnetDirectedBroadcast', 
                   'bool', 
                   [param('ns3::Ipv4Mask const &', 'mask')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Serialize(uint8_t * buf) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Set(uint32_t address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'address')])
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Address::Set(char const * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    return

def register_Ns3Ipv4Mask_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(ns3::Ipv4Mask const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(uint32_t mask) [constructor]
    cls.add_constructor([param('uint32_t', 'mask')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask::Ipv4Mask(char const * mask) [constructor]
    cls.add_constructor([param('char const *', 'mask')])
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Mask::Get() const [member function]
    cls.add_method('Get', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): uint32_t ns3::Ipv4Mask::GetInverse() const [member function]
    cls.add_method('GetInverse', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): uint16_t ns3::Ipv4Mask::GetPrefixLength() const [member function]
    cls.add_method('GetPrefixLength', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): static ns3::Ipv4Mask ns3::Ipv4Mask::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_static=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Mask::IsEqual(ns3::Ipv4Mask other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv4Mask', 'other')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4Mask::IsMatch(ns3::Ipv4Address a, ns3::Ipv4Address b) const [member function]
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv4Address', 'a'), param('ns3::Ipv4Address', 'b')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Mask::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4Mask::Set(uint32_t mask) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint32_t', 'mask')])
    return

def register_Ns3Ipv6Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(char const * address) [constructor]
    cls.add_constructor([param('char const *', 'address')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(uint8_t * address) [constructor]
    cls.add_constructor([param('uint8_t *', 'address')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(ns3::Ipv6Address const & addr) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6Address const &', 'addr')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address::Ipv6Address(ns3::Ipv6Address const * addr) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address const *', 'addr')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address ns3::Ipv6Address::CombinePrefix(ns3::Ipv6Prefix const & prefix) [member function]
    cls.add_method('CombinePrefix', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Prefix const &', 'prefix')])
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::Deserialize(uint8_t const * buf) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Ipv6Address', 
                   [param('uint8_t const *', 'buf')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllHostsMulticast() [member function]
    cls.add_method('GetAllHostsMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllNodesMulticast() [member function]
    cls.add_method('GetAllNodesMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAllRoutersMulticast() [member function]
    cls.add_method('GetAllRoutersMulticast', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetAny() [member function]
    cls.add_method('GetAny', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::GetBytes(uint8_t * buf) const [member function]
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv6Address::GetIpv4MappedAddress() const [member function]
    cls.add_method('GetIpv4MappedAddress', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllHostsMulticast() const [member function]
    cls.add_method('IsAllHostsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllNodesMulticast() const [member function]
    cls.add_method('IsAllNodesMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAllRoutersMulticast() const [member function]
    cls.add_method('IsAllRoutersMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsAny() const [member function]
    cls.add_method('IsAny', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsDocumentation() const [member function]
    cls.add_method('IsDocumentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsEqual(ns3::Ipv6Address const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Address const &', 'other')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsIpv4MappedAddress() const [member function]
    cls.add_method('IsIpv4MappedAddress', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLinkLocal() const [member function]
    cls.add_method('IsLinkLocal', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLinkLocalMulticast() const [member function]
    cls.add_method('IsLinkLocalMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsLocalhost() const [member function]
    cls.add_method('IsLocalhost', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static bool ns3::Ipv6Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Address::IsSolicitedMulticast() const [member function]
    cls.add_method('IsSolicitedMulticast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac16Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac16Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac48Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredAddress(ns3::Mac64Address addr, ns3::Ipv6Address prefix) [member function]
    cls.add_method('MakeAutoconfiguredAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac64Address', 'addr'), param('ns3::Ipv6Address', 'prefix')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac16Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac16Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac48Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac48Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeAutoconfiguredLinkLocalAddress(ns3::Mac64Address mac) [member function]
    cls.add_method('MakeAutoconfiguredLinkLocalAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Mac64Address', 'mac')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeIpv4MappedAddress(ns3::Ipv4Address addr) [member function]
    cls.add_method('MakeIpv4MappedAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv4Address', 'addr')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Address ns3::Ipv6Address::MakeSolicitedAddress(ns3::Ipv6Address addr) [member function]
    cls.add_method('MakeSolicitedAddress', 
                   'ns3::Ipv6Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Serialize(uint8_t * buf) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Set(char const * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('char const *', 'address')])
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Address::Set(uint8_t * address) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint8_t *', 'address')])
    return

def register_Ns3Ipv6Prefix_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(uint8_t * prefix) [constructor]
    cls.add_constructor([param('uint8_t *', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(char const * prefix) [constructor]
    cls.add_constructor([param('char const *', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(uint8_t prefix) [constructor]
    cls.add_constructor([param('uint8_t', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(ns3::Ipv6Prefix const & prefix) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'prefix')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix::Ipv6Prefix(ns3::Ipv6Prefix const * prefix) [constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const *', 'prefix')])
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Prefix::GetBytes(uint8_t * buf) const [member function]
    cls.add_method('GetBytes', 
                   'void', 
                   [param('uint8_t *', 'buf')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetLoopback() [member function]
    cls.add_method('GetLoopback', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetOnes() [member function]
    cls.add_method('GetOnes', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): uint8_t ns3::Ipv6Prefix::GetPrefixLength() const [member function]
    cls.add_method('GetPrefixLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): static ns3::Ipv6Prefix ns3::Ipv6Prefix::GetZero() [member function]
    cls.add_method('GetZero', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_static=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Prefix::IsEqual(ns3::Ipv6Prefix const & other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ipv6Prefix const &', 'other')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6Prefix::IsMatch(ns3::Ipv6Address a, ns3::Ipv6Address b) const [member function]
    cls.add_method('IsMatch', 
                   'bool', 
                   [param('ns3::Ipv6Address', 'a'), param('ns3::Ipv6Address', 'b')], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6Prefix::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    return

def register_Ns3LogComponent_methods(root_module, cls):
    ## log.h (module 'core'): ns3::LogComponent::LogComponent(ns3::LogComponent const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::LogComponent const &', 'arg0')])
    ## log.h (module 'core'): ns3::LogComponent::LogComponent(std::string const & name, std::string const & file, ns3::LogLevel const mask=::ns3::LOG_NONE) [constructor]
    cls.add_constructor([param('std::string const &', 'name'), param('std::string const &', 'file'), param('ns3::LogLevel const', 'mask', default_value='::ns3::LOG_NONE')])
    ## log.h (module 'core'): void ns3::LogComponent::Disable(ns3::LogLevel const level) [member function]
    cls.add_method('Disable', 
                   'void', 
                   [param('ns3::LogLevel const', 'level')])
    ## log.h (module 'core'): void ns3::LogComponent::Enable(ns3::LogLevel const level) [member function]
    cls.add_method('Enable', 
                   'void', 
                   [param('ns3::LogLevel const', 'level')])
    ## log.h (module 'core'): std::string ns3::LogComponent::File() const [member function]
    cls.add_method('File', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## log.h (module 'core'): static std::map<std::basic_string<char, std::char_traits<char>, std::allocator<char> >,ns3::LogComponent*,std::less<std::basic_string<char, std::char_traits<char>, std::allocator<char> > >,std::allocator<std::pair<const std::basic_string<char, std::char_traits<char>, std::allocator<char> >, ns3::LogComponent*> > > * ns3::LogComponent::GetComponentList() [member function]
    cls.add_method('GetComponentList', 
                   'std::map< std::string, ns3::LogComponent * > *', 
                   [], 
                   is_static=True)
    ## log.h (module 'core'): static std::string ns3::LogComponent::GetLevelLabel(ns3::LogLevel const level) [member function]
    cls.add_method('GetLevelLabel', 
                   'std::string', 
                   [param('ns3::LogLevel const', 'level')], 
                   is_static=True)
    ## log.h (module 'core'): bool ns3::LogComponent::IsEnabled(ns3::LogLevel const level) const [member function]
    cls.add_method('IsEnabled', 
                   'bool', 
                   [param('ns3::LogLevel const', 'level')], 
                   is_const=True)
    ## log.h (module 'core'): bool ns3::LogComponent::IsNoneEnabled() const [member function]
    cls.add_method('IsNoneEnabled', 
                   'bool', 
                   [], 
                   is_const=True)
    ## log.h (module 'core'): char const * ns3::LogComponent::Name() const [member function]
    cls.add_method('Name', 
                   'char const *', 
                   [], 
                   is_const=True)
    ## log.h (module 'core'): void ns3::LogComponent::SetMask(ns3::LogLevel const level) [member function]
    cls.add_method('SetMask', 
                   'void', 
                   [param('ns3::LogLevel const', 'level')])
    return

def register_Ns3Mac48Address_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address(ns3::Mac48Address const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Mac48Address const &', 'arg0')])
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48Address::Mac48Address(char const * str) [constructor]
    cls.add_constructor([param('char const *', 'str')])
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::Allocate() [member function]
    cls.add_method('Allocate', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::ConvertFrom(ns3::Address const & address) [member function]
    cls.add_method('ConvertFrom', 
                   'ns3::Mac48Address', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): void ns3::Mac48Address::CopyFrom(uint8_t const * buffer) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('uint8_t const *', 'buffer')])
    ## mac48-address.h (module 'network'): void ns3::Mac48Address::CopyTo(uint8_t * buffer) const [member function]
    cls.add_method('CopyTo', 
                   'void', 
                   [param('uint8_t *', 'buffer')], 
                   is_const=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetBroadcast() [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast(ns3::Ipv4Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv4Address', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast(ns3::Ipv6Address address) [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Mac48Address', 
                   [param('ns3::Ipv6Address', 'address')], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticast6Prefix() [member function]
    cls.add_method('GetMulticast6Prefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): static ns3::Mac48Address ns3::Mac48Address::GetMulticastPrefix() [member function]
    cls.add_method('GetMulticastPrefix', 
                   'ns3::Mac48Address', 
                   [], 
                   is_static=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48Address::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48Address::IsGroup() const [member function]
    cls.add_method('IsGroup', 
                   'bool', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): static bool ns3::Mac48Address::IsMatchingType(ns3::Address const & address) [member function]
    cls.add_method('IsMatchingType', 
                   'bool', 
                   [param('ns3::Address const &', 'address')], 
                   is_static=True)
    return

def register_Ns3Names_methods(root_module, cls):
    ## names.h (module 'core'): ns3::Names::Names() [constructor]
    cls.add_constructor([])
    ## names.h (module 'core'): ns3::Names::Names(ns3::Names const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Names const &', 'arg0')])
    ## names.h (module 'core'): static void ns3::Names::Add(std::string name, ns3::Ptr<ns3::Object> object) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::Ptr< ns3::Object >', 'object')], 
                   is_static=True)
    ## names.h (module 'core'): static void ns3::Names::Add(std::string path, std::string name, ns3::Ptr<ns3::Object> object) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'path'), param('std::string', 'name'), param('ns3::Ptr< ns3::Object >', 'object')], 
                   is_static=True)
    ## names.h (module 'core'): static void ns3::Names::Add(ns3::Ptr<ns3::Object> context, std::string name, ns3::Ptr<ns3::Object> object) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'context'), param('std::string', 'name'), param('ns3::Ptr< ns3::Object >', 'object')], 
                   is_static=True)
    ## names.h (module 'core'): static void ns3::Names::Clear() [member function]
    cls.add_method('Clear', 
                   'void', 
                   [], 
                   is_static=True)
    ## names.h (module 'core'): static std::string ns3::Names::FindName(ns3::Ptr<ns3::Object> object) [member function]
    cls.add_method('FindName', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::Object >', 'object')], 
                   is_static=True)
    ## names.h (module 'core'): static std::string ns3::Names::FindPath(ns3::Ptr<ns3::Object> object) [member function]
    cls.add_method('FindPath', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::Object >', 'object')], 
                   is_static=True)
    ## names.h (module 'core'): static void ns3::Names::Rename(std::string oldpath, std::string newname) [member function]
    cls.add_method('Rename', 
                   'void', 
                   [param('std::string', 'oldpath'), param('std::string', 'newname')], 
                   is_static=True)
    ## names.h (module 'core'): static void ns3::Names::Rename(std::string path, std::string oldname, std::string newname) [member function]
    cls.add_method('Rename', 
                   'void', 
                   [param('std::string', 'path'), param('std::string', 'oldname'), param('std::string', 'newname')], 
                   is_static=True)
    ## names.h (module 'core'): static void ns3::Names::Rename(ns3::Ptr<ns3::Object> context, std::string oldname, std::string newname) [member function]
    cls.add_method('Rename', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'context'), param('std::string', 'oldname'), param('std::string', 'newname')], 
                   is_static=True)
    return

def register_Ns3NodeContainer_methods(root_module, cls):
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'arg0')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer() [constructor]
    cls.add_constructor([])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::Ptr<ns3::Node> node) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Node >', 'node')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(std::string nodeName) [constructor]
    cls.add_constructor([param('std::string', 'nodeName')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c, ns3::NodeContainer const & d) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd')])
    ## node-container.h (module 'network'): ns3::NodeContainer::NodeContainer(ns3::NodeContainer const & a, ns3::NodeContainer const & b, ns3::NodeContainer const & c, ns3::NodeContainer const & d, ns3::NodeContainer const & e) [constructor]
    cls.add_constructor([param('ns3::NodeContainer const &', 'a'), param('ns3::NodeContainer const &', 'b'), param('ns3::NodeContainer const &', 'c'), param('ns3::NodeContainer const &', 'd'), param('ns3::NodeContainer const &', 'e')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(ns3::NodeContainer other) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::NodeContainer', 'other')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Add(std::string nodeName) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('std::string', 'nodeName')])
    ## node-container.h (module 'network'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Node>*,std::vector<ns3::Ptr<ns3::Node>, std::allocator<ns3::Ptr<ns3::Node> > > > ns3::NodeContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_const=True)
    ## node-container.h (module 'network'): void ns3::NodeContainer::Create(uint32_t n) [member function]
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n')])
    ## node-container.h (module 'network'): void ns3::NodeContainer::Create(uint32_t n, uint32_t systemId) [member function]
    cls.add_method('Create', 
                   'void', 
                   [param('uint32_t', 'n'), param('uint32_t', 'systemId')])
    ## node-container.h (module 'network'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Node>*,std::vector<ns3::Ptr<ns3::Node>, std::allocator<ns3::Ptr<ns3::Node> > > > ns3::NodeContainer::End() const [member function]
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Node > const, std::vector< ns3::Ptr< ns3::Node > > >', 
                   [], 
                   is_const=True)
    ## node-container.h (module 'network'): ns3::Ptr<ns3::Node> ns3::NodeContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Node >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## node-container.h (module 'network'): static ns3::NodeContainer ns3::NodeContainer::GetGlobal() [member function]
    cls.add_method('GetGlobal', 
                   'ns3::NodeContainer', 
                   [], 
                   is_static=True)
    ## node-container.h (module 'network'): uint32_t ns3::NodeContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    return

def register_Ns3NonCopyable_methods(root_module, cls):
    ## non-copyable.h (module 'core'): ns3::NonCopyable::NonCopyable() [constructor]
    cls.add_constructor([], 
                        visibility='protected')
    return

def register_Ns3ObjectBase_methods(root_module, cls):
    ## object-base.h (module 'core'): ns3::ObjectBase::ObjectBase() [constructor]
    cls.add_constructor([])
    ## object-base.h (module 'core'): ns3::ObjectBase::ObjectBase(ns3::ObjectBase const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectBase const &', 'arg0')])
    ## object-base.h (module 'core'): void ns3::ObjectBase::GetAttribute(std::string name, ns3::AttributeValue & value) const [member function]
    cls.add_method('GetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    ## object-base.h (module 'core'): bool ns3::ObjectBase::GetAttributeFailSafe(std::string name, ns3::AttributeValue & value) const [member function]
    cls.add_method('GetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True)
    ## object-base.h (module 'core'): ns3::TypeId ns3::ObjectBase::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## object-base.h (module 'core'): static ns3::TypeId ns3::ObjectBase::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## object-base.h (module 'core'): void ns3::ObjectBase::SetAttribute(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('SetAttribute', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::SetAttributeFailSafe(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('SetAttributeFailSafe', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceConnect(std::string name, std::string context, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceConnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceConnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceConnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceDisconnect(std::string name, std::string context, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceDisconnect', 
                   'bool', 
                   [param('std::string', 'name'), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): bool ns3::ObjectBase::TraceDisconnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('TraceDisconnectWithoutContext', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## object-base.h (module 'core'): void ns3::ObjectBase::ConstructSelf(ns3::AttributeConstructionList const & attributes) [member function]
    cls.add_method('ConstructSelf', 
                   'void', 
                   [param('ns3::AttributeConstructionList const &', 'attributes')], 
                   visibility='protected')
    ## object-base.h (module 'core'): void ns3::ObjectBase::NotifyConstructionCompleted() [member function]
    cls.add_method('NotifyConstructionCompleted', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectDeleter_methods(root_module, cls):
    ## object.h (module 'core'): ns3::ObjectDeleter::ObjectDeleter() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): ns3::ObjectDeleter::ObjectDeleter(ns3::ObjectDeleter const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectDeleter const &', 'arg0')])
    ## object.h (module 'core'): static void ns3::ObjectDeleter::Delete(ns3::Object * object) [member function]
    cls.add_method('Delete', 
                   'void', 
                   [param('ns3::Object *', 'object')], 
                   is_static=True)
    return

def register_Ns3ObjectFactory_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory(ns3::ObjectFactory const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectFactory const &', 'arg0')])
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactory::ObjectFactory(std::string typeId) [constructor]
    cls.add_constructor([param('std::string', 'typeId')])
    ## object-factory.h (module 'core'): ns3::Ptr<ns3::Object> ns3::ObjectFactory::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::Object >', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): ns3::TypeId ns3::ObjectFactory::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::Set(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(ns3::TypeId tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('ns3::TypeId', 'tid')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(char const * tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('char const *', 'tid')])
    ## object-factory.h (module 'core'): void ns3::ObjectFactory::SetTypeId(std::string tid) [member function]
    cls.add_method('SetTypeId', 
                   'void', 
                   [param('std::string', 'tid')])
    return

def register_Ns3OriginatorBlockAckAgreement_methods(root_module, cls):
    ## originator-block-ack-agreement.h (module 'wifi'): ns3::OriginatorBlockAckAgreement::OriginatorBlockAckAgreement(ns3::OriginatorBlockAckAgreement const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::OriginatorBlockAckAgreement const &', 'arg0')])
    ## originator-block-ack-agreement.h (module 'wifi'): ns3::OriginatorBlockAckAgreement::OriginatorBlockAckAgreement() [constructor]
    cls.add_constructor([])
    ## originator-block-ack-agreement.h (module 'wifi'): ns3::OriginatorBlockAckAgreement::OriginatorBlockAckAgreement(ns3::Mac48Address recipient, uint8_t tid) [constructor]
    cls.add_constructor([param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')])
    ## originator-block-ack-agreement.h (module 'wifi'): void ns3::OriginatorBlockAckAgreement::CompleteExchange() [member function]
    cls.add_method('CompleteExchange', 
                   'void', 
                   [])
    ## originator-block-ack-agreement.h (module 'wifi'): bool ns3::OriginatorBlockAckAgreement::IsBlockAckRequestNeeded() const [member function]
    cls.add_method('IsBlockAckRequestNeeded', 
                   'bool', 
                   [], 
                   is_const=True)
    ## originator-block-ack-agreement.h (module 'wifi'): bool ns3::OriginatorBlockAckAgreement::IsEstablished() const [member function]
    cls.add_method('IsEstablished', 
                   'bool', 
                   [], 
                   is_const=True)
    ## originator-block-ack-agreement.h (module 'wifi'): bool ns3::OriginatorBlockAckAgreement::IsInactive() const [member function]
    cls.add_method('IsInactive', 
                   'bool', 
                   [], 
                   is_const=True)
    ## originator-block-ack-agreement.h (module 'wifi'): bool ns3::OriginatorBlockAckAgreement::IsPending() const [member function]
    cls.add_method('IsPending', 
                   'bool', 
                   [], 
                   is_const=True)
    ## originator-block-ack-agreement.h (module 'wifi'): bool ns3::OriginatorBlockAckAgreement::IsUnsuccessful() const [member function]
    cls.add_method('IsUnsuccessful', 
                   'bool', 
                   [], 
                   is_const=True)
    ## originator-block-ack-agreement.h (module 'wifi'): void ns3::OriginatorBlockAckAgreement::NotifyMpduTransmission(uint16_t nextSeqNumber) [member function]
    cls.add_method('NotifyMpduTransmission', 
                   'void', 
                   [param('uint16_t', 'nextSeqNumber')])
    ## originator-block-ack-agreement.h (module 'wifi'): void ns3::OriginatorBlockAckAgreement::SetState(ns3::OriginatorBlockAckAgreement::State state) [member function]
    cls.add_method('SetState', 
                   'void', 
                   [param('ns3::OriginatorBlockAckAgreement::State', 'state')])
    return

def register_Ns3PacketMetadata_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::PacketMetadata(uint64_t uid, uint32_t size) [constructor]
    cls.add_constructor([param('uint64_t', 'uid'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::PacketMetadata(ns3::PacketMetadata const & o) [copy constructor]
    cls.add_constructor([param('ns3::PacketMetadata const &', 'o')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddAtEnd(ns3::PacketMetadata const & o) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::PacketMetadata const &', 'o')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddHeader(ns3::Header const & header, uint32_t size) [member function]
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddPaddingAtEnd(uint32_t end) [member function]
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::AddTrailer(ns3::Trailer const & trailer, uint32_t size) [member function]
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator ns3::PacketMetadata::BeginItem(ns3::Buffer buffer) const [member function]
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [param('ns3::Buffer', 'buffer')], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata ns3::PacketMetadata::CreateFragment(uint32_t start, uint32_t end) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::PacketMetadata', 
                   [param('uint32_t', 'start'), param('uint32_t', 'end')], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::Deserialize(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): static void ns3::PacketMetadata::Enable() [member function]
    cls.add_method('Enable', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet-metadata.h (module 'network'): static void ns3::PacketMetadata::EnableChecking() [member function]
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): uint64_t ns3::PacketMetadata::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveAtEnd(uint32_t end) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'end')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveAtStart(uint32_t start) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'start')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveHeader(ns3::Header const & header, uint32_t size) [member function]
    cls.add_method('RemoveHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): void ns3::PacketMetadata::RemoveTrailer(ns3::Trailer const & trailer, uint32_t size) [member function]
    cls.add_method('RemoveTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer'), param('uint32_t', 'size')])
    ## packet-metadata.h (module 'network'): uint32_t ns3::PacketMetadata::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3PacketMetadataItem_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::Item() [constructor]
    cls.add_constructor([])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::Item(ns3::PacketMetadata::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketMetadata::Item const &', 'arg0')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::current [variable]
    cls.add_instance_attribute('current', 'ns3::Buffer::Iterator', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentSize [variable]
    cls.add_instance_attribute('currentSize', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentTrimedFromEnd [variable]
    cls.add_instance_attribute('currentTrimedFromEnd', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::currentTrimedFromStart [variable]
    cls.add_instance_attribute('currentTrimedFromStart', 'uint32_t', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::isFragment [variable]
    cls.add_instance_attribute('isFragment', 'bool', is_const=False)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3PacketMetadataItemIterator_methods(root_module, cls):
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator::ItemIterator(ns3::PacketMetadata::ItemIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketMetadata::ItemIterator const &', 'arg0')])
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::ItemIterator::ItemIterator(ns3::PacketMetadata const * metadata, ns3::Buffer buffer) [constructor]
    cls.add_constructor([param('ns3::PacketMetadata const *', 'metadata'), param('ns3::Buffer', 'buffer')])
    ## packet-metadata.h (module 'network'): bool ns3::PacketMetadata::ItemIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet-metadata.h (module 'network'): ns3::PacketMetadata::Item ns3::PacketMetadata::ItemIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::PacketMetadata::Item', 
                   [])
    return

def register_Ns3PacketTagIterator_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::PacketTagIterator::PacketTagIterator(ns3::PacketTagIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagIterator const &', 'arg0')])
    ## packet.h (module 'network'): bool ns3::PacketTagIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item ns3::PacketTagIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::PacketTagIterator::Item', 
                   [])
    return

def register_Ns3PacketTagIteratorItem_methods(root_module, cls):
    ## packet.h (module 'network'): ns3::PacketTagIterator::Item::Item(ns3::PacketTagIterator::Item const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagIterator::Item const &', 'arg0')])
    ## packet.h (module 'network'): void ns3::PacketTagIterator::Item::GetTag(ns3::Tag & tag) const [member function]
    cls.add_method('GetTag', 
                   'void', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::TypeId ns3::PacketTagIterator::Item::GetTypeId() const [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    return

def register_Ns3PacketTagList_methods(root_module, cls):
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::PacketTagList() [constructor]
    cls.add_constructor([])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::PacketTagList(ns3::PacketTagList const & o) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagList const &', 'o')])
    ## packet-tag-list.h (module 'network'): void ns3::PacketTagList::Add(ns3::Tag const & tag) const [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData const * ns3::PacketTagList::Head() const [member function]
    cls.add_method('Head', 
                   'ns3::PacketTagList::TagData const *', 
                   [], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Peek(ns3::Tag & tag) const [member function]
    cls.add_method('Peek', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Remove(ns3::Tag & tag) [member function]
    cls.add_method('Remove', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet-tag-list.h (module 'network'): void ns3::PacketTagList::RemoveAll() [member function]
    cls.add_method('RemoveAll', 
                   'void', 
                   [])
    ## packet-tag-list.h (module 'network'): bool ns3::PacketTagList::Replace(ns3::Tag & tag) [member function]
    cls.add_method('Replace', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    return

def register_Ns3PacketTagListTagData_methods(root_module, cls):
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData() [constructor]
    cls.add_constructor([])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::TagData(ns3::PacketTagList::TagData const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketTagList::TagData const &', 'arg0')])
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::count [variable]
    cls.add_instance_attribute('count', 'uint32_t', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::data [variable]
    cls.add_instance_attribute('data', 'uint8_t [ 21 ]', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::next [variable]
    cls.add_instance_attribute('next', 'ns3::PacketTagList::TagData *', is_const=False)
    ## packet-tag-list.h (module 'network'): ns3::PacketTagList::TagData::tid [variable]
    cls.add_instance_attribute('tid', 'ns3::TypeId', is_const=False)
    return

def register_Ns3ParameterLogger_methods(root_module, cls):
    ## log.h (module 'core'): ns3::ParameterLogger::ParameterLogger(ns3::ParameterLogger const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ParameterLogger const &', 'arg0')])
    ## log.h (module 'core'): ns3::ParameterLogger::ParameterLogger(std::ostream & os) [constructor]
    cls.add_constructor([param('std::ostream &', 'os')])
    return

def register_Ns3PuActivity_methods(root_module, cls):
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::PuActivity() [constructor]
    cls.add_constructor([])
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::PuActivity(ns3::PuActivity const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PuActivity const &', 'arg0')])
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::alpha [variable]
    cls.add_instance_attribute('alpha', 'double', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::arrival_time [variable]
    cls.add_instance_attribute('arrival_time', 'ns3::Time [ 700 ]', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::beta [variable]
    cls.add_instance_attribute('beta', 'double', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::departure_time [variable]
    cls.add_instance_attribute('departure_time', 'ns3::Time [ 700 ]', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::detected [variable]
    cls.add_instance_attribute('detected', 'bool [ 700 ]', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::interference [variable]
    cls.add_instance_attribute('interference', 'double', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::main_channel [variable]
    cls.add_instance_attribute('main_channel', 'int', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::number_data [variable]
    cls.add_instance_attribute('number_data', 'int', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::radius [variable]
    cls.add_instance_attribute('radius', 'double', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::x_loc [variable]
    cls.add_instance_attribute('x_loc', 'double', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::x_loc_receiver [variable]
    cls.add_instance_attribute('x_loc_receiver', 'double', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::y_loc [variable]
    cls.add_instance_attribute('y_loc', 'double', is_const=False)
    ## pu-model.h (module 'cognitive'): ns3::PuActivity::y_loc_receiver [variable]
    cls.add_instance_attribute('y_loc_receiver', 'double', is_const=False)
    return

def register_Ns3RandomVariableStreamHelper_methods(root_module, cls):
    ## random-variable-stream-helper.h (module 'core'): ns3::RandomVariableStreamHelper::RandomVariableStreamHelper() [constructor]
    cls.add_constructor([])
    ## random-variable-stream-helper.h (module 'core'): ns3::RandomVariableStreamHelper::RandomVariableStreamHelper(ns3::RandomVariableStreamHelper const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RandomVariableStreamHelper const &', 'arg0')])
    ## random-variable-stream-helper.h (module 'core'): static int64_t ns3::RandomVariableStreamHelper::AssignStreams(std::string path, int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('std::string', 'path'), param('int64_t', 'stream')], 
                   is_static=True)
    return

def register_Ns3RepositoryEntryRecv_methods(root_module, cls):
    ## repository.h (module 'cognitive'): ns3::RepositoryEntryRecv::RepositoryEntryRecv() [constructor]
    cls.add_constructor([])
    ## repository.h (module 'cognitive'): ns3::RepositoryEntryRecv::RepositoryEntryRecv(ns3::RepositoryEntryRecv const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RepositoryEntryRecv const &', 'arg0')])
    ## repository.h (module 'cognitive'): ns3::RepositoryEntryRecv::rxChannel [variable]
    cls.add_instance_attribute('rxChannel', 'int', is_const=False)
    return

def register_Ns3RepositoryEntrySend_methods(root_module, cls):
    ## repository.h (module 'cognitive'): ns3::RepositoryEntrySend::RepositoryEntrySend() [constructor]
    cls.add_constructor([])
    ## repository.h (module 'cognitive'): ns3::RepositoryEntrySend::RepositoryEntrySend(ns3::RepositoryEntrySend const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RepositoryEntrySend const &', 'arg0')])
    ## repository.h (module 'cognitive'): ns3::RepositoryEntrySend::active [variable]
    cls.add_instance_attribute('active', 'bool', is_const=False)
    ## repository.h (module 'cognitive'): ns3::RepositoryEntrySend::time [variable]
    cls.add_instance_attribute('time', 'double', is_const=False)
    return

def register_Ns3RngSeedManager_methods(root_module, cls):
    ## rng-seed-manager.h (module 'core'): ns3::RngSeedManager::RngSeedManager() [constructor]
    cls.add_constructor([])
    ## rng-seed-manager.h (module 'core'): ns3::RngSeedManager::RngSeedManager(ns3::RngSeedManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RngSeedManager const &', 'arg0')])
    ## rng-seed-manager.h (module 'core'): static uint64_t ns3::RngSeedManager::GetNextStreamIndex() [member function]
    cls.add_method('GetNextStreamIndex', 
                   'uint64_t', 
                   [], 
                   is_static=True)
    ## rng-seed-manager.h (module 'core'): static uint64_t ns3::RngSeedManager::GetRun() [member function]
    cls.add_method('GetRun', 
                   'uint64_t', 
                   [], 
                   is_static=True)
    ## rng-seed-manager.h (module 'core'): static uint32_t ns3::RngSeedManager::GetSeed() [member function]
    cls.add_method('GetSeed', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## rng-seed-manager.h (module 'core'): static void ns3::RngSeedManager::SetRun(uint64_t run) [member function]
    cls.add_method('SetRun', 
                   'void', 
                   [param('uint64_t', 'run')], 
                   is_static=True)
    ## rng-seed-manager.h (module 'core'): static void ns3::RngSeedManager::SetSeed(uint32_t seed) [member function]
    cls.add_method('SetSeed', 
                   'void', 
                   [param('uint32_t', 'seed')], 
                   is_static=True)
    return

def register_Ns3RngStream_methods(root_module, cls):
    ## rng-stream.h (module 'core'): ns3::RngStream::RngStream(uint32_t seed, uint64_t stream, uint64_t substream) [constructor]
    cls.add_constructor([param('uint32_t', 'seed'), param('uint64_t', 'stream'), param('uint64_t', 'substream')])
    ## rng-stream.h (module 'core'): ns3::RngStream::RngStream(ns3::RngStream const & r) [copy constructor]
    cls.add_constructor([param('ns3::RngStream const &', 'r')])
    ## rng-stream.h (module 'core'): double ns3::RngStream::RandU01() [member function]
    cls.add_method('RandU01', 
                   'double', 
                   [])
    return

def register_Ns3SimpleRefCount__Ns3Object_Ns3ObjectBase_Ns3ObjectDeleter_methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::SimpleRefCount(ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter> const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Object, ns3::ObjectBase, ns3::ObjectDeleter>::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3Simulator_methods(root_module, cls):
    ## simulator.h (module 'core'): ns3::Simulator::Simulator(ns3::Simulator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Simulator const &', 'arg0')])
    ## simulator.h (module 'core'): static void ns3::Simulator::Cancel(ns3::EventId const & id) [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Destroy() [member function]
    cls.add_method('Destroy', 
                   'void', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static uint32_t ns3::Simulator::GetContext() [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::GetDelayLeft(ns3::EventId const & id) [member function]
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Ptr<ns3::SimulatorImpl> ns3::Simulator::GetImplementation() [member function]
    cls.add_method('GetImplementation', 
                   'ns3::Ptr< ns3::SimulatorImpl >', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::GetMaximumSimulationTime() [member function]
    cls.add_method('GetMaximumSimulationTime', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static uint32_t ns3::Simulator::GetSystemId() [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static bool ns3::Simulator::IsExpired(ns3::EventId const & id) [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static bool ns3::Simulator::IsFinished() [member function]
    cls.add_method('IsFinished', 
                   'bool', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static ns3::Time ns3::Simulator::Now() [member function]
    cls.add_method('Now', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Remove(ns3::EventId const & id) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::SetImplementation(ns3::Ptr<ns3::SimulatorImpl> impl) [member function]
    cls.add_method('SetImplementation', 
                   'void', 
                   [param('ns3::Ptr< ns3::SimulatorImpl >', 'impl')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::SetScheduler(ns3::ObjectFactory schedulerFactory) [member function]
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::ObjectFactory', 'schedulerFactory')], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Stop() [member function]
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_static=True)
    ## simulator.h (module 'core'): static void ns3::Simulator::Stop(ns3::Time const & delay) [member function]
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time const &', 'delay')], 
                   is_static=True)
    return

def register_Ns3SpectrumEntry_methods(root_module, cls):
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumEntry::SpectrumEntry() [constructor]
    cls.add_constructor([])
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumEntry::SpectrumEntry(ns3::SpectrumEntry const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumEntry const &', 'arg0')])
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumEntry::bandwidth [variable]
    cls.add_instance_attribute('bandwidth', 'double', is_const=False)
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumEntry::per [variable]
    cls.add_instance_attribute('per', 'double', is_const=False)
    return

def register_Ns3SpectrumManager_methods(root_module, cls):
    ## spectrum-manager.h (module 'cognitive'): ns3::SpectrumManager::SpectrumManager(ns3::SpectrumManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumManager const &', 'arg0')])
    ## spectrum-manager.h (module 'cognitive'): ns3::SpectrumManager::SpectrumManager(ns3::Ptr<ns3::RegularWifiMac> mac, int id) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::RegularWifiMac >', 'mac'), param('int', 'id')])
    ## spectrum-manager.h (module 'cognitive'): ns3::SpectrumManager::SpectrumManager(ns3::Ptr<ns3::RegularWifiMac> mac, ns3::Ptr<ns3::WifiPhy> phy, int id, ns3::Time sense_time, ns3::Time transmit_time) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::RegularWifiMac >', 'mac'), param('ns3::Ptr< ns3::WifiPhy >', 'phy'), param('int', 'id'), param('ns3::Time', 'sense_time'), param('ns3::Time', 'transmit_time')])
    ## spectrum-manager.h (module 'cognitive'): void ns3::SpectrumManager::HandoffEnded() [member function]
    cls.add_method('HandoffEnded', 
                   'void', 
                   [])
    ## spectrum-manager.h (module 'cognitive'): bool ns3::SpectrumManager::IsChannelAvailable() [member function]
    cls.add_method('IsChannelAvailable', 
                   'bool', 
                   [])
    ## spectrum-manager.h (module 'cognitive'): bool ns3::SpectrumManager::IsPuInterfering(ns3::Time txDuration) [member function]
    cls.add_method('IsPuInterfering', 
                   'bool', 
                   [param('ns3::Time', 'txDuration')])
    ## spectrum-manager.h (module 'cognitive'): void ns3::SpectrumManager::SenseEnded() [member function]
    cls.add_method('SenseEnded', 
                   'void', 
                   [])
    ## spectrum-manager.h (module 'cognitive'): void ns3::SpectrumManager::SetPuModel(double prob, ns3::Ptr<ns3::PUModel> p) [member function]
    cls.add_method('SetPuModel', 
                   'void', 
                   [param('double', 'prob'), param('ns3::Ptr< ns3::PUModel >', 'p')])
    ## spectrum-manager.h (module 'cognitive'): void ns3::SpectrumManager::SetRepository(ns3::Ptr<ns3::Repository> rep) [member function]
    cls.add_method('SetRepository', 
                   'void', 
                   [param('ns3::Ptr< ns3::Repository >', 'rep')])
    ## spectrum-manager.h (module 'cognitive'): void ns3::SpectrumManager::Start() [member function]
    cls.add_method('Start', 
                   'void', 
                   [])
    ## spectrum-manager.h (module 'cognitive'): void ns3::SpectrumManager::TransmitEnded() [member function]
    cls.add_method('TransmitEnded', 
                   'void', 
                   [])
    return

def register_Ns3SpectrumSensing_methods(root_module, cls):
    ## spectrum-sensing.h (module 'cognitive'): ns3::SpectrumSensing::SpectrumSensing(ns3::SpectrumSensing const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumSensing const &', 'arg0')])
    ## spectrum-sensing.h (module 'cognitive'): ns3::SpectrumSensing::SpectrumSensing(ns3::SpectrumManager * sm) [constructor]
    cls.add_constructor([param('ns3::SpectrumManager *', 'sm')])
    ## spectrum-sensing.h (module 'cognitive'): ns3::SpectrumSensing::SpectrumSensing(ns3::SpectrumManager * sm, double prob, ns3::Ptr<ns3::PUModel> p) [constructor]
    cls.add_constructor([param('ns3::SpectrumManager *', 'sm'), param('double', 'prob'), param('ns3::Ptr< ns3::PUModel >', 'p')])
    ## spectrum-sensing.h (module 'cognitive'): bool ns3::SpectrumSensing::GetSenseResultsFuture(int id, ns3::Time sense_time, ns3::Time transmit_time, int channel) [member function]
    cls.add_method('GetSenseResultsFuture', 
                   'bool', 
                   [param('int', 'id'), param('ns3::Time', 'sense_time'), param('ns3::Time', 'transmit_time'), param('int', 'channel')])
    return

def register_Ns3SystemCondition_methods(root_module, cls):
    ## system-condition.h (module 'core'): ns3::SystemCondition::SystemCondition(ns3::SystemCondition const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SystemCondition const &', 'arg0')])
    ## system-condition.h (module 'core'): ns3::SystemCondition::SystemCondition() [constructor]
    cls.add_constructor([])
    ## system-condition.h (module 'core'): void ns3::SystemCondition::Broadcast() [member function]
    cls.add_method('Broadcast', 
                   'void', 
                   [])
    ## system-condition.h (module 'core'): bool ns3::SystemCondition::GetCondition() [member function]
    cls.add_method('GetCondition', 
                   'bool', 
                   [])
    ## system-condition.h (module 'core'): void ns3::SystemCondition::SetCondition(bool condition) [member function]
    cls.add_method('SetCondition', 
                   'void', 
                   [param('bool', 'condition')])
    ## system-condition.h (module 'core'): void ns3::SystemCondition::Signal() [member function]
    cls.add_method('Signal', 
                   'void', 
                   [])
    ## system-condition.h (module 'core'): bool ns3::SystemCondition::TimedWait(uint64_t ns) [member function]
    cls.add_method('TimedWait', 
                   'bool', 
                   [param('uint64_t', 'ns')])
    ## system-condition.h (module 'core'): void ns3::SystemCondition::Wait() [member function]
    cls.add_method('Wait', 
                   'void', 
                   [])
    return

def register_Ns3SystemMutex_methods(root_module, cls):
    ## system-mutex.h (module 'core'): ns3::SystemMutex::SystemMutex(ns3::SystemMutex const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SystemMutex const &', 'arg0')])
    ## system-mutex.h (module 'core'): ns3::SystemMutex::SystemMutex() [constructor]
    cls.add_constructor([])
    ## system-mutex.h (module 'core'): void ns3::SystemMutex::Lock() [member function]
    cls.add_method('Lock', 
                   'void', 
                   [])
    ## system-mutex.h (module 'core'): void ns3::SystemMutex::Unlock() [member function]
    cls.add_method('Unlock', 
                   'void', 
                   [])
    return

def register_Ns3SystemWallClockMs_methods(root_module, cls):
    ## system-wall-clock-ms.h (module 'core'): ns3::SystemWallClockMs::SystemWallClockMs(ns3::SystemWallClockMs const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SystemWallClockMs const &', 'arg0')])
    ## system-wall-clock-ms.h (module 'core'): ns3::SystemWallClockMs::SystemWallClockMs() [constructor]
    cls.add_constructor([])
    ## system-wall-clock-ms.h (module 'core'): int64_t ns3::SystemWallClockMs::End() [member function]
    cls.add_method('End', 
                   'int64_t', 
                   [])
    ## system-wall-clock-ms.h (module 'core'): int64_t ns3::SystemWallClockMs::GetElapsedReal() const [member function]
    cls.add_method('GetElapsedReal', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## system-wall-clock-ms.h (module 'core'): int64_t ns3::SystemWallClockMs::GetElapsedSystem() const [member function]
    cls.add_method('GetElapsedSystem', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## system-wall-clock-ms.h (module 'core'): int64_t ns3::SystemWallClockMs::GetElapsedUser() const [member function]
    cls.add_method('GetElapsedUser', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## system-wall-clock-ms.h (module 'core'): void ns3::SystemWallClockMs::Start() [member function]
    cls.add_method('Start', 
                   'void', 
                   [])
    return

def register_Ns3Tag_methods(root_module, cls):
    ## tag.h (module 'network'): ns3::Tag::Tag() [constructor]
    cls.add_constructor([])
    ## tag.h (module 'network'): ns3::Tag::Tag(ns3::Tag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Tag const &', 'arg0')])
    ## tag.h (module 'network'): void ns3::Tag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_virtual=True)
    ## tag.h (module 'network'): uint32_t ns3::Tag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## tag.h (module 'network'): static ns3::TypeId ns3::Tag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## tag.h (module 'network'): void ns3::Tag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## tag.h (module 'network'): void ns3::Tag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TagBuffer_methods(root_module, cls):
    ## tag-buffer.h (module 'network'): ns3::TagBuffer::TagBuffer(ns3::TagBuffer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TagBuffer const &', 'arg0')])
    ## tag-buffer.h (module 'network'): ns3::TagBuffer::TagBuffer(uint8_t * start, uint8_t * end) [constructor]
    cls.add_constructor([param('uint8_t *', 'start'), param('uint8_t *', 'end')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::CopyFrom(ns3::TagBuffer o) [member function]
    cls.add_method('CopyFrom', 
                   'void', 
                   [param('ns3::TagBuffer', 'o')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::Read(uint8_t * buffer, uint32_t size) [member function]
    cls.add_method('Read', 
                   'void', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')])
    ## tag-buffer.h (module 'network'): double ns3::TagBuffer::ReadDouble() [member function]
    cls.add_method('ReadDouble', 
                   'double', 
                   [])
    ## tag-buffer.h (module 'network'): uint16_t ns3::TagBuffer::ReadU16() [member function]
    cls.add_method('ReadU16', 
                   'uint16_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint32_t ns3::TagBuffer::ReadU32() [member function]
    cls.add_method('ReadU32', 
                   'uint32_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint64_t ns3::TagBuffer::ReadU64() [member function]
    cls.add_method('ReadU64', 
                   'uint64_t', 
                   [])
    ## tag-buffer.h (module 'network'): uint8_t ns3::TagBuffer::ReadU8() [member function]
    cls.add_method('ReadU8', 
                   'uint8_t', 
                   [])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::TrimAtEnd(uint32_t trim) [member function]
    cls.add_method('TrimAtEnd', 
                   'void', 
                   [param('uint32_t', 'trim')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::Write(uint8_t const * buffer, uint32_t size) [member function]
    cls.add_method('Write', 
                   'void', 
                   [param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteDouble(double v) [member function]
    cls.add_method('WriteDouble', 
                   'void', 
                   [param('double', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU16(uint16_t data) [member function]
    cls.add_method('WriteU16', 
                   'void', 
                   [param('uint16_t', 'data')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU32(uint32_t data) [member function]
    cls.add_method('WriteU32', 
                   'void', 
                   [param('uint32_t', 'data')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU64(uint64_t v) [member function]
    cls.add_method('WriteU64', 
                   'void', 
                   [param('uint64_t', 'v')])
    ## tag-buffer.h (module 'network'): void ns3::TagBuffer::WriteU8(uint8_t v) [member function]
    cls.add_method('WriteU8', 
                   'void', 
                   [param('uint8_t', 'v')])
    return

def register_Ns3TimeWithUnit_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## nstime.h (module 'core'): ns3::TimeWithUnit::TimeWithUnit(ns3::TimeWithUnit const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TimeWithUnit const &', 'arg0')])
    ## nstime.h (module 'core'): ns3::TimeWithUnit::TimeWithUnit(ns3::Time const time, ns3::Time::Unit const unit) [constructor]
    cls.add_constructor([param('ns3::Time const', 'time'), param('ns3::Time::Unit const', 'unit')])
    return

def register_Ns3Timer_methods(root_module, cls):
    ## timer.h (module 'core'): ns3::Timer::Timer(ns3::Timer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Timer const &', 'arg0')])
    ## timer.h (module 'core'): ns3::Timer::Timer() [constructor]
    cls.add_constructor([])
    ## timer.h (module 'core'): ns3::Timer::Timer(ns3::Timer::DestroyPolicy destroyPolicy) [constructor]
    cls.add_constructor([param('ns3::Timer::DestroyPolicy', 'destroyPolicy')])
    ## timer.h (module 'core'): void ns3::Timer::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## timer.h (module 'core'): ns3::Time ns3::Timer::GetDelay() const [member function]
    cls.add_method('GetDelay', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## timer.h (module 'core'): ns3::Time ns3::Timer::GetDelayLeft() const [member function]
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## timer.h (module 'core'): ns3::Timer::State ns3::Timer::GetState() const [member function]
    cls.add_method('GetState', 
                   'ns3::Timer::State', 
                   [], 
                   is_const=True)
    ## timer.h (module 'core'): bool ns3::Timer::IsExpired() const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [], 
                   is_const=True)
    ## timer.h (module 'core'): bool ns3::Timer::IsRunning() const [member function]
    cls.add_method('IsRunning', 
                   'bool', 
                   [], 
                   is_const=True)
    ## timer.h (module 'core'): bool ns3::Timer::IsSuspended() const [member function]
    cls.add_method('IsSuspended', 
                   'bool', 
                   [], 
                   is_const=True)
    ## timer.h (module 'core'): void ns3::Timer::Remove() [member function]
    cls.add_method('Remove', 
                   'void', 
                   [])
    ## timer.h (module 'core'): void ns3::Timer::Resume() [member function]
    cls.add_method('Resume', 
                   'void', 
                   [])
    ## timer.h (module 'core'): void ns3::Timer::Schedule() [member function]
    cls.add_method('Schedule', 
                   'void', 
                   [])
    ## timer.h (module 'core'): void ns3::Timer::Schedule(ns3::Time delay) [member function]
    cls.add_method('Schedule', 
                   'void', 
                   [param('ns3::Time', 'delay')])
    ## timer.h (module 'core'): void ns3::Timer::SetDelay(ns3::Time const & delay) [member function]
    cls.add_method('SetDelay', 
                   'void', 
                   [param('ns3::Time const &', 'delay')])
    ## timer.h (module 'core'): void ns3::Timer::Suspend() [member function]
    cls.add_method('Suspend', 
                   'void', 
                   [])
    return

def register_Ns3TimerImpl_methods(root_module, cls):
    ## timer-impl.h (module 'core'): ns3::TimerImpl::TimerImpl() [constructor]
    cls.add_constructor([])
    ## timer-impl.h (module 'core'): ns3::TimerImpl::TimerImpl(ns3::TimerImpl const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TimerImpl const &', 'arg0')])
    ## timer-impl.h (module 'core'): void ns3::TimerImpl::Invoke() [member function]
    cls.add_method('Invoke', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## timer-impl.h (module 'core'): ns3::EventId ns3::TimerImpl::Schedule(ns3::Time const & delay) [member function]
    cls.add_method('Schedule', 
                   'ns3::EventId', 
                   [param('ns3::Time const &', 'delay')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3TypeId_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## type-id.h (module 'core'): ns3::TypeId::TypeId(char const * name) [constructor]
    cls.add_constructor([param('char const *', 'name')])
    ## type-id.h (module 'core'): ns3::TypeId::TypeId() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::TypeId(ns3::TypeId const & o) [copy constructor]
    cls.add_constructor([param('ns3::TypeId const &', 'o')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddAttribute(std::string name, std::string help, ns3::AttributeValue const & initialValue, ns3::Ptr<ns3::AttributeAccessor const> accessor, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddAttribute(std::string name, std::string help, uint32_t flags, ns3::AttributeValue const & initialValue, ns3::Ptr<ns3::AttributeAccessor const> accessor, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('AddAttribute', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('uint32_t', 'flags'), param('ns3::AttributeValue const &', 'initialValue'), param('ns3::Ptr< ns3::AttributeAccessor const >', 'accessor'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddTraceSource(std::string name, std::string help, ns3::Ptr<ns3::TraceSourceAccessor const> accessor) [member function]
    cls.add_method('AddTraceSource', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::Ptr< ns3::TraceSourceAccessor const >', 'accessor')], 
                   deprecated=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::AddTraceSource(std::string name, std::string help, ns3::Ptr<ns3::TraceSourceAccessor const> accessor, std::string callback) [member function]
    cls.add_method('AddTraceSource', 
                   'ns3::TypeId', 
                   [param('std::string', 'name'), param('std::string', 'help'), param('ns3::Ptr< ns3::TraceSourceAccessor const >', 'accessor'), param('std::string', 'callback')])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation ns3::TypeId::GetAttribute(uint32_t i) const [member function]
    cls.add_method('GetAttribute', 
                   'ns3::TypeId::AttributeInformation', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetAttributeFullName(uint32_t i) const [member function]
    cls.add_method('GetAttributeFullName', 
                   'std::string', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): uint32_t ns3::TypeId::GetAttributeN() const [member function]
    cls.add_method('GetAttributeN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::Callback<ns3::ObjectBase*,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> ns3::TypeId::GetConstructor() const [member function]
    cls.add_method('GetConstructor', 
                   'ns3::Callback< ns3::ObjectBase *, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetGroupName() const [member function]
    cls.add_method('GetGroupName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): uint32_t ns3::TypeId::GetHash() const [member function]
    cls.add_method('GetHash', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeId::GetName() const [member function]
    cls.add_method('GetName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::GetParent() const [member function]
    cls.add_method('GetParent', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::GetRegistered(uint32_t i) [member function]
    cls.add_method('GetRegistered', 
                   'ns3::TypeId', 
                   [param('uint32_t', 'i')], 
                   is_static=True)
    ## type-id.h (module 'core'): static uint32_t ns3::TypeId::GetRegisteredN() [member function]
    cls.add_method('GetRegisteredN', 
                   'uint32_t', 
                   [], 
                   is_static=True)
    ## type-id.h (module 'core'): std::size_t ns3::TypeId::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'std::size_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation ns3::TypeId::GetTraceSource(uint32_t i) const [member function]
    cls.add_method('GetTraceSource', 
                   'ns3::TypeId::TraceSourceInformation', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## type-id.h (module 'core'): uint32_t ns3::TypeId::GetTraceSourceN() const [member function]
    cls.add_method('GetTraceSourceN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): uint16_t ns3::TypeId::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::HasConstructor() const [member function]
    cls.add_method('HasConstructor', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::HasParent() const [member function]
    cls.add_method('HasParent', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::HideFromDocumentation() [member function]
    cls.add_method('HideFromDocumentation', 
                   'ns3::TypeId', 
                   [])
    ## type-id.h (module 'core'): bool ns3::TypeId::IsChildOf(ns3::TypeId other) const [member function]
    cls.add_method('IsChildOf', 
                   'bool', 
                   [param('ns3::TypeId', 'other')], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::LookupAttributeByName(std::string name, ns3::TypeId::AttributeInformation * info) const [member function]
    cls.add_method('LookupAttributeByName', 
                   'bool', 
                   [param('std::string', 'name'), param('ns3::TypeId::AttributeInformation *', 'info', transfer_ownership=False)], 
                   is_const=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::LookupByHash(uint32_t hash) [member function]
    cls.add_method('LookupByHash', 
                   'ns3::TypeId', 
                   [param('uint32_t', 'hash')], 
                   is_static=True)
    ## type-id.h (module 'core'): static bool ns3::TypeId::LookupByHashFailSafe(uint32_t hash, ns3::TypeId * tid) [member function]
    cls.add_method('LookupByHashFailSafe', 
                   'bool', 
                   [param('uint32_t', 'hash'), param('ns3::TypeId *', 'tid')], 
                   is_static=True)
    ## type-id.h (module 'core'): static ns3::TypeId ns3::TypeId::LookupByName(std::string name) [member function]
    cls.add_method('LookupByName', 
                   'ns3::TypeId', 
                   [param('std::string', 'name')], 
                   is_static=True)
    ## type-id.h (module 'core'): ns3::Ptr<ns3::TraceSourceAccessor const> ns3::TypeId::LookupTraceSourceByName(std::string name) const [member function]
    cls.add_method('LookupTraceSourceByName', 
                   'ns3::Ptr< ns3::TraceSourceAccessor const >', 
                   [param('std::string', 'name')], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::MustHideFromDocumentation() const [member function]
    cls.add_method('MustHideFromDocumentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): bool ns3::TypeId::SetAttributeInitialValue(uint32_t i, ns3::Ptr<ns3::AttributeValue const> initialValue) [member function]
    cls.add_method('SetAttributeInitialValue', 
                   'bool', 
                   [param('uint32_t', 'i'), param('ns3::Ptr< ns3::AttributeValue const >', 'initialValue')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetGroupName(std::string groupName) [member function]
    cls.add_method('SetGroupName', 
                   'ns3::TypeId', 
                   [param('std::string', 'groupName')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetParent(ns3::TypeId tid) [member function]
    cls.add_method('SetParent', 
                   'ns3::TypeId', 
                   [param('ns3::TypeId', 'tid')])
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeId::SetSize(std::size_t size) [member function]
    cls.add_method('SetSize', 
                   'ns3::TypeId', 
                   [param('std::size_t', 'size')])
    ## type-id.h (module 'core'): void ns3::TypeId::SetUid(uint16_t tid) [member function]
    cls.add_method('SetUid', 
                   'void', 
                   [param('uint16_t', 'tid')])
    return

def register_Ns3TypeIdAttributeInformation_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::AttributeInformation() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::AttributeInformation(ns3::TypeId::AttributeInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeId::AttributeInformation const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::accessor [variable]
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::AttributeAccessor const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::checker [variable]
    cls.add_instance_attribute('checker', 'ns3::Ptr< ns3::AttributeChecker const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::flags [variable]
    cls.add_instance_attribute('flags', 'uint32_t', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::help [variable]
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::initialValue [variable]
    cls.add_instance_attribute('initialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::AttributeInformation::originalInitialValue [variable]
    cls.add_instance_attribute('originalInitialValue', 'ns3::Ptr< ns3::AttributeValue const >', is_const=False)
    return

def register_Ns3TypeIdTraceSourceInformation_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::TraceSourceInformation() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::TraceSourceInformation(ns3::TypeId::TraceSourceInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeId::TraceSourceInformation const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::accessor [variable]
    cls.add_instance_attribute('accessor', 'ns3::Ptr< ns3::TraceSourceAccessor const >', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::callback [variable]
    cls.add_instance_attribute('callback', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::help [variable]
    cls.add_instance_attribute('help', 'std::string', is_const=False)
    ## type-id.h (module 'core'): ns3::TypeId::TraceSourceInformation::name [variable]
    cls.add_instance_attribute('name', 'std::string', is_const=False)
    return

def register_Ns3Vector2D_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D(ns3::Vector2D const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector2D const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D(double _x, double _y) [constructor]
    cls.add_constructor([param('double', '_x'), param('double', '_y')])
    ## vector.h (module 'core'): ns3::Vector2D::Vector2D() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2D::x [variable]
    cls.add_instance_attribute('x', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector2D::y [variable]
    cls.add_instance_attribute('y', 'double', is_const=False)
    return

def register_Ns3Vector3D_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D(ns3::Vector3D const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector3D const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D(double _x, double _y, double _z) [constructor]
    cls.add_constructor([param('double', '_x'), param('double', '_y'), param('double', '_z')])
    ## vector.h (module 'core'): ns3::Vector3D::Vector3D() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3D::x [variable]
    cls.add_instance_attribute('x', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector3D::y [variable]
    cls.add_instance_attribute('y', 'double', is_const=False)
    ## vector.h (module 'core'): ns3::Vector3D::z [variable]
    cls.add_instance_attribute('z', 'double', is_const=False)
    return

def register_Ns3Watchdog_methods(root_module, cls):
    ## watchdog.h (module 'core'): ns3::Watchdog::Watchdog(ns3::Watchdog const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Watchdog const &', 'arg0')])
    ## watchdog.h (module 'core'): ns3::Watchdog::Watchdog() [constructor]
    cls.add_constructor([])
    ## watchdog.h (module 'core'): void ns3::Watchdog::Ping(ns3::Time delay) [member function]
    cls.add_method('Ping', 
                   'void', 
                   [param('ns3::Time', 'delay')])
    return

def register_Ns3WifiMode_methods(root_module, cls):
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    ## wifi-mode.h (module 'wifi'): ns3::WifiMode::WifiMode(ns3::WifiMode const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiMode const &', 'arg0')])
    ## wifi-mode.h (module 'wifi'): ns3::WifiMode::WifiMode() [constructor]
    cls.add_constructor([])
    ## wifi-mode.h (module 'wifi'): ns3::WifiMode::WifiMode(std::string name) [constructor]
    cls.add_constructor([param('std::string', 'name')])
    ## wifi-mode.h (module 'wifi'): ns3::WifiCodeRate ns3::WifiMode::GetCodeRate(uint8_t nss) const [member function]
    cls.add_method('GetCodeRate', 
                   'ns3::WifiCodeRate', 
                   [param('uint8_t', 'nss')], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): uint16_t ns3::WifiMode::GetConstellationSize(uint8_t nss) const [member function]
    cls.add_method('GetConstellationSize', 
                   'uint16_t', 
                   [param('uint8_t', 'nss')], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): uint64_t ns3::WifiMode::GetDataRate(uint32_t channelWidth, bool isShortGuardInterval, uint8_t nss) const [member function]
    cls.add_method('GetDataRate', 
                   'uint64_t', 
                   [param('uint32_t', 'channelWidth'), param('bool', 'isShortGuardInterval'), param('uint8_t', 'nss')], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): uint8_t ns3::WifiMode::GetMcsValue() const [member function]
    cls.add_method('GetMcsValue', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): ns3::WifiModulationClass ns3::WifiMode::GetModulationClass() const [member function]
    cls.add_method('GetModulationClass', 
                   'ns3::WifiModulationClass', 
                   [], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): uint64_t ns3::WifiMode::GetPhyRate(uint32_t channelWidth, bool isShortGuardInterval, uint8_t nss) const [member function]
    cls.add_method('GetPhyRate', 
                   'uint64_t', 
                   [param('uint32_t', 'channelWidth'), param('bool', 'isShortGuardInterval'), param('uint8_t', 'nss')], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): uint32_t ns3::WifiMode::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): std::string ns3::WifiMode::GetUniqueName() const [member function]
    cls.add_method('GetUniqueName', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): bool ns3::WifiMode::IsMandatory() const [member function]
    cls.add_method('IsMandatory', 
                   'bool', 
                   [], 
                   is_const=True)
    return

def register_Ns3WifiModeFactory_methods(root_module, cls):
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeFactory::WifiModeFactory(ns3::WifiModeFactory const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiModeFactory const &', 'arg0')])
    ## wifi-mode.h (module 'wifi'): static ns3::WifiMode ns3::WifiModeFactory::CreateWifiMcs(std::string uniqueName, uint8_t mcsValue, ns3::WifiModulationClass modClass) [member function]
    cls.add_method('CreateWifiMcs', 
                   'ns3::WifiMode', 
                   [param('std::string', 'uniqueName'), param('uint8_t', 'mcsValue'), param('ns3::WifiModulationClass', 'modClass')], 
                   is_static=True)
    ## wifi-mode.h (module 'wifi'): static ns3::WifiMode ns3::WifiModeFactory::CreateWifiMode(std::string uniqueName, ns3::WifiModulationClass modClass, bool isMandatory, ns3::WifiCodeRate codingRate, uint16_t constellationSize) [member function]
    cls.add_method('CreateWifiMode', 
                   'ns3::WifiMode', 
                   [param('std::string', 'uniqueName'), param('ns3::WifiModulationClass', 'modClass'), param('bool', 'isMandatory'), param('ns3::WifiCodeRate', 'codingRate'), param('uint16_t', 'constellationSize')], 
                   is_static=True)
    return

def register_Ns3WifiPhyListener_methods(root_module, cls):
    ## wifi-phy.h (module 'wifi'): ns3::WifiPhyListener::WifiPhyListener() [constructor]
    cls.add_constructor([])
    ## wifi-phy.h (module 'wifi'): ns3::WifiPhyListener::WifiPhyListener(ns3::WifiPhyListener const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiPhyListener const &', 'arg0')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhyListener::NotifyMaybeCcaBusyStart(ns3::Time duration) [member function]
    cls.add_method('NotifyMaybeCcaBusyStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhyListener::NotifyRxEndError() [member function]
    cls.add_method('NotifyRxEndError', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhyListener::NotifyRxEndOk() [member function]
    cls.add_method('NotifyRxEndOk', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhyListener::NotifyRxStart(ns3::Time duration) [member function]
    cls.add_method('NotifyRxStart', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhyListener::NotifySleep() [member function]
    cls.add_method('NotifySleep', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhyListener::NotifyTxStart(ns3::Time duration, double txPowerDbm) [member function]
    cls.add_method('NotifyTxStart', 
                   'void', 
                   [param('ns3::Time', 'duration'), param('double', 'txPowerDbm')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhyListener::NotifyWakeup() [member function]
    cls.add_method('NotifyWakeup', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3WifiRemoteStation_methods(root_module, cls):
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation::WifiRemoteStation() [constructor]
    cls.add_constructor([])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation::WifiRemoteStation(ns3::WifiRemoteStation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiRemoteStation const &', 'arg0')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation::m_slrc [variable]
    cls.add_instance_attribute('m_slrc', 'uint32_t', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation::m_ssrc [variable]
    cls.add_instance_attribute('m_ssrc', 'uint32_t', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation::m_state [variable]
    cls.add_instance_attribute('m_state', 'ns3::WifiRemoteStationState *', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation::m_tid [variable]
    cls.add_instance_attribute('m_tid', 'uint8_t', is_const=False)
    return

def register_Ns3WifiRemoteStationInfo_methods(root_module, cls):
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationInfo::WifiRemoteStationInfo(ns3::WifiRemoteStationInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiRemoteStationInfo const &', 'arg0')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationInfo::WifiRemoteStationInfo() [constructor]
    cls.add_constructor([])
    ## wifi-remote-station-manager.h (module 'wifi'): double ns3::WifiRemoteStationInfo::GetFrameErrorRate() const [member function]
    cls.add_method('GetFrameErrorRate', 
                   'double', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationInfo::NotifyTxFailed() [member function]
    cls.add_method('NotifyTxFailed', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationInfo::NotifyTxSuccess(uint32_t retryCounter) [member function]
    cls.add_method('NotifyTxSuccess', 
                   'void', 
                   [param('uint32_t', 'retryCounter')])
    return

def register_Ns3WifiRemoteStationState_methods(root_module, cls):
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::WifiRemoteStationState() [constructor]
    cls.add_constructor([])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::WifiRemoteStationState(ns3::WifiRemoteStationState const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiRemoteStationState const &', 'arg0')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_address [variable]
    cls.add_instance_attribute('m_address', 'ns3::Mac48Address', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_aggregation [variable]
    cls.add_instance_attribute('m_aggregation', 'bool', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_channelWidth [variable]
    cls.add_instance_attribute('m_channelWidth', 'uint32_t', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_greenfield [variable]
    cls.add_instance_attribute('m_greenfield', 'bool', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_info [variable]
    cls.add_instance_attribute('m_info', 'ns3::WifiRemoteStationInfo', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_ness [variable]
    cls.add_instance_attribute('m_ness', 'uint32_t', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_operationalMcsSet [variable]
    cls.add_instance_attribute('m_operationalMcsSet', 'ns3::WifiModeList', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_operationalRateSet [variable]
    cls.add_instance_attribute('m_operationalRateSet', 'ns3::WifiModeList', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_rx [variable]
    cls.add_instance_attribute('m_rx', 'uint32_t', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_shortGuardInterval [variable]
    cls.add_instance_attribute('m_shortGuardInterval', 'bool', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_stbc [variable]
    cls.add_instance_attribute('m_stbc', 'bool', is_const=False)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationState::m_tx [variable]
    cls.add_instance_attribute('m_tx', 'uint32_t', is_const=False)
    return

def register_Ns3WifiTxVector_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## wifi-tx-vector.h (module 'wifi'): ns3::WifiTxVector::WifiTxVector(ns3::WifiTxVector const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiTxVector const &', 'arg0')])
    ## wifi-tx-vector.h (module 'wifi'): ns3::WifiTxVector::WifiTxVector() [constructor]
    cls.add_constructor([])
    ## wifi-tx-vector.h (module 'wifi'): ns3::WifiTxVector::WifiTxVector(ns3::WifiMode mode, uint8_t powerLevel, uint8_t retries, bool shortGuardInterval, uint8_t nss, uint8_t ness, uint32_t channelWidth, bool aggregation, bool stbc) [constructor]
    cls.add_constructor([param('ns3::WifiMode', 'mode'), param('uint8_t', 'powerLevel'), param('uint8_t', 'retries'), param('bool', 'shortGuardInterval'), param('uint8_t', 'nss'), param('uint8_t', 'ness'), param('uint32_t', 'channelWidth'), param('bool', 'aggregation'), param('bool', 'stbc')])
    ## wifi-tx-vector.h (module 'wifi'): uint32_t ns3::WifiTxVector::GetChannelWidth() const [member function]
    cls.add_method('GetChannelWidth', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): ns3::WifiMode ns3::WifiTxVector::GetMode() const [member function]
    cls.add_method('GetMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): uint8_t ns3::WifiTxVector::GetNess() const [member function]
    cls.add_method('GetNess', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): uint8_t ns3::WifiTxVector::GetNss() const [member function]
    cls.add_method('GetNss', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): uint8_t ns3::WifiTxVector::GetRetries() const [member function]
    cls.add_method('GetRetries', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): uint8_t ns3::WifiTxVector::GetTxPowerLevel() const [member function]
    cls.add_method('GetTxPowerLevel', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): bool ns3::WifiTxVector::IsAggregation() const [member function]
    cls.add_method('IsAggregation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): bool ns3::WifiTxVector::IsShortGuardInterval() const [member function]
    cls.add_method('IsShortGuardInterval', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): bool ns3::WifiTxVector::IsStbc() const [member function]
    cls.add_method('IsStbc', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetAggregation(bool aggregation) [member function]
    cls.add_method('SetAggregation', 
                   'void', 
                   [param('bool', 'aggregation')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetChannelWidth(uint32_t channelWidth) [member function]
    cls.add_method('SetChannelWidth', 
                   'void', 
                   [param('uint32_t', 'channelWidth')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetMode(ns3::WifiMode mode) [member function]
    cls.add_method('SetMode', 
                   'void', 
                   [param('ns3::WifiMode', 'mode')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetNess(uint8_t ness) [member function]
    cls.add_method('SetNess', 
                   'void', 
                   [param('uint8_t', 'ness')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetNss(uint8_t nss) [member function]
    cls.add_method('SetNss', 
                   'void', 
                   [param('uint8_t', 'nss')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetRetries(uint8_t retries) [member function]
    cls.add_method('SetRetries', 
                   'void', 
                   [param('uint8_t', 'retries')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetShortGuardInterval(bool guardinterval) [member function]
    cls.add_method('SetShortGuardInterval', 
                   'void', 
                   [param('bool', 'guardinterval')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetStbc(bool stbc) [member function]
    cls.add_method('SetStbc', 
                   'void', 
                   [param('bool', 'stbc')])
    ## wifi-tx-vector.h (module 'wifi'): void ns3::WifiTxVector::SetTxPowerLevel(uint8_t powerlevel) [member function]
    cls.add_method('SetTxPowerLevel', 
                   'void', 
                   [param('uint8_t', 'powerlevel')])
    return

def register_Ns3Empty_methods(root_module, cls):
    ## empty.h (module 'core'): ns3::empty::empty() [constructor]
    cls.add_constructor([])
    ## empty.h (module 'core'): ns3::empty::empty(ns3::empty const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::empty const &', 'arg0')])
    return

def register_Ns3Int64x64_t_methods(root_module, cls):
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('!=')
    cls.add_inplace_numeric_operator('+=', param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_unary_numeric_operator('-')
    cls.add_binary_numeric_operator('/', root_module['ns3::int64x64_t'], root_module['ns3::int64x64_t'], param('ns3::int64x64_t const &', u'right'))
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_inplace_numeric_operator('*=', param('ns3::int64x64_t const &', u'right'))
    cls.add_inplace_numeric_operator('-=', param('ns3::int64x64_t const &', u'right'))
    cls.add_inplace_numeric_operator('/=', param('ns3::int64x64_t const &', u'right'))
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('>=')
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t() [constructor]
    cls.add_constructor([])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(double v) [constructor]
    cls.add_constructor([param('double', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long double v) [constructor]
    cls.add_constructor([param('long double', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(int v) [constructor]
    cls.add_constructor([param('int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long int v) [constructor]
    cls.add_constructor([param('long int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long long int v) [constructor]
    cls.add_constructor([param('long long int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(unsigned int v) [constructor]
    cls.add_constructor([param('unsigned int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long unsigned int v) [constructor]
    cls.add_constructor([param('long unsigned int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(long long unsigned int v) [constructor]
    cls.add_constructor([param('long long unsigned int', 'v')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(int64_t hi, uint64_t lo) [constructor]
    cls.add_constructor([param('int64_t', 'hi'), param('uint64_t', 'lo')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::int64x64_t(ns3::int64x64_t const & o) [copy constructor]
    cls.add_constructor([param('ns3::int64x64_t const &', 'o')])
    ## int64x64-double.h (module 'core'): double ns3::int64x64_t::GetDouble() const [member function]
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    ## int64x64-double.h (module 'core'): int64_t ns3::int64x64_t::GetHigh() const [member function]
    cls.add_method('GetHigh', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## int64x64-double.h (module 'core'): uint64_t ns3::int64x64_t::GetLow() const [member function]
    cls.add_method('GetLow', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## int64x64-double.h (module 'core'): static ns3::int64x64_t ns3::int64x64_t::Invert(uint64_t v) [member function]
    cls.add_method('Invert', 
                   'ns3::int64x64_t', 
                   [param('uint64_t', 'v')], 
                   is_static=True)
    ## int64x64-double.h (module 'core'): void ns3::int64x64_t::MulByInvert(ns3::int64x64_t const & o) [member function]
    cls.add_method('MulByInvert', 
                   'void', 
                   [param('ns3::int64x64_t const &', 'o')])
    ## int64x64-double.h (module 'core'): ns3::int64x64_t::implementation [variable]
    cls.add_static_attribute('implementation', 'ns3::int64x64_t::impl_type const', is_const=True)
    return

def register_Ns3MpduInfo_methods(root_module, cls):
    ## wifi-phy.h (module 'wifi'): ns3::mpduInfo::mpduInfo() [constructor]
    cls.add_constructor([])
    ## wifi-phy.h (module 'wifi'): ns3::mpduInfo::mpduInfo(ns3::mpduInfo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::mpduInfo const &', 'arg0')])
    ## wifi-phy.h (module 'wifi'): ns3::mpduInfo::packetType [variable]
    cls.add_instance_attribute('packetType', 'uint8_t', is_const=False)
    ## wifi-phy.h (module 'wifi'): ns3::mpduInfo::referenceNumber [variable]
    cls.add_instance_attribute('referenceNumber', 'uint32_t', is_const=False)
    return

def register_Ns3SignalNoiseDbm_methods(root_module, cls):
    ## wifi-phy.h (module 'wifi'): ns3::signalNoiseDbm::signalNoiseDbm() [constructor]
    cls.add_constructor([])
    ## wifi-phy.h (module 'wifi'): ns3::signalNoiseDbm::signalNoiseDbm(ns3::signalNoiseDbm const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::signalNoiseDbm const &', 'arg0')])
    ## wifi-phy.h (module 'wifi'): ns3::signalNoiseDbm::noise [variable]
    cls.add_instance_attribute('noise', 'double', is_const=False)
    ## wifi-phy.h (module 'wifi'): ns3::signalNoiseDbm::signal [variable]
    cls.add_instance_attribute('signal', 'double', is_const=False)
    return

def register_Ns3Chunk_methods(root_module, cls):
    ## chunk.h (module 'network'): ns3::Chunk::Chunk() [constructor]
    cls.add_constructor([])
    ## chunk.h (module 'network'): ns3::Chunk::Chunk(ns3::Chunk const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Chunk const &', 'arg0')])
    ## chunk.h (module 'network'): uint32_t ns3::Chunk::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    ## chunk.h (module 'network'): static ns3::TypeId ns3::Chunk::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## chunk.h (module 'network'): void ns3::Chunk::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Header_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## header.h (module 'network'): ns3::Header::Header() [constructor]
    cls.add_constructor([])
    ## header.h (module 'network'): ns3::Header::Header(ns3::Header const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Header const &', 'arg0')])
    ## header.h (module 'network'): uint32_t ns3::Header::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_virtual=True)
    ## header.h (module 'network'): uint32_t ns3::Header::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## header.h (module 'network'): static ns3::TypeId ns3::Header::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## header.h (module 'network'): void ns3::Header::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## header.h (module 'network'): void ns3::Header::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Object_methods(root_module, cls):
    ## object.h (module 'core'): ns3::Object::Object() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): void ns3::Object::AggregateObject(ns3::Ptr<ns3::Object> other) [member function]
    cls.add_method('AggregateObject', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'other')])
    ## object.h (module 'core'): void ns3::Object::Dispose() [member function]
    cls.add_method('Dispose', 
                   'void', 
                   [])
    ## object.h (module 'core'): ns3::Object::AggregateIterator ns3::Object::GetAggregateIterator() const [member function]
    cls.add_method('GetAggregateIterator', 
                   'ns3::Object::AggregateIterator', 
                   [], 
                   is_const=True)
    ## object.h (module 'core'): ns3::TypeId ns3::Object::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object.h (module 'core'): static ns3::TypeId ns3::Object::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## object.h (module 'core'): void ns3::Object::Initialize() [member function]
    cls.add_method('Initialize', 
                   'void', 
                   [])
    ## object.h (module 'core'): ns3::Object::Object(ns3::Object const & o) [copy constructor]
    cls.add_constructor([param('ns3::Object const &', 'o')], 
                        visibility='protected')
    ## object.h (module 'core'): void ns3::Object::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## object.h (module 'core'): void ns3::Object::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## object.h (module 'core'): void ns3::Object::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3ObjectAggregateIterator_methods(root_module, cls):
    ## object.h (module 'core'): ns3::Object::AggregateIterator::AggregateIterator(ns3::Object::AggregateIterator const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Object::AggregateIterator const &', 'arg0')])
    ## object.h (module 'core'): ns3::Object::AggregateIterator::AggregateIterator() [constructor]
    cls.add_constructor([])
    ## object.h (module 'core'): bool ns3::Object::AggregateIterator::HasNext() const [member function]
    cls.add_method('HasNext', 
                   'bool', 
                   [], 
                   is_const=True)
    ## object.h (module 'core'): ns3::Ptr<ns3::Object const> ns3::Object::AggregateIterator::Next() [member function]
    cls.add_method('Next', 
                   'ns3::Ptr< ns3::Object const >', 
                   [])
    return

def register_Ns3PUModel_methods(root_module, cls):
    ## pu-model.h (module 'cognitive'): ns3::PUModel::PUModel(ns3::PUModel const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PUModel const &', 'arg0')])
    ## pu-model.h (module 'cognitive'): ns3::PUModel::PUModel() [constructor]
    cls.add_constructor([])
    ## pu-model.h (module 'cognitive'): bool ns3::PUModel::CheckActive(ns3::Time timeNow, ns3::Time ts) [member function]
    cls.add_method('CheckActive', 
                   'bool', 
                   [param('ns3::Time', 'timeNow'), param('ns3::Time', 'ts')])
    ## pu-model.h (module 'cognitive'): ns3::Time ns3::PUModel::GetNextOffTime(ns3::Time timeNow) [member function]
    cls.add_method('GetNextOffTime', 
                   'ns3::Time', 
                   [param('ns3::Time', 'timeNow')])
    ## pu-model.h (module 'cognitive'): static ns3::TypeId ns3::PUModel::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## pu-model.h (module 'cognitive'): bool ns3::PUModel::IsPuActive(ns3::Time timeNow, ns3::Time ts, double x, double y, int channel) [member function]
    cls.add_method('IsPuActive', 
                   'bool', 
                   [param('ns3::Time', 'timeNow'), param('ns3::Time', 'ts'), param('double', 'x'), param('double', 'y'), param('int', 'channel')])
    ## pu-model.h (module 'cognitive'): void ns3::PUModel::SetPuMapFile(char * file) [member function]
    cls.add_method('SetPuMapFile', 
                   'void', 
                   [param('char *', 'file')])
    return

def register_Ns3PacketChannelPacketTag_methods(root_module, cls):
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketChannelPacketTag::PacketChannelPacketTag(ns3::PacketChannelPacketTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketChannelPacketTag const &', 'arg0')])
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketChannelPacketTag::PacketChannelPacketTag(uint16_t t=0) [constructor]
    cls.add_constructor([param('uint16_t', 't', default_value='0')])
    ## cognitive-packet-tags.h (module 'cognitive'): void ns3::PacketChannelPacketTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): uint16_t ns3::PacketChannelPacketTag::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::TypeId ns3::PacketChannelPacketTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): uint32_t ns3::PacketChannelPacketTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): static ns3::TypeId ns3::PacketChannelPacketTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## cognitive-packet-tags.h (module 'cognitive'): void ns3::PacketChannelPacketTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): void ns3::PacketChannelPacketTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3PacketTypePacketTag_methods(root_module, cls):
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketTypePacketTag::PacketTypePacketTag(ns3::PacketTypePacketTag const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PacketTypePacketTag const &', 'arg0')])
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketTypePacketTag::PacketTypePacketTag(ns3::PacketType t=::ns3::CTRL_PACKET) [constructor]
    cls.add_constructor([param('ns3::PacketType', 't', default_value='::ns3::CTRL_PACKET')])
    ## cognitive-packet-tags.h (module 'cognitive'): void ns3::PacketTypePacketTag::Deserialize(ns3::TagBuffer i) [member function]
    cls.add_method('Deserialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::PacketType ns3::PacketTypePacketTag::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::PacketType', 
                   [], 
                   is_const=True)
    ## cognitive-packet-tags.h (module 'cognitive'): ns3::TypeId ns3::PacketTypePacketTag::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): uint32_t ns3::PacketTypePacketTag::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): static ns3::TypeId ns3::PacketTypePacketTag::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## cognitive-packet-tags.h (module 'cognitive'): void ns3::PacketTypePacketTag::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): void ns3::PacketTypePacketTag::Serialize(ns3::TagBuffer i) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::TagBuffer', 'i')], 
                   is_const=True, is_virtual=True)
    ## cognitive-packet-tags.h (module 'cognitive'): void ns3::PacketTypePacketTag::Set(ns3::PacketType m_type) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::PacketType', 'm_type')])
    return

def register_Ns3RandomVariableStream_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::RandomVariableStream::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::RandomVariableStream::RandomVariableStream() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::RandomVariableStream::SetStream(int64_t stream) [member function]
    cls.add_method('SetStream', 
                   'void', 
                   [param('int64_t', 'stream')])
    ## random-variable-stream.h (module 'core'): int64_t ns3::RandomVariableStream::GetStream() const [member function]
    cls.add_method('GetStream', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): void ns3::RandomVariableStream::SetAntithetic(bool isAntithetic) [member function]
    cls.add_method('SetAntithetic', 
                   'void', 
                   [param('bool', 'isAntithetic')])
    ## random-variable-stream.h (module 'core'): bool ns3::RandomVariableStream::IsAntithetic() const [member function]
    cls.add_method('IsAntithetic', 
                   'bool', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::RandomVariableStream::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::RandomVariableStream::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## random-variable-stream.h (module 'core'): ns3::RngStream * ns3::RandomVariableStream::Peek() const [member function]
    cls.add_method('Peek', 
                   'ns3::RngStream *', 
                   [], 
                   is_const=True, visibility='protected')
    return

def register_Ns3Repository_methods(root_module, cls):
    ## repository.h (module 'cognitive'): ns3::Repository::Repository(ns3::Repository const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Repository const &', 'arg0')])
    ## repository.h (module 'cognitive'): ns3::Repository::Repository() [constructor]
    cls.add_constructor([])
    ## repository.h (module 'cognitive'): int ns3::Repository::GetRxChannel(int node) [member function]
    cls.add_method('GetRxChannel', 
                   'int', 
                   [param('int', 'node')])
    ## repository.h (module 'cognitive'): static ns3::TypeId ns3::Repository::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## repository.h (module 'cognitive'): void ns3::Repository::SetRxChannel(int node, int channel) [member function]
    cls.add_method('SetRxChannel', 
                   'void', 
                   [param('int', 'node'), param('int', 'channel')])
    ## repository.h (module 'cognitive'): void ns3::Repository::UpdateTxChannel(int node, int channel, double time) [member function]
    cls.add_method('UpdateTxChannel', 
                   'void', 
                   [param('int', 'node'), param('int', 'channel'), param('double', 'time')])
    return

def register_Ns3Scheduler_methods(root_module, cls):
    ## scheduler.h (module 'core'): ns3::Scheduler::Scheduler() [constructor]
    cls.add_constructor([])
    ## scheduler.h (module 'core'): ns3::Scheduler::Scheduler(ns3::Scheduler const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Scheduler const &', 'arg0')])
    ## scheduler.h (module 'core'): static ns3::TypeId ns3::Scheduler::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## scheduler.h (module 'core'): void ns3::Scheduler::Insert(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_pure_virtual=True, is_virtual=True)
    ## scheduler.h (module 'core'): bool ns3::Scheduler::IsEmpty() const [member function]
    cls.add_method('IsEmpty', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## scheduler.h (module 'core'): ns3::Scheduler::Event ns3::Scheduler::PeekNext() const [member function]
    cls.add_method('PeekNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## scheduler.h (module 'core'): void ns3::Scheduler::Remove(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_pure_virtual=True, is_virtual=True)
    ## scheduler.h (module 'core'): ns3::Scheduler::Event ns3::Scheduler::RemoveNext() [member function]
    cls.add_method('RemoveNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3SchedulerEvent_methods(root_module, cls):
    cls.add_binary_comparison_operator('<')
    ## scheduler.h (module 'core'): ns3::Scheduler::Event::Event() [constructor]
    cls.add_constructor([])
    ## scheduler.h (module 'core'): ns3::Scheduler::Event::Event(ns3::Scheduler::Event const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Scheduler::Event const &', 'arg0')])
    ## scheduler.h (module 'core'): ns3::Scheduler::Event::impl [variable]
    cls.add_instance_attribute('impl', 'ns3::EventImpl *', is_const=False)
    ## scheduler.h (module 'core'): ns3::Scheduler::Event::key [variable]
    cls.add_instance_attribute('key', 'ns3::Scheduler::EventKey', is_const=False)
    return

def register_Ns3SchedulerEventKey_methods(root_module, cls):
    cls.add_binary_comparison_operator('!=')
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    ## scheduler.h (module 'core'): ns3::Scheduler::EventKey::EventKey() [constructor]
    cls.add_constructor([])
    ## scheduler.h (module 'core'): ns3::Scheduler::EventKey::EventKey(ns3::Scheduler::EventKey const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Scheduler::EventKey const &', 'arg0')])
    ## scheduler.h (module 'core'): ns3::Scheduler::EventKey::m_context [variable]
    cls.add_instance_attribute('m_context', 'uint32_t', is_const=False)
    ## scheduler.h (module 'core'): ns3::Scheduler::EventKey::m_ts [variable]
    cls.add_instance_attribute('m_ts', 'uint64_t', is_const=False)
    ## scheduler.h (module 'core'): ns3::Scheduler::EventKey::m_uid [variable]
    cls.add_instance_attribute('m_uid', 'uint32_t', is_const=False)
    return

def register_Ns3SequentialRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::SequentialRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::SequentialRandomVariable::SequentialRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): ns3::Ptr<ns3::RandomVariableStream> ns3::SequentialRandomVariable::GetIncrement() const [member function]
    cls.add_method('GetIncrement', 
                   'ns3::Ptr< ns3::RandomVariableStream >', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::SequentialRandomVariable::GetConsecutive() const [member function]
    cls.add_method('GetConsecutive', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::SequentialRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::SequentialRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeAccessor__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter< ns3::AttributeAccessor > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::AttributeAccessor, ns3::empty, ns3::DefaultDeleter<ns3::AttributeAccessor> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeChecker_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeChecker__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter< ns3::AttributeChecker > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::AttributeChecker, ns3::empty, ns3::DefaultDeleter<ns3::AttributeChecker> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3AttributeValue_Ns3Empty_Ns3DefaultDeleter__lt__ns3AttributeValue__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::SimpleRefCount(ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter< ns3::AttributeValue > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::AttributeValue, ns3::empty, ns3::DefaultDeleter<ns3::AttributeValue> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3CallbackImplBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3CallbackImplBase__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::SimpleRefCount(ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter< ns3::CallbackImplBase > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::CallbackImplBase, ns3::empty, ns3::DefaultDeleter<ns3::CallbackImplBase> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3EventImpl_Ns3Empty_Ns3DefaultDeleter__lt__ns3EventImpl__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::SimpleRefCount(ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::EventImpl, ns3::empty, ns3::DefaultDeleter< ns3::EventImpl > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::EventImpl, ns3::empty, ns3::DefaultDeleter<ns3::EventImpl> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3FdReader_Ns3Empty_Ns3DefaultDeleter__lt__ns3FdReader__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::FdReader, ns3::empty, ns3::DefaultDeleter<ns3::FdReader> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::FdReader, ns3::empty, ns3::DefaultDeleter<ns3::FdReader> >::SimpleRefCount(ns3::SimpleRefCount<ns3::FdReader, ns3::empty, ns3::DefaultDeleter<ns3::FdReader> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::FdReader, ns3::empty, ns3::DefaultDeleter< ns3::FdReader > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::FdReader, ns3::empty, ns3::DefaultDeleter<ns3::FdReader> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3HashImplementation_Ns3Empty_Ns3DefaultDeleter__lt__ns3HashImplementation__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter< ns3::Hash::Implementation > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Hash::Implementation, ns3::empty, ns3::DefaultDeleter<ns3::Hash::Implementation> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3NixVector_Ns3Empty_Ns3DefaultDeleter__lt__ns3NixVector__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::SimpleRefCount(ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::NixVector, ns3::empty, ns3::DefaultDeleter< ns3::NixVector > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::NixVector, ns3::empty, ns3::DefaultDeleter<ns3::NixVector> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3Packet_Ns3Empty_Ns3DefaultDeleter__lt__ns3Packet__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::SimpleRefCount(ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::Packet, ns3::empty, ns3::DefaultDeleter< ns3::Packet > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::Packet, ns3::empty, ns3::DefaultDeleter<ns3::Packet> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3RefCountBase_Ns3Empty_Ns3DefaultDeleter__lt__ns3RefCountBase__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter<ns3::RefCountBase> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter<ns3::RefCountBase> >::SimpleRefCount(ns3::SimpleRefCount<ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter<ns3::RefCountBase> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter< ns3::RefCountBase > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::RefCountBase, ns3::empty, ns3::DefaultDeleter<ns3::RefCountBase> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3SystemThread_Ns3Empty_Ns3DefaultDeleter__lt__ns3SystemThread__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SystemThread, ns3::empty, ns3::DefaultDeleter<ns3::SystemThread> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::SystemThread, ns3::empty, ns3::DefaultDeleter<ns3::SystemThread> >::SimpleRefCount(ns3::SimpleRefCount<ns3::SystemThread, ns3::empty, ns3::DefaultDeleter<ns3::SystemThread> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::SystemThread, ns3::empty, ns3::DefaultDeleter< ns3::SystemThread > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::SystemThread, ns3::empty, ns3::DefaultDeleter<ns3::SystemThread> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3TraceSourceAccessor_Ns3Empty_Ns3DefaultDeleter__lt__ns3TraceSourceAccessor__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::SimpleRefCount(ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter< ns3::TraceSourceAccessor > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::TraceSourceAccessor, ns3::empty, ns3::DefaultDeleter<ns3::TraceSourceAccessor> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimpleRefCount__Ns3WifiInformationElement_Ns3Empty_Ns3DefaultDeleter__lt__ns3WifiInformationElement__gt___methods(root_module, cls):
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter<ns3::WifiInformationElement> >::SimpleRefCount() [constructor]
    cls.add_constructor([])
    ## simple-ref-count.h (module 'core'): ns3::SimpleRefCount<ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter<ns3::WifiInformationElement> >::SimpleRefCount(ns3::SimpleRefCount<ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter<ns3::WifiInformationElement> > const & o) [copy constructor]
    cls.add_constructor([param('ns3::SimpleRefCount< ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter< ns3::WifiInformationElement > > const &', 'o')])
    ## simple-ref-count.h (module 'core'): static void ns3::SimpleRefCount<ns3::WifiInformationElement, ns3::empty, ns3::DefaultDeleter<ns3::WifiInformationElement> >::Cleanup() [member function]
    cls.add_method('Cleanup', 
                   'void', 
                   [], 
                   is_static=True)
    return

def register_Ns3SimulatorImpl_methods(root_module, cls):
    ## simulator-impl.h (module 'core'): ns3::SimulatorImpl::SimulatorImpl() [constructor]
    cls.add_constructor([])
    ## simulator-impl.h (module 'core'): ns3::SimulatorImpl::SimulatorImpl(ns3::SimulatorImpl const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SimulatorImpl const &', 'arg0')])
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::Cancel(ns3::EventId const & id) [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::Destroy() [member function]
    cls.add_method('Destroy', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): uint32_t ns3::SimulatorImpl::GetContext() const [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): ns3::Time ns3::SimulatorImpl::GetDelayLeft(ns3::EventId const & id) const [member function]
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [param('ns3::EventId const &', 'id')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): ns3::Time ns3::SimulatorImpl::GetMaximumSimulationTime() const [member function]
    cls.add_method('GetMaximumSimulationTime', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): uint32_t ns3::SimulatorImpl::GetSystemId() const [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): static ns3::TypeId ns3::SimulatorImpl::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## simulator-impl.h (module 'core'): bool ns3::SimulatorImpl::IsExpired(ns3::EventId const & id) const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [param('ns3::EventId const &', 'id')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): bool ns3::SimulatorImpl::IsFinished() const [member function]
    cls.add_method('IsFinished', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): ns3::Time ns3::SimulatorImpl::Now() const [member function]
    cls.add_method('Now', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::Remove(ns3::EventId const & id) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::Run() [member function]
    cls.add_method('Run', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): ns3::EventId ns3::SimulatorImpl::Schedule(ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('Schedule', 
                   'ns3::EventId', 
                   [param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): ns3::EventId ns3::SimulatorImpl::ScheduleDestroy(ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleDestroy', 
                   'ns3::EventId', 
                   [param('ns3::EventImpl *', 'event')], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): ns3::EventId ns3::SimulatorImpl::ScheduleNow(ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleNow', 
                   'ns3::EventId', 
                   [param('ns3::EventImpl *', 'event')], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::ScheduleWithContext(uint32_t context, ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleWithContext', 
                   'void', 
                   [param('uint32_t', 'context'), param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::SetScheduler(ns3::ObjectFactory schedulerFactory) [member function]
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::ObjectFactory', 'schedulerFactory')], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::Stop() [member function]
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## simulator-impl.h (module 'core'): void ns3::SimulatorImpl::Stop(ns3::Time const & delay) [member function]
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time const &', 'delay')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3SpectrumData_methods(root_module, cls):
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumData::SpectrumData(ns3::SpectrumData const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumData const &', 'arg0')])
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumData::SpectrumData() [constructor]
    cls.add_constructor([])
    ## spectrum-data.h (module 'cognitive'): ns3::SpectrumEntry ns3::SpectrumData::GetSpectrumData(int channel) [member function]
    cls.add_method('GetSpectrumData', 
                   'ns3::SpectrumEntry', 
                   [param('int', 'channel')])
    ## spectrum-data.h (module 'cognitive'): static ns3::TypeId ns3::SpectrumData::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    return

def register_Ns3SpectrumDecision_methods(root_module, cls):
    ## spectrum-decision.h (module 'cognitive'): ns3::SpectrumDecision::SpectrumDecision(ns3::SpectrumDecision const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SpectrumDecision const &', 'arg0')])
    ## spectrum-decision.h (module 'cognitive'): ns3::SpectrumDecision::SpectrumDecision(ns3::SpectrumManager * sm) [constructor]
    cls.add_constructor([param('ns3::SpectrumManager *', 'sm')])
    ## spectrum-decision.h (module 'cognitive'): int ns3::SpectrumDecision::DecideSpectrum(int current_channel) [member function]
    cls.add_method('DecideSpectrum', 
                   'int', 
                   [param('int', 'current_channel')])
    ## spectrum-decision.h (module 'cognitive'): bool ns3::SpectrumDecision::DecideSwitch() [member function]
    cls.add_method('DecideSwitch', 
                   'bool', 
                   [])
    return

def register_Ns3Synchronizer_methods(root_module, cls):
    ## synchronizer.h (module 'core'): ns3::Synchronizer::Synchronizer(ns3::Synchronizer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Synchronizer const &', 'arg0')])
    ## synchronizer.h (module 'core'): ns3::Synchronizer::Synchronizer() [constructor]
    cls.add_constructor([])
    ## synchronizer.h (module 'core'): uint64_t ns3::Synchronizer::EventEnd() [member function]
    cls.add_method('EventEnd', 
                   'uint64_t', 
                   [])
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::EventStart() [member function]
    cls.add_method('EventStart', 
                   'void', 
                   [])
    ## synchronizer.h (module 'core'): uint64_t ns3::Synchronizer::GetCurrentRealtime() [member function]
    cls.add_method('GetCurrentRealtime', 
                   'uint64_t', 
                   [])
    ## synchronizer.h (module 'core'): int64_t ns3::Synchronizer::GetDrift(uint64_t ts) [member function]
    cls.add_method('GetDrift', 
                   'int64_t', 
                   [param('uint64_t', 'ts')])
    ## synchronizer.h (module 'core'): uint64_t ns3::Synchronizer::GetOrigin() [member function]
    cls.add_method('GetOrigin', 
                   'uint64_t', 
                   [])
    ## synchronizer.h (module 'core'): static ns3::TypeId ns3::Synchronizer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## synchronizer.h (module 'core'): bool ns3::Synchronizer::Realtime() [member function]
    cls.add_method('Realtime', 
                   'bool', 
                   [])
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::SetCondition(bool arg0) [member function]
    cls.add_method('SetCondition', 
                   'void', 
                   [param('bool', 'arg0')])
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::SetOrigin(uint64_t ts) [member function]
    cls.add_method('SetOrigin', 
                   'void', 
                   [param('uint64_t', 'ts')])
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::Signal() [member function]
    cls.add_method('Signal', 
                   'void', 
                   [])
    ## synchronizer.h (module 'core'): bool ns3::Synchronizer::Synchronize(uint64_t tsCurrent, uint64_t tsDelay) [member function]
    cls.add_method('Synchronize', 
                   'bool', 
                   [param('uint64_t', 'tsCurrent'), param('uint64_t', 'tsDelay')])
    ## synchronizer.h (module 'core'): uint64_t ns3::Synchronizer::DoEventEnd() [member function]
    cls.add_method('DoEventEnd', 
                   'uint64_t', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::DoEventStart() [member function]
    cls.add_method('DoEventStart', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): uint64_t ns3::Synchronizer::DoGetCurrentRealtime() [member function]
    cls.add_method('DoGetCurrentRealtime', 
                   'uint64_t', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): int64_t ns3::Synchronizer::DoGetDrift(uint64_t ns) [member function]
    cls.add_method('DoGetDrift', 
                   'int64_t', 
                   [param('uint64_t', 'ns')], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): bool ns3::Synchronizer::DoRealtime() [member function]
    cls.add_method('DoRealtime', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::DoSetCondition(bool arg0) [member function]
    cls.add_method('DoSetCondition', 
                   'void', 
                   [param('bool', 'arg0')], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::DoSetOrigin(uint64_t ns) [member function]
    cls.add_method('DoSetOrigin', 
                   'void', 
                   [param('uint64_t', 'ns')], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): void ns3::Synchronizer::DoSignal() [member function]
    cls.add_method('DoSignal', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    ## synchronizer.h (module 'core'): bool ns3::Synchronizer::DoSynchronize(uint64_t nsCurrent, uint64_t nsDelay) [member function]
    cls.add_method('DoSynchronize', 
                   'bool', 
                   [param('uint64_t', 'nsCurrent'), param('uint64_t', 'nsDelay')], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    return

def register_Ns3SystemThread_methods(root_module, cls):
    ## system-thread.h (module 'core'): ns3::SystemThread::SystemThread(ns3::SystemThread const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SystemThread const &', 'arg0')])
    ## system-thread.h (module 'core'): ns3::SystemThread::SystemThread(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [constructor]
    cls.add_constructor([param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## system-thread.h (module 'core'): static bool ns3::SystemThread::Equals(pthread_t id) [member function]
    cls.add_method('Equals', 
                   'bool', 
                   [param('pthread_t', 'id')], 
                   is_static=True)
    ## system-thread.h (module 'core'): void ns3::SystemThread::Join() [member function]
    cls.add_method('Join', 
                   'void', 
                   [])
    ## system-thread.h (module 'core'): static pthread_t ns3::SystemThread::Self() [member function]
    cls.add_method('Self', 
                   'pthread_t', 
                   [], 
                   is_static=True)
    ## system-thread.h (module 'core'): void ns3::SystemThread::Start() [member function]
    cls.add_method('Start', 
                   'void', 
                   [])
    return

def register_Ns3Time_methods(root_module, cls):
    cls.add_binary_comparison_operator('<=')
    cls.add_binary_comparison_operator('!=')
    cls.add_inplace_numeric_operator('+=', param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('*', root_module['ns3::Time'], root_module['ns3::Time'], param('int64_t const &', u'right'))
    cls.add_binary_numeric_operator('+', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('-', root_module['ns3::Time'], root_module['ns3::Time'], param('ns3::Time const &', u'right'))
    cls.add_binary_numeric_operator('/', root_module['ns3::Time'], root_module['ns3::Time'], param('int64_t const &', u'right'))
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('>')
    cls.add_inplace_numeric_operator('-=', param('ns3::Time const &', u'right'))
    cls.add_output_stream_operator()
    cls.add_binary_comparison_operator('==')
    cls.add_binary_comparison_operator('>=')
    ## nstime.h (module 'core'): ns3::Time::Time() [constructor]
    cls.add_constructor([])
    ## nstime.h (module 'core'): ns3::Time::Time(ns3::Time const & o) [copy constructor]
    cls.add_constructor([param('ns3::Time const &', 'o')])
    ## nstime.h (module 'core'): ns3::Time::Time(double v) [constructor]
    cls.add_constructor([param('double', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(int v) [constructor]
    cls.add_constructor([param('int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long int v) [constructor]
    cls.add_constructor([param('long int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long long int v) [constructor]
    cls.add_constructor([param('long long int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(unsigned int v) [constructor]
    cls.add_constructor([param('unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long unsigned int v) [constructor]
    cls.add_constructor([param('long unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(long long unsigned int v) [constructor]
    cls.add_constructor([param('long long unsigned int', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(ns3::int64x64_t const & v) [constructor]
    cls.add_constructor([param('ns3::int64x64_t const &', 'v')])
    ## nstime.h (module 'core'): ns3::Time::Time(std::string const & s) [constructor]
    cls.add_constructor([param('std::string const &', 's')])
    ## nstime.h (module 'core'): ns3::TimeWithUnit ns3::Time::As(ns3::Time::Unit const unit) const [member function]
    cls.add_method('As', 
                   'ns3::TimeWithUnit', 
                   [param('ns3::Time::Unit const', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): int ns3::Time::Compare(ns3::Time const & o) const [member function]
    cls.add_method('Compare', 
                   'int', 
                   [param('ns3::Time const &', 'o')], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::From(ns3::int64x64_t const & value) [member function]
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'value')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::From(ns3::int64x64_t const & value, ns3::Time::Unit unit) [member function]
    cls.add_method('From', 
                   'ns3::Time', 
                   [param('ns3::int64x64_t const &', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::FromDouble(double value, ns3::Time::Unit unit) [member function]
    cls.add_method('FromDouble', 
                   'ns3::Time', 
                   [param('double', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::FromInteger(uint64_t value, ns3::Time::Unit unit) [member function]
    cls.add_method('FromInteger', 
                   'ns3::Time', 
                   [param('uint64_t', 'value'), param('ns3::Time::Unit', 'unit')], 
                   is_static=True)
    ## nstime.h (module 'core'): double ns3::Time::GetDays() const [member function]
    cls.add_method('GetDays', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetDouble() const [member function]
    cls.add_method('GetDouble', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetFemtoSeconds() const [member function]
    cls.add_method('GetFemtoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetHours() const [member function]
    cls.add_method('GetHours', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetInteger() const [member function]
    cls.add_method('GetInteger', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetMicroSeconds() const [member function]
    cls.add_method('GetMicroSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetMilliSeconds() const [member function]
    cls.add_method('GetMilliSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetMinutes() const [member function]
    cls.add_method('GetMinutes', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetNanoSeconds() const [member function]
    cls.add_method('GetNanoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetPicoSeconds() const [member function]
    cls.add_method('GetPicoSeconds', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time::Unit ns3::Time::GetResolution() [member function]
    cls.add_method('GetResolution', 
                   'ns3::Time::Unit', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): double ns3::Time::GetSeconds() const [member function]
    cls.add_method('GetSeconds', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::GetTimeStep() const [member function]
    cls.add_method('GetTimeStep', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::GetYears() const [member function]
    cls.add_method('GetYears', 
                   'double', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsNegative() const [member function]
    cls.add_method('IsNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsPositive() const [member function]
    cls.add_method('IsPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsStrictlyNegative() const [member function]
    cls.add_method('IsStrictlyNegative', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsStrictlyPositive() const [member function]
    cls.add_method('IsStrictlyPositive', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): bool ns3::Time::IsZero() const [member function]
    cls.add_method('IsZero', 
                   'bool', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::Max() [member function]
    cls.add_method('Max', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): static ns3::Time ns3::Time::Min() [member function]
    cls.add_method('Min', 
                   'ns3::Time', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): static void ns3::Time::SetResolution(ns3::Time::Unit resolution) [member function]
    cls.add_method('SetResolution', 
                   'void', 
                   [param('ns3::Time::Unit', 'resolution')], 
                   is_static=True)
    ## nstime.h (module 'core'): static bool ns3::Time::StaticInit() [member function]
    cls.add_method('StaticInit', 
                   'bool', 
                   [], 
                   is_static=True)
    ## nstime.h (module 'core'): ns3::int64x64_t ns3::Time::To(ns3::Time::Unit unit) const [member function]
    cls.add_method('To', 
                   'ns3::int64x64_t', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): double ns3::Time::ToDouble(ns3::Time::Unit unit) const [member function]
    cls.add_method('ToDouble', 
                   'double', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    ## nstime.h (module 'core'): int64_t ns3::Time::ToInteger(ns3::Time::Unit unit) const [member function]
    cls.add_method('ToInteger', 
                   'int64_t', 
                   [param('ns3::Time::Unit', 'unit')], 
                   is_const=True)
    return

def register_Ns3TraceSourceAccessor_methods(root_module, cls):
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor::TraceSourceAccessor(ns3::TraceSourceAccessor const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TraceSourceAccessor const &', 'arg0')])
    ## trace-source-accessor.h (module 'core'): ns3::TraceSourceAccessor::TraceSourceAccessor() [constructor]
    cls.add_constructor([])
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::Connect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('Connect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::ConnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('ConnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::Disconnect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('Disconnect', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('std::string', 'context'), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trace-source-accessor.h (module 'core'): bool ns3::TraceSourceAccessor::DisconnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]
    cls.add_method('DisconnectWithoutContext', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'obj', transfer_ownership=False), param('ns3::CallbackBase const &', 'cb')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3Trailer_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## trailer.h (module 'network'): ns3::Trailer::Trailer() [constructor]
    cls.add_constructor([])
    ## trailer.h (module 'network'): ns3::Trailer::Trailer(ns3::Trailer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Trailer const &', 'arg0')])
    ## trailer.h (module 'network'): uint32_t ns3::Trailer::Deserialize(ns3::Buffer::Iterator end) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'end')], 
                   is_pure_virtual=True, is_virtual=True)
    ## trailer.h (module 'network'): uint32_t ns3::Trailer::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trailer.h (module 'network'): static ns3::TypeId ns3::Trailer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## trailer.h (module 'network'): void ns3::Trailer::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## trailer.h (module 'network'): void ns3::Trailer::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3TriangularRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::TriangularRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::TriangularRandomVariable::TriangularRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetValue(double mean, double min, double max) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'min'), param('double', 'max')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::TriangularRandomVariable::GetInteger(uint32_t mean, uint32_t min, uint32_t max) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'min'), param('uint32_t', 'max')])
    ## random-variable-stream.h (module 'core'): double ns3::TriangularRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::TriangularRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3UniformRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::UniformRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::UniformRandomVariable::UniformRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetMin() const [member function]
    cls.add_method('GetMin', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetMax() const [member function]
    cls.add_method('GetMax', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetValue(double min, double max) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'min'), param('double', 'max')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::UniformRandomVariable::GetInteger(uint32_t min, uint32_t max) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'min'), param('uint32_t', 'max')])
    ## random-variable-stream.h (module 'core'): double ns3::UniformRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::UniformRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3WallClockSynchronizer_methods(root_module, cls):
    ## wall-clock-synchronizer.h (module 'core'): ns3::WallClockSynchronizer::WallClockSynchronizer(ns3::WallClockSynchronizer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WallClockSynchronizer const &', 'arg0')])
    ## wall-clock-synchronizer.h (module 'core'): ns3::WallClockSynchronizer::WallClockSynchronizer() [constructor]
    cls.add_constructor([])
    ## wall-clock-synchronizer.h (module 'core'): static ns3::TypeId ns3::WallClockSynchronizer::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wall-clock-synchronizer.h (module 'core'): ns3::WallClockSynchronizer::NS_PER_SEC [variable]
    cls.add_static_attribute('NS_PER_SEC', 'uint64_t const', is_const=True)
    ## wall-clock-synchronizer.h (module 'core'): ns3::WallClockSynchronizer::US_PER_NS [variable]
    cls.add_static_attribute('US_PER_NS', 'uint64_t const', is_const=True)
    ## wall-clock-synchronizer.h (module 'core'): ns3::WallClockSynchronizer::US_PER_SEC [variable]
    cls.add_static_attribute('US_PER_SEC', 'uint64_t const', is_const=True)
    ## wall-clock-synchronizer.h (module 'core'): uint64_t ns3::WallClockSynchronizer::DoEventEnd() [member function]
    cls.add_method('DoEventEnd', 
                   'uint64_t', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): void ns3::WallClockSynchronizer::DoEventStart() [member function]
    cls.add_method('DoEventStart', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): uint64_t ns3::WallClockSynchronizer::DoGetCurrentRealtime() [member function]
    cls.add_method('DoGetCurrentRealtime', 
                   'uint64_t', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): int64_t ns3::WallClockSynchronizer::DoGetDrift(uint64_t ns) [member function]
    cls.add_method('DoGetDrift', 
                   'int64_t', 
                   [param('uint64_t', 'ns')], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): bool ns3::WallClockSynchronizer::DoRealtime() [member function]
    cls.add_method('DoRealtime', 
                   'bool', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): void ns3::WallClockSynchronizer::DoSetCondition(bool cond) [member function]
    cls.add_method('DoSetCondition', 
                   'void', 
                   [param('bool', 'cond')], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): void ns3::WallClockSynchronizer::DoSetOrigin(uint64_t ns) [member function]
    cls.add_method('DoSetOrigin', 
                   'void', 
                   [param('uint64_t', 'ns')], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): void ns3::WallClockSynchronizer::DoSignal() [member function]
    cls.add_method('DoSignal', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): bool ns3::WallClockSynchronizer::DoSynchronize(uint64_t nsCurrent, uint64_t nsDelay) [member function]
    cls.add_method('DoSynchronize', 
                   'bool', 
                   [param('uint64_t', 'nsCurrent'), param('uint64_t', 'nsDelay')], 
                   visibility='protected', is_virtual=True)
    ## wall-clock-synchronizer.h (module 'core'): uint64_t ns3::WallClockSynchronizer::DriftCorrect(uint64_t nsNow, uint64_t nsDelay) [member function]
    cls.add_method('DriftCorrect', 
                   'uint64_t', 
                   [param('uint64_t', 'nsNow'), param('uint64_t', 'nsDelay')], 
                   visibility='protected')
    ## wall-clock-synchronizer.h (module 'core'): uint64_t ns3::WallClockSynchronizer::GetNormalizedRealtime() [member function]
    cls.add_method('GetNormalizedRealtime', 
                   'uint64_t', 
                   [], 
                   visibility='protected')
    ## wall-clock-synchronizer.h (module 'core'): uint64_t ns3::WallClockSynchronizer::GetRealtime() [member function]
    cls.add_method('GetRealtime', 
                   'uint64_t', 
                   [], 
                   visibility='protected')
    ## wall-clock-synchronizer.h (module 'core'): void ns3::WallClockSynchronizer::NsToTimeval(int64_t ns, timeval * tv) [member function]
    cls.add_method('NsToTimeval', 
                   'void', 
                   [param('int64_t', 'ns'), param('timeval *', 'tv')], 
                   visibility='protected')
    ## wall-clock-synchronizer.h (module 'core'): bool ns3::WallClockSynchronizer::SleepWait(uint64_t ns) [member function]
    cls.add_method('SleepWait', 
                   'bool', 
                   [param('uint64_t', 'ns')], 
                   visibility='protected')
    ## wall-clock-synchronizer.h (module 'core'): bool ns3::WallClockSynchronizer::SpinWait(uint64_t ns) [member function]
    cls.add_method('SpinWait', 
                   'bool', 
                   [param('uint64_t', 'ns')], 
                   visibility='protected')
    ## wall-clock-synchronizer.h (module 'core'): void ns3::WallClockSynchronizer::TimevalAdd(timeval * tv1, timeval * tv2, timeval * result) [member function]
    cls.add_method('TimevalAdd', 
                   'void', 
                   [param('timeval *', 'tv1'), param('timeval *', 'tv2'), param('timeval *', 'result')], 
                   visibility='protected')
    ## wall-clock-synchronizer.h (module 'core'): uint64_t ns3::WallClockSynchronizer::TimevalToNs(timeval * tv) [member function]
    cls.add_method('TimevalToNs', 
                   'uint64_t', 
                   [param('timeval *', 'tv')], 
                   visibility='protected')
    return

def register_Ns3WeibullRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::WeibullRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::WeibullRandomVariable::WeibullRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetScale() const [member function]
    cls.add_method('GetScale', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetShape() const [member function]
    cls.add_method('GetShape', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetValue(double scale, double shape, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'scale'), param('double', 'shape'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::WeibullRandomVariable::GetInteger(uint32_t scale, uint32_t shape, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'scale'), param('uint32_t', 'shape'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::WeibullRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::WeibullRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3WifiInformationElement_methods(root_module, cls):
    cls.add_binary_comparison_operator('<')
    cls.add_binary_comparison_operator('==')
    ## wifi-information-element.h (module 'wifi'): ns3::WifiInformationElement::WifiInformationElement() [constructor]
    cls.add_constructor([])
    ## wifi-information-element.h (module 'wifi'): ns3::WifiInformationElement::WifiInformationElement(ns3::WifiInformationElement const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiInformationElement const &', 'arg0')])
    ## wifi-information-element.h (module 'wifi'): ns3::Buffer::Iterator ns3::WifiInformationElement::Deserialize(ns3::Buffer::Iterator i) [member function]
    cls.add_method('Deserialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'i')])
    ## wifi-information-element.h (module 'wifi'): ns3::Buffer::Iterator ns3::WifiInformationElement::DeserializeIfPresent(ns3::Buffer::Iterator i) [member function]
    cls.add_method('DeserializeIfPresent', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'i')])
    ## wifi-information-element.h (module 'wifi'): uint8_t ns3::WifiInformationElement::DeserializeInformationField(ns3::Buffer::Iterator start, uint8_t length) [member function]
    cls.add_method('DeserializeInformationField', 
                   'uint8_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint8_t', 'length')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-information-element.h (module 'wifi'): ns3::WifiInformationElementId ns3::WifiInformationElement::ElementId() const [member function]
    cls.add_method('ElementId', 
                   'ns3::WifiInformationElementId', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-information-element.h (module 'wifi'): uint8_t ns3::WifiInformationElement::GetInformationFieldSize() const [member function]
    cls.add_method('GetInformationFieldSize', 
                   'uint8_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-information-element.h (module 'wifi'): uint16_t ns3::WifiInformationElement::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-information-element.h (module 'wifi'): void ns3::WifiInformationElement::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## wifi-information-element.h (module 'wifi'): ns3::Buffer::Iterator ns3::WifiInformationElement::Serialize(ns3::Buffer::Iterator i) const [member function]
    cls.add_method('Serialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'i')], 
                   is_const=True)
    ## wifi-information-element.h (module 'wifi'): void ns3::WifiInformationElement::SerializeInformationField(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('SerializeInformationField', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3WifiMac_methods(root_module, cls):
    ## wifi-mac.h (module 'wifi'): ns3::WifiMac::WifiMac() [constructor]
    cls.add_constructor([])
    ## wifi-mac.h (module 'wifi'): ns3::WifiMac::WifiMac(ns3::WifiMac const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiMac const &', 'arg0')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::ConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('ConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Mac48Address ns3::WifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetBasicBlockAckTimeout() const [member function]
    cls.add_method('GetBasicBlockAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Mac48Address ns3::WifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetCompressedBlockAckTimeout() const [member function]
    cls.add_method('GetCompressedBlockAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetMaxPropagationDelay() const [member function]
    cls.add_method('GetMaxPropagationDelay', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetMsduLifetime() const [member function]
    cls.add_method('GetMsduLifetime', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetRifs() const [member function]
    cls.add_method('GetRifs', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Time ns3::WifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Ssid ns3::WifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): static ns3::TypeId ns3::WifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::WifiPhy> ns3::WifiMac::GetWifiPhy() const [member function]
    cls.add_method('GetWifiPhy', 
                   'ns3::Ptr< ns3::WifiPhy >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::WifiRemoteStationManager> ns3::WifiMac::GetWifiRemoteStationManager() const [member function]
    cls.add_method('GetWifiRemoteStationManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): bool ns3::WifiMac::IsRxRadio() [member function]
    cls.add_method('IsRxRadio', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): bool ns3::WifiMac::IsTxRadio() [member function]
    cls.add_method('IsTxRadio', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::NotifyPromiscRx(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyPromiscRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::NotifyRx(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::NotifyRxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::NotifyTx(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::NotifyTxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::ResetWifiPhy() [member function]
    cls.add_method('ResetWifiPhy', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetBasicBlockAckTimeout(ns3::Time blockAckTimeout) [member function]
    cls.add_method('SetBasicBlockAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'blockAckTimeout')], 
                   is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetCompressedBlockAckTimeout(ns3::Time blockAckTimeout) [member function]
    cls.add_method('SetCompressedBlockAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'blockAckTimeout')], 
                   is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetMaxPropagationDelay(ns3::Time delay) [member function]
    cls.add_method('SetMaxPropagationDelay', 
                   'void', 
                   [param('ns3::Time', 'delay')])
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetPromisc() [member function]
    cls.add_method('SetPromisc', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetRifs(ns3::Time rifs) [member function]
    cls.add_method('SetRifs', 
                   'void', 
                   [param('ns3::Time', 'rifs')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetRxRadio(bool isRx, ns3::Ptr<ns3::Node> node, ns3::Ptr<ns3::Repository> repo, ns3::Ptr<ns3::PUModel> puModel, ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetRxRadio', 
                   'void', 
                   [param('bool', 'isRx'), param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::Ptr< ns3::Repository >', 'repo'), param('ns3::Ptr< ns3::PUModel >', 'puModel'), param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetTxRadio(bool isTx) [member function]
    cls.add_method('SetTxRadio', 
                   'void', 
                   [param('bool', 'isTx')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): bool ns3::WifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::ConfigureDcf(ns3::Ptr<ns3::Dcf> dcf, uint32_t cwmin, uint32_t cwmax, ns3::AcIndex ac) [member function]
    cls.add_method('ConfigureDcf', 
                   'void', 
                   [param('ns3::Ptr< ns3::Dcf >', 'dcf'), param('uint32_t', 'cwmin'), param('uint32_t', 'cwmax'), param('ns3::AcIndex', 'ac')], 
                   visibility='protected')
    ## wifi-mac.h (module 'wifi'): void ns3::WifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    return

def register_Ns3WifiMacHeader_methods(root_module, cls):
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacHeader::WifiMacHeader(ns3::WifiMacHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiMacHeader const &', 'arg0')])
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacHeader::WifiMacHeader() [constructor]
    cls.add_constructor([])
    ## wifi-mac-header.h (module 'wifi'): uint32_t ns3::WifiMacHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::Mac48Address ns3::WifiMacHeader::GetAddr1() const [member function]
    cls.add_method('GetAddr1', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::Mac48Address ns3::WifiMacHeader::GetAddr2() const [member function]
    cls.add_method('GetAddr2', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::Mac48Address ns3::WifiMacHeader::GetAddr3() const [member function]
    cls.add_method('GetAddr3', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::Mac48Address ns3::WifiMacHeader::GetAddr4() const [member function]
    cls.add_method('GetAddr4', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::Time ns3::WifiMacHeader::GetDuration() const [member function]
    cls.add_method('GetDuration', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): uint16_t ns3::WifiMacHeader::GetFragmentNumber() const [member function]
    cls.add_method('GetFragmentNumber', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::TypeId ns3::WifiMacHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacHeader::QosAckPolicy ns3::WifiMacHeader::GetQosAckPolicy() const [member function]
    cls.add_method('GetQosAckPolicy', 
                   'ns3::WifiMacHeader::QosAckPolicy', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): uint8_t ns3::WifiMacHeader::GetQosTid() const [member function]
    cls.add_method('GetQosTid', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): uint8_t ns3::WifiMacHeader::GetQosTxopLimit() const [member function]
    cls.add_method('GetQosTxopLimit', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): uint16_t ns3::WifiMacHeader::GetRawDuration() const [member function]
    cls.add_method('GetRawDuration', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): uint16_t ns3::WifiMacHeader::GetSequenceControl() const [member function]
    cls.add_method('GetSequenceControl', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): uint16_t ns3::WifiMacHeader::GetSequenceNumber() const [member function]
    cls.add_method('GetSequenceNumber', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): uint32_t ns3::WifiMacHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h (module 'wifi'): uint32_t ns3::WifiMacHeader::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): ns3::WifiMacType ns3::WifiMacHeader::GetType() const [member function]
    cls.add_method('GetType', 
                   'ns3::WifiMacType', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): static ns3::TypeId ns3::WifiMacHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-mac-header.h (module 'wifi'): char const * ns3::WifiMacHeader::GetTypeString() const [member function]
    cls.add_method('GetTypeString', 
                   'char const *', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsAck() const [member function]
    cls.add_method('IsAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsAction() const [member function]
    cls.add_method('IsAction', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsAssocReq() const [member function]
    cls.add_method('IsAssocReq', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsAssocResp() const [member function]
    cls.add_method('IsAssocResp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsAuthentication() const [member function]
    cls.add_method('IsAuthentication', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsBeacon() const [member function]
    cls.add_method('IsBeacon', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsBlockAck() const [member function]
    cls.add_method('IsBlockAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsBlockAckReq() const [member function]
    cls.add_method('IsBlockAckReq', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsCfpoll() const [member function]
    cls.add_method('IsCfpoll', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsCtl() const [member function]
    cls.add_method('IsCtl', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsCts() const [member function]
    cls.add_method('IsCts', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsData() const [member function]
    cls.add_method('IsData', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsDeauthentication() const [member function]
    cls.add_method('IsDeauthentication', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsDisassociation() const [member function]
    cls.add_method('IsDisassociation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsFromDs() const [member function]
    cls.add_method('IsFromDs', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsMgt() const [member function]
    cls.add_method('IsMgt', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsMoreFragments() const [member function]
    cls.add_method('IsMoreFragments', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsMultihopAction() const [member function]
    cls.add_method('IsMultihopAction', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsProbeReq() const [member function]
    cls.add_method('IsProbeReq', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsProbeResp() const [member function]
    cls.add_method('IsProbeResp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsQosAck() const [member function]
    cls.add_method('IsQosAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsQosAmsdu() const [member function]
    cls.add_method('IsQosAmsdu', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsQosBlockAck() const [member function]
    cls.add_method('IsQosBlockAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsQosData() const [member function]
    cls.add_method('IsQosData', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsQosEosp() const [member function]
    cls.add_method('IsQosEosp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsQosNoAck() const [member function]
    cls.add_method('IsQosNoAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsReassocReq() const [member function]
    cls.add_method('IsReassocReq', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsReassocResp() const [member function]
    cls.add_method('IsReassocResp', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsRetry() const [member function]
    cls.add_method('IsRetry', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsRts() const [member function]
    cls.add_method('IsRts', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): bool ns3::WifiMacHeader::IsToDs() const [member function]
    cls.add_method('IsToDs', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetAction() [member function]
    cls.add_method('SetAction', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetAddr1(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr1', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetAddr2(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr2', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetAddr3(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr3', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetAddr4(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddr4', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetAssocReq() [member function]
    cls.add_method('SetAssocReq', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetAssocResp() [member function]
    cls.add_method('SetAssocResp', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetBeacon() [member function]
    cls.add_method('SetBeacon', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetBlockAck() [member function]
    cls.add_method('SetBlockAck', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetBlockAckReq() [member function]
    cls.add_method('SetBlockAckReq', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetDsFrom() [member function]
    cls.add_method('SetDsFrom', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetDsNotFrom() [member function]
    cls.add_method('SetDsNotFrom', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetDsNotTo() [member function]
    cls.add_method('SetDsNotTo', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetDsTo() [member function]
    cls.add_method('SetDsTo', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetDuration(ns3::Time duration) [member function]
    cls.add_method('SetDuration', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetFragmentNumber(uint8_t frag) [member function]
    cls.add_method('SetFragmentNumber', 
                   'void', 
                   [param('uint8_t', 'frag')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetId(uint16_t id) [member function]
    cls.add_method('SetId', 
                   'void', 
                   [param('uint16_t', 'id')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetMoreFragments() [member function]
    cls.add_method('SetMoreFragments', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetMultihopAction() [member function]
    cls.add_method('SetMultihopAction', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetNoMoreFragments() [member function]
    cls.add_method('SetNoMoreFragments', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetNoOrder() [member function]
    cls.add_method('SetNoOrder', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetNoRetry() [member function]
    cls.add_method('SetNoRetry', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetOrder() [member function]
    cls.add_method('SetOrder', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetProbeReq() [member function]
    cls.add_method('SetProbeReq', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetProbeResp() [member function]
    cls.add_method('SetProbeResp', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosAckPolicy(ns3::WifiMacHeader::QosAckPolicy policy) [member function]
    cls.add_method('SetQosAckPolicy', 
                   'void', 
                   [param('ns3::WifiMacHeader::QosAckPolicy', 'policy')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosAmsdu() [member function]
    cls.add_method('SetQosAmsdu', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosBlockAck() [member function]
    cls.add_method('SetQosBlockAck', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosEosp() [member function]
    cls.add_method('SetQosEosp', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosMeshControlPresent() [member function]
    cls.add_method('SetQosMeshControlPresent', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosNoAck() [member function]
    cls.add_method('SetQosNoAck', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosNoAmsdu() [member function]
    cls.add_method('SetQosNoAmsdu', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosNoEosp() [member function]
    cls.add_method('SetQosNoEosp', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosNoMeshControlPresent() [member function]
    cls.add_method('SetQosNoMeshControlPresent', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosNormalAck() [member function]
    cls.add_method('SetQosNormalAck', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosTid(uint8_t tid) [member function]
    cls.add_method('SetQosTid', 
                   'void', 
                   [param('uint8_t', 'tid')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetQosTxopLimit(uint8_t txop) [member function]
    cls.add_method('SetQosTxopLimit', 
                   'void', 
                   [param('uint8_t', 'txop')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetRawDuration(uint16_t duration) [member function]
    cls.add_method('SetRawDuration', 
                   'void', 
                   [param('uint16_t', 'duration')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetRetry() [member function]
    cls.add_method('SetRetry', 
                   'void', 
                   [])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetSequenceNumber(uint16_t seq) [member function]
    cls.add_method('SetSequenceNumber', 
                   'void', 
                   [param('uint16_t', 'seq')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetType(ns3::WifiMacType type) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::WifiMacType', 'type')])
    ## wifi-mac-header.h (module 'wifi'): void ns3::WifiMacHeader::SetTypeData() [member function]
    cls.add_method('SetTypeData', 
                   'void', 
                   [])
    return

def register_Ns3WifiPhy_methods(root_module, cls):
    ## wifi-phy.h (module 'wifi'): ns3::WifiPhy::WifiPhy(ns3::WifiPhy const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiPhy const &', 'arg0')])
    ## wifi-phy.h (module 'wifi'): ns3::WifiPhy::WifiPhy() [constructor]
    cls.add_constructor([])
    ## wifi-phy.h (module 'wifi'): int64_t ns3::WifiPhy::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::Time ns3::WifiPhy::CalculatePlcpPreambleAndHeaderDuration(ns3::WifiTxVector txVector, ns3::WifiPreamble preamble) [member function]
    cls.add_method('CalculatePlcpPreambleAndHeaderDuration', 
                   'ns3::Time', 
                   [param('ns3::WifiTxVector', 'txVector'), param('ns3::WifiPreamble', 'preamble')])
    ## wifi-phy.h (module 'wifi'): double ns3::WifiPhy::CalculateSnr(ns3::WifiMode txMode, double ber) const [member function]
    cls.add_method('CalculateSnr', 
                   'double', 
                   [param('ns3::WifiMode', 'txMode'), param('double', 'ber')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::Time ns3::WifiPhy::CalculateTxDuration(uint32_t size, ns3::WifiTxVector txVector, ns3::WifiPreamble preamble, double frequency, uint8_t packetType, uint8_t incFlag) [member function]
    cls.add_method('CalculateTxDuration', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WifiTxVector', 'txVector'), param('ns3::WifiPreamble', 'preamble'), param('double', 'frequency'), param('uint8_t', 'packetType'), param('uint8_t', 'incFlag')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::ConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('ConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetBssMembershipSelector(uint32_t selector) const [member function]
    cls.add_method('GetBssMembershipSelector', 
                   'uint32_t', 
                   [param('uint32_t', 'selector')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::Ptr<ns3::WifiChannel> ns3::WifiPhy::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::WifiChannel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint16_t ns3::WifiPhy::GetChannelNumber() const [member function]
    cls.add_method('GetChannelNumber', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::Time ns3::WifiPhy::GetChannelSwitchDelay() const [member function]
    cls.add_method('GetChannelSwitchDelay', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetChannelWidth() const [member function]
    cls.add_method('GetChannelWidth', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::Time ns3::WifiPhy::GetDelayUntilIdle() [member function]
    cls.add_method('GetDelayUntilIdle', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetDsssRate11Mbps() [member function]
    cls.add_method('GetDsssRate11Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetDsssRate1Mbps() [member function]
    cls.add_method('GetDsssRate1Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetDsssRate2Mbps() [member function]
    cls.add_method('GetDsssRate2Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetDsssRate5_5Mbps() [member function]
    cls.add_method('GetDsssRate5_5Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate12Mbps() [member function]
    cls.add_method('GetErpOfdmRate12Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate18Mbps() [member function]
    cls.add_method('GetErpOfdmRate18Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate24Mbps() [member function]
    cls.add_method('GetErpOfdmRate24Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate36Mbps() [member function]
    cls.add_method('GetErpOfdmRate36Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate48Mbps() [member function]
    cls.add_method('GetErpOfdmRate48Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate54Mbps() [member function]
    cls.add_method('GetErpOfdmRate54Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate6Mbps() [member function]
    cls.add_method('GetErpOfdmRate6Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetErpOfdmRate9Mbps() [member function]
    cls.add_method('GetErpOfdmRate9Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetFrequency() const [member function]
    cls.add_method('GetFrequency', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::GetGreenfield() const [member function]
    cls.add_method('GetGreenfield', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::GetGuardInterval() const [member function]
    cls.add_method('GetGuardInterval', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs0() [member function]
    cls.add_method('GetHtMcs0', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs1() [member function]
    cls.add_method('GetHtMcs1', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs10() [member function]
    cls.add_method('GetHtMcs10', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs11() [member function]
    cls.add_method('GetHtMcs11', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs12() [member function]
    cls.add_method('GetHtMcs12', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs13() [member function]
    cls.add_method('GetHtMcs13', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs14() [member function]
    cls.add_method('GetHtMcs14', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs15() [member function]
    cls.add_method('GetHtMcs15', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs16() [member function]
    cls.add_method('GetHtMcs16', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs17() [member function]
    cls.add_method('GetHtMcs17', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs18() [member function]
    cls.add_method('GetHtMcs18', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs19() [member function]
    cls.add_method('GetHtMcs19', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs2() [member function]
    cls.add_method('GetHtMcs2', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs20() [member function]
    cls.add_method('GetHtMcs20', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs21() [member function]
    cls.add_method('GetHtMcs21', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs22() [member function]
    cls.add_method('GetHtMcs22', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs23() [member function]
    cls.add_method('GetHtMcs23', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs24() [member function]
    cls.add_method('GetHtMcs24', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs25() [member function]
    cls.add_method('GetHtMcs25', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs26() [member function]
    cls.add_method('GetHtMcs26', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs27() [member function]
    cls.add_method('GetHtMcs27', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs28() [member function]
    cls.add_method('GetHtMcs28', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs29() [member function]
    cls.add_method('GetHtMcs29', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs3() [member function]
    cls.add_method('GetHtMcs3', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs30() [member function]
    cls.add_method('GetHtMcs30', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs31() [member function]
    cls.add_method('GetHtMcs31', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs4() [member function]
    cls.add_method('GetHtMcs4', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs5() [member function]
    cls.add_method('GetHtMcs5', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs6() [member function]
    cls.add_method('GetHtMcs6', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs7() [member function]
    cls.add_method('GetHtMcs7', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs8() [member function]
    cls.add_method('GetHtMcs8', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtMcs9() [member function]
    cls.add_method('GetHtMcs9', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetHtPlcpHeaderMode(ns3::WifiMode payloadMode) [member function]
    cls.add_method('GetHtPlcpHeaderMode', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiMode', 'payloadMode')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): ns3::Time ns3::WifiPhy::GetLastRxStartTime() const [member function]
    cls.add_method('GetLastRxStartTime', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::GetLdpc() const [member function]
    cls.add_method('GetLdpc', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::WifiMode ns3::WifiPhy::GetMcs(uint8_t mcs) const [member function]
    cls.add_method('GetMcs', 
                   'ns3::WifiMode', 
                   [param('uint8_t', 'mcs')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::WifiModeList ns3::WifiPhy::GetMembershipSelectorModes(uint32_t selector) [member function]
    cls.add_method('GetMembershipSelectorModes', 
                   'ns3::WifiModeList', 
                   [param('uint32_t', 'selector')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): ns3::WifiMode ns3::WifiPhy::GetMode(uint32_t mode) const [member function]
    cls.add_method('GetMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'mode')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetNBssMembershipSelectors() const [member function]
    cls.add_method('GetNBssMembershipSelectors', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint8_t ns3::WifiPhy::GetNMcs() const [member function]
    cls.add_method('GetNMcs', 
                   'uint8_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetNModes() const [member function]
    cls.add_method('GetNModes', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetNTxPower() const [member function]
    cls.add_method('GetNTxPower', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetNumberOfReceiveAntennas() const [member function]
    cls.add_method('GetNumberOfReceiveAntennas', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): uint32_t ns3::WifiPhy::GetNumberOfTransmitAntennas() const [member function]
    cls.add_method('GetNumberOfTransmitAntennas', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate12Mbps() [member function]
    cls.add_method('GetOfdmRate12Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate12MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate12MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate12MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate12MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate13_5MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate13_5MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate18Mbps() [member function]
    cls.add_method('GetOfdmRate18Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate18MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate18MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate1_5MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate1_5MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate24Mbps() [member function]
    cls.add_method('GetOfdmRate24Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate24MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate24MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate27MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate27MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate2_25MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate2_25MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate36Mbps() [member function]
    cls.add_method('GetOfdmRate36Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate3MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate3MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate3MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate3MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate48Mbps() [member function]
    cls.add_method('GetOfdmRate48Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate4_5MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate4_5MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate4_5MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate4_5MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate54Mbps() [member function]
    cls.add_method('GetOfdmRate54Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate6Mbps() [member function]
    cls.add_method('GetOfdmRate6Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate6MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate6MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate6MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate6MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate9Mbps() [member function]
    cls.add_method('GetOfdmRate9Mbps', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate9MbpsBW10MHz() [member function]
    cls.add_method('GetOfdmRate9MbpsBW10MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetOfdmRate9MbpsBW5MHz() [member function]
    cls.add_method('GetOfdmRate9MbpsBW5MHz', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): ns3::Time ns3::WifiPhy::GetPayloadDuration(uint32_t size, ns3::WifiTxVector txVector, ns3::WifiPreamble preamble, double frequency, uint8_t packetType, uint8_t incFlag) [member function]
    cls.add_method('GetPayloadDuration', 
                   'ns3::Time', 
                   [param('uint32_t', 'size'), param('ns3::WifiTxVector', 'txVector'), param('ns3::WifiPreamble', 'preamble'), param('double', 'frequency'), param('uint8_t', 'packetType'), param('uint8_t', 'incFlag')])
    ## wifi-phy.h (module 'wifi'): static ns3::Time ns3::WifiPhy::GetPlcpHeaderDuration(ns3::WifiTxVector txVector, ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpHeaderDuration', 
                   'ns3::Time', 
                   [param('ns3::WifiTxVector', 'txVector'), param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetPlcpHeaderMode(ns3::WifiMode payloadMode, ns3::WifiPreamble preamble, ns3::WifiTxVector txVector) [member function]
    cls.add_method('GetPlcpHeaderMode', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiMode', 'payloadMode'), param('ns3::WifiPreamble', 'preamble'), param('ns3::WifiTxVector', 'txVector')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::Time ns3::WifiPhy::GetPlcpHtSigHeaderDuration(ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpHtSigHeaderDuration', 
                   'ns3::Time', 
                   [param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::Time ns3::WifiPhy::GetPlcpHtTrainingSymbolDuration(ns3::WifiPreamble preamble, ns3::WifiTxVector txVector) [member function]
    cls.add_method('GetPlcpHtTrainingSymbolDuration', 
                   'ns3::Time', 
                   [param('ns3::WifiPreamble', 'preamble'), param('ns3::WifiTxVector', 'txVector')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::Time ns3::WifiPhy::GetPlcpPreambleDuration(ns3::WifiTxVector txVector, ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpPreambleDuration', 
                   'ns3::Time', 
                   [param('ns3::WifiTxVector', 'txVector'), param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::Time ns3::WifiPhy::GetPlcpVhtSigA1Duration(ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpVhtSigA1Duration', 
                   'ns3::Time', 
                   [param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::Time ns3::WifiPhy::GetPlcpVhtSigA2Duration(ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpVhtSigA2Duration', 
                   'ns3::Time', 
                   [param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::Time ns3::WifiPhy::GetPlcpVhtSigBDuration(ns3::WifiPreamble preamble) [member function]
    cls.add_method('GetPlcpVhtSigBDuration', 
                   'ns3::Time', 
                   [param('ns3::WifiPreamble', 'preamble')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): ns3::Time ns3::WifiPhy::GetStateDuration() [member function]
    cls.add_method('GetStateDuration', 
                   'ns3::Time', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::GetStbc() const [member function]
    cls.add_method('GetStbc', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): double ns3::WifiPhy::GetTxPowerEnd() const [member function]
    cls.add_method('GetTxPowerEnd', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): double ns3::WifiPhy::GetTxPowerStart() const [member function]
    cls.add_method('GetTxPowerStart', 
                   'double', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): static ns3::TypeId ns3::WifiPhy::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs0() [member function]
    cls.add_method('GetVhtMcs0', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs1() [member function]
    cls.add_method('GetVhtMcs1', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs2() [member function]
    cls.add_method('GetVhtMcs2', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs3() [member function]
    cls.add_method('GetVhtMcs3', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs4() [member function]
    cls.add_method('GetVhtMcs4', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs5() [member function]
    cls.add_method('GetVhtMcs5', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs6() [member function]
    cls.add_method('GetVhtMcs6', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs7() [member function]
    cls.add_method('GetVhtMcs7', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs8() [member function]
    cls.add_method('GetVhtMcs8', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtMcs9() [member function]
    cls.add_method('GetVhtMcs9', 
                   'ns3::WifiMode', 
                   [], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): static ns3::WifiMode ns3::WifiPhy::GetVhtPlcpHeaderMode(ns3::WifiMode payloadMode) [member function]
    cls.add_method('GetVhtPlcpHeaderMode', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiMode', 'payloadMode')], 
                   is_static=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsModeSupported(ns3::WifiMode mode) const [member function]
    cls.add_method('IsModeSupported', 
                   'bool', 
                   [param('ns3::WifiMode', 'mode')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateBusy() [member function]
    cls.add_method('IsStateBusy', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateCcaBusy() [member function]
    cls.add_method('IsStateCcaBusy', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateIdle() [member function]
    cls.add_method('IsStateIdle', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateRx() [member function]
    cls.add_method('IsStateRx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateSensing() [member function]
    cls.add_method('IsStateSensing', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateSleep() [member function]
    cls.add_method('IsStateSleep', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateSwitching() [member function]
    cls.add_method('IsStateSwitching', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): bool ns3::WifiPhy::IsStateTx() [member function]
    cls.add_method('IsStateTx', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyMonitorSniffRx(ns3::Ptr<ns3::Packet const> packet, uint16_t channelFreqMhz, uint16_t channelNumber, uint32_t rate, ns3::WifiPreamble preamble, ns3::WifiTxVector txVector, ns3::mpduInfo aMpdu, ns3::signalNoiseDbm signalNoise) [member function]
    cls.add_method('NotifyMonitorSniffRx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint16_t', 'channelFreqMhz'), param('uint16_t', 'channelNumber'), param('uint32_t', 'rate'), param('ns3::WifiPreamble', 'preamble'), param('ns3::WifiTxVector', 'txVector'), param('ns3::mpduInfo', 'aMpdu'), param('ns3::signalNoiseDbm', 'signalNoise')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyMonitorSniffTx(ns3::Ptr<ns3::Packet const> packet, uint16_t channelFreqMhz, uint16_t channelNumber, uint32_t rate, ns3::WifiPreamble preamble, ns3::WifiTxVector txVector, ns3::mpduInfo aMpdu) [member function]
    cls.add_method('NotifyMonitorSniffTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint16_t', 'channelFreqMhz'), param('uint16_t', 'channelNumber'), param('uint32_t', 'rate'), param('ns3::WifiPreamble', 'preamble'), param('ns3::WifiTxVector', 'txVector'), param('ns3::mpduInfo', 'aMpdu')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyRxBegin(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyRxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyRxEnd(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyRxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyTxBegin(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxBegin', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyTxDrop(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxDrop', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::NotifyTxEnd(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NotifyTxEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::RegisterListener(ns3::WifiPhyListener * listener) [member function]
    cls.add_method('RegisterListener', 
                   'void', 
                   [param('ns3::WifiPhyListener *', 'listener')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::ResumeFromSleep() [member function]
    cls.add_method('ResumeFromSleep', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SendPacket(ns3::Ptr<ns3::Packet const> packet, ns3::WifiTxVector txVector, ns3::WifiPreamble preamble, uint8_t packetType, uint32_t mpduReferenceNumber) [member function]
    cls.add_method('SendPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiTxVector', 'txVector'), param('ns3::WifiPreamble', 'preamble'), param('uint8_t', 'packetType'), param('uint32_t', 'mpduReferenceNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetChannelNumber(uint16_t id) [member function]
    cls.add_method('SetChannelNumber', 
                   'void', 
                   [param('uint16_t', 'id')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetChannelWidth(uint32_t channelwidth) [member function]
    cls.add_method('SetChannelWidth', 
                   'void', 
                   [param('uint32_t', 'channelwidth')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetFrequency(uint32_t freq) [member function]
    cls.add_method('SetFrequency', 
                   'void', 
                   [param('uint32_t', 'freq')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetGreenfield(bool greenfield) [member function]
    cls.add_method('SetGreenfield', 
                   'void', 
                   [param('bool', 'greenfield')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetGuardInterval(bool guardInterval) [member function]
    cls.add_method('SetGuardInterval', 
                   'void', 
                   [param('bool', 'guardInterval')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetHandoffEndedCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetHandoffEndedCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetLdpc(bool ldpc) [member function]
    cls.add_method('SetLdpc', 
                   'void', 
                   [param('bool', 'ldpc')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetNumberOfReceiveAntennas(uint32_t rx) [member function]
    cls.add_method('SetNumberOfReceiveAntennas', 
                   'void', 
                   [param('uint32_t', 'rx')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetNumberOfTransmitAntennas(uint32_t tx) [member function]
    cls.add_method('SetNumberOfTransmitAntennas', 
                   'void', 
                   [param('uint32_t', 'tx')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetReceiveErrorCallback(ns3::Callback<void,ns3::Ptr<const ns3::Packet>,double,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> callback) [member function]
    cls.add_method('SetReceiveErrorCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet const >, double, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetReceiveOkCallback(ns3::Callback<void,ns3::Ptr<ns3::Packet>,double,ns3::WifiTxVector,ns3::WifiPreamble,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> callback) [member function]
    cls.add_method('SetReceiveOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, double, ns3::WifiTxVector, ns3::WifiPreamble, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetSenseEndedCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetSenseEndedCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetSleepMode() [member function]
    cls.add_method('SetSleepMode', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::SetStbc(bool stbc) [member function]
    cls.add_method('SetStbc', 
                   'void', 
                   [param('bool', 'stbc')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::StartSensing(ns3::Time duration) [member function]
    cls.add_method('StartSensing', 
                   'void', 
                   [param('ns3::Time', 'duration')], 
                   is_pure_virtual=True, is_virtual=True)
    ## wifi-phy.h (module 'wifi'): void ns3::WifiPhy::UnregisterListener(ns3::WifiPhyListener * listener) [member function]
    cls.add_method('UnregisterListener', 
                   'void', 
                   [param('ns3::WifiPhyListener *', 'listener')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3WifiRemoteStationManager_methods(root_module, cls):
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationManager::WifiRemoteStationManager(ns3::WifiRemoteStationManager const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiRemoteStationManager const &', 'arg0')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationManager::WifiRemoteStationManager() [constructor]
    cls.add_constructor([])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::AddAllSupportedModes(ns3::Mac48Address address) [member function]
    cls.add_method('AddAllSupportedModes', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::AddBasicMcs(ns3::WifiMode mcs) [member function]
    cls.add_method('AddBasicMcs', 
                   'void', 
                   [param('ns3::WifiMode', 'mcs')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::AddBasicMode(ns3::WifiMode mode) [member function]
    cls.add_method('AddBasicMode', 
                   'void', 
                   [param('ns3::WifiMode', 'mode')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::AddStationHtCapabilities(ns3::Mac48Address from, ns3::HtCapabilities htcapabilities) [member function]
    cls.add_method('AddStationHtCapabilities', 
                   'void', 
                   [param('ns3::Mac48Address', 'from'), param('ns3::HtCapabilities', 'htcapabilities')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::AddStationVhtCapabilities(ns3::Mac48Address from, ns3::VhtCapabilities vhtcapabilities) [member function]
    cls.add_method('AddStationVhtCapabilities', 
                   'void', 
                   [param('ns3::Mac48Address', 'from'), param('ns3::VhtCapabilities', 'vhtcapabilities')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::AddSupportedMcs(ns3::Mac48Address address, ns3::WifiMode mcs) [member function]
    cls.add_method('AddSupportedMcs', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'mcs')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::AddSupportedMode(ns3::Mac48Address address, ns3::WifiMode mode) [member function]
    cls.add_method('AddSupportedMode', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'mode')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::DoGetCtsToSelfTxVector() [member function]
    cls.add_method('DoGetCtsToSelfTxVector', 
                   'ns3::WifiTxVector', 
                   [])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::GetAckTxVector(ns3::Mac48Address address, ns3::WifiMode dataMode) [member function]
    cls.add_method('GetAckTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'dataMode')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiMode ns3::WifiRemoteStationManager::GetBasicMcs(uint32_t i) const [member function]
    cls.add_method('GetBasicMcs', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiMode ns3::WifiRemoteStationManager::GetBasicMode(uint32_t i) const [member function]
    cls.add_method('GetBasicMode', 
                   'ns3::WifiMode', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::GetBlockAckTxVector(ns3::Mac48Address address, ns3::WifiMode dataMode) [member function]
    cls.add_method('GetBlockAckTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'dataMode')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::GetCtsToSelfTxVector(ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('GetCtsToSelfTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::GetCtsTxVector(ns3::Mac48Address address, ns3::WifiMode rtsMode) [member function]
    cls.add_method('GetCtsTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'rtsMode')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::GetDataTxVector(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet, uint32_t fullPacketSize) [member function]
    cls.add_method('GetDataTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fullPacketSize')])
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiMode ns3::WifiRemoteStationManager::GetDefaultMcs() const [member function]
    cls.add_method('GetDefaultMcs', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiMode ns3::WifiRemoteStationManager::GetDefaultMode() const [member function]
    cls.add_method('GetDefaultMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::GetDefaultTxPowerLevel() const [member function]
    cls.add_method('GetDefaultTxPowerLevel', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetFragmentOffset(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet, uint32_t fragmentNumber) [member function]
    cls.add_method('GetFragmentOffset', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fragmentNumber')])
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetFragmentSize(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet, uint32_t fragmentNumber) [member function]
    cls.add_method('GetFragmentSize', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fragmentNumber')])
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetFragmentationThreshold() const [member function]
    cls.add_method('GetFragmentationThreshold', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::GetGreenfieldSupported(ns3::Mac48Address address) const [member function]
    cls.add_method('GetGreenfieldSupported', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStationInfo ns3::WifiRemoteStationManager::GetInfo(ns3::Mac48Address address) [member function]
    cls.add_method('GetInfo', 
                   'ns3::WifiRemoteStationInfo', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetMaxSlrc() const [member function]
    cls.add_method('GetMaxSlrc', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetMaxSsrc() const [member function]
    cls.add_method('GetMaxSsrc', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNBasicMcs() const [member function]
    cls.add_method('GetNBasicMcs', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNBasicModes() const [member function]
    cls.add_method('GetNBasicModes', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiMode ns3::WifiRemoteStationManager::GetNonUnicastMode() const [member function]
    cls.add_method('GetNonUnicastMode', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNumberOfTransmitAntennas() [member function]
    cls.add_method('GetNumberOfTransmitAntennas', 
                   'uint32_t', 
                   [])
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetRtsCtsThreshold() const [member function]
    cls.add_method('GetRtsCtsThreshold', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::GetRtsTxVector(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('GetRtsTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-remote-station-manager.h (module 'wifi'): static ns3::TypeId ns3::WifiRemoteStationManager::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::HasHtSupported() const [member function]
    cls.add_method('HasHtSupported', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::HasVhtSupported() const [member function]
    cls.add_method('HasVhtSupported', 
                   'bool', 
                   [], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::IsAssociated(ns3::Mac48Address address) const [member function]
    cls.add_method('IsAssociated', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::IsBrandNew(ns3::Mac48Address address) const [member function]
    cls.add_method('IsBrandNew', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::IsLastFragment(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet, uint32_t fragmentNumber) [member function]
    cls.add_method('IsLastFragment', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fragmentNumber')])
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::IsWaitAssocTxOk(ns3::Mac48Address address) const [member function]
    cls.add_method('IsWaitAssocTxOk', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_const=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::NeedCtsToSelf(ns3::WifiTxVector txVector) [member function]
    cls.add_method('NeedCtsToSelf', 
                   'bool', 
                   [param('ns3::WifiTxVector', 'txVector')])
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::NeedDataRetransmission(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedDataRetransmission', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::NeedFragmentation(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedFragmentation', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::NeedRts(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedRts', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::NeedRtsRetransmission(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('NeedRtsRetransmission', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::PrepareForQueue(ns3::Mac48Address address, ns3::WifiMacHeader const * header, ns3::Ptr<ns3::Packet const> packet, uint32_t fullPacketSize) [member function]
    cls.add_method('PrepareForQueue', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('uint32_t', 'fullPacketSize')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::RecordDisassociated(ns3::Mac48Address address) [member function]
    cls.add_method('RecordDisassociated', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::RecordGotAssocTxFailed(ns3::Mac48Address address) [member function]
    cls.add_method('RecordGotAssocTxFailed', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::RecordGotAssocTxOk(ns3::Mac48Address address) [member function]
    cls.add_method('RecordGotAssocTxOk', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::RecordWaitAssocTxOk(ns3::Mac48Address address) [member function]
    cls.add_method('RecordWaitAssocTxOk', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::ReportDataFailed(ns3::Mac48Address address, ns3::WifiMacHeader const * header) [member function]
    cls.add_method('ReportDataFailed', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::ReportDataOk(ns3::Mac48Address address, ns3::WifiMacHeader const * header, double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('ReportDataOk', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::ReportFinalDataFailed(ns3::Mac48Address address, ns3::WifiMacHeader const * header) [member function]
    cls.add_method('ReportFinalDataFailed', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::ReportFinalRtsFailed(ns3::Mac48Address address, ns3::WifiMacHeader const * header) [member function]
    cls.add_method('ReportFinalRtsFailed', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::ReportRtsFailed(ns3::Mac48Address address, ns3::WifiMacHeader const * header) [member function]
    cls.add_method('ReportRtsFailed', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::ReportRtsOk(ns3::Mac48Address address, ns3::WifiMacHeader const * header, double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('ReportRtsOk', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::ReportRxOk(ns3::Mac48Address address, ns3::WifiMacHeader const * header, double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('ReportRxOk', 
                   'void', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMacHeader const *', 'header'), param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::Reset() [member function]
    cls.add_method('Reset', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::Reset(ns3::Mac48Address address) [member function]
    cls.add_method('Reset', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetDefaultTxPowerLevel(uint8_t txPower) [member function]
    cls.add_method('SetDefaultTxPowerLevel', 
                   'void', 
                   [param('uint8_t', 'txPower')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetFragmentationThreshold(uint32_t threshold) [member function]
    cls.add_method('SetFragmentationThreshold', 
                   'void', 
                   [param('uint32_t', 'threshold')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetHtSupported(bool enable) [member function]
    cls.add_method('SetHtSupported', 
                   'void', 
                   [param('bool', 'enable')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetMaxSlrc(uint32_t maxSlrc) [member function]
    cls.add_method('SetMaxSlrc', 
                   'void', 
                   [param('uint32_t', 'maxSlrc')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetMaxSsrc(uint32_t maxSsrc) [member function]
    cls.add_method('SetMaxSsrc', 
                   'void', 
                   [param('uint32_t', 'maxSsrc')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetRtsCtsThreshold(uint32_t threshold) [member function]
    cls.add_method('SetRtsCtsThreshold', 
                   'void', 
                   [param('uint32_t', 'threshold')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetVhtSupported(bool enable) [member function]
    cls.add_method('SetVhtSupported', 
                   'void', 
                   [param('bool', 'enable')])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetupMac(ns3::Ptr<ns3::WifiMac> mac) [member function]
    cls.add_method('SetupMac', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiMac >', 'mac')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::SetupPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetupPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::UpdateFragmentationThreshold() [member function]
    cls.add_method('UpdateFragmentationThreshold', 
                   'void', 
                   [])
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::GetAggregation(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetAggregation', 
                   'bool', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetChannelWidth(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetChannelWidth', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::GetGreenfield(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetGreenfield', 
                   'bool', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetLongRetryCount(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetLongRetryCount', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::Ptr<ns3::WifiMac> ns3::WifiRemoteStationManager::GetMac() const [member function]
    cls.add_method('GetMac', 
                   'ns3::Ptr< ns3::WifiMac >', 
                   [], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiMode ns3::WifiRemoteStationManager::GetMcsSupported(ns3::WifiRemoteStation const * station, uint32_t i) const [member function]
    cls.add_method('GetMcsSupported', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiRemoteStation const *', 'station'), param('uint32_t', 'i')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNMcsSupported(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetNMcsSupported', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNSupported(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetNSupported', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNess(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetNess', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNumberOfReceiveAntennas(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetNumberOfReceiveAntennas', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetNumberOfTransmitAntennas(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetNumberOfTransmitAntennas', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::Ptr<ns3::WifiPhy> ns3::WifiRemoteStationManager::GetPhy() const [member function]
    cls.add_method('GetPhy', 
                   'ns3::Ptr< ns3::WifiPhy >', 
                   [], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::GetShortGuardInterval(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetShortGuardInterval', 
                   'bool', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::GetShortRetryCount(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetShortRetryCount', 
                   'uint32_t', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::GetStbc(ns3::WifiRemoteStation const * station) const [member function]
    cls.add_method('GetStbc', 
                   'bool', 
                   [param('ns3::WifiRemoteStation const *', 'station')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiMode ns3::WifiRemoteStationManager::GetSupported(ns3::WifiRemoteStation const * station, uint32_t i) const [member function]
    cls.add_method('GetSupported', 
                   'ns3::WifiMode', 
                   [param('ns3::WifiRemoteStation const *', 'station'), param('uint32_t', 'i')], 
                   is_const=True, visibility='protected')
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiRemoteStation * ns3::WifiRemoteStationManager::DoCreateStation() const [member function]
    cls.add_method('DoCreateStation', 
                   'ns3::WifiRemoteStation *', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::DoGetAckTxChannelWidth(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetAckTxChannelWidth', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoGetAckTxGuardInterval(ns3::Mac48Address address, ns3::WifiMode ackMode) [member function]
    cls.add_method('DoGetAckTxGuardInterval', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ackMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetAckTxNess(ns3::Mac48Address address, ns3::WifiMode ackMode) [member function]
    cls.add_method('DoGetAckTxNess', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ackMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetAckTxNss(ns3::Mac48Address address, ns3::WifiMode ackMode) [member function]
    cls.add_method('DoGetAckTxNss', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ackMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetAckTxPowerLevel(ns3::Mac48Address address, ns3::WifiMode ackMode) [member function]
    cls.add_method('DoGetAckTxPowerLevel', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ackMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoGetAckTxStbc(ns3::Mac48Address address, ns3::WifiMode ackMode) [member function]
    cls.add_method('DoGetAckTxStbc', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ackMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::DoGetBlockAckTxChannelWidth(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetBlockAckTxChannelWidth', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoGetBlockAckTxGuardInterval(ns3::Mac48Address address, ns3::WifiMode blockAckMode) [member function]
    cls.add_method('DoGetBlockAckTxGuardInterval', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'blockAckMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetBlockAckTxNess(ns3::Mac48Address address, ns3::WifiMode blockAckMode) [member function]
    cls.add_method('DoGetBlockAckTxNess', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'blockAckMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetBlockAckTxNss(ns3::Mac48Address address, ns3::WifiMode blockAckMode) [member function]
    cls.add_method('DoGetBlockAckTxNss', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'blockAckMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetBlockAckTxPowerLevel(ns3::Mac48Address address, ns3::WifiMode blockAckMode) [member function]
    cls.add_method('DoGetBlockAckTxPowerLevel', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'blockAckMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoGetBlockAckTxStbc(ns3::Mac48Address address, ns3::WifiMode blockAckMode) [member function]
    cls.add_method('DoGetBlockAckTxStbc', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'blockAckMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint32_t ns3::WifiRemoteStationManager::DoGetCtsTxChannelWidth(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetCtsTxChannelWidth', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoGetCtsTxGuardInterval(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetCtsTxGuardInterval', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetCtsTxNess(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetCtsTxNess', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetCtsTxNss(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetCtsTxNss', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): uint8_t ns3::WifiRemoteStationManager::DoGetCtsTxPowerLevel(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetCtsTxPowerLevel', 
                   'uint8_t', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoGetCtsTxStbc(ns3::Mac48Address address, ns3::WifiMode ctsMode) [member function]
    cls.add_method('DoGetCtsTxStbc', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('ns3::WifiMode', 'ctsMode')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::DoGetDataTxVector(ns3::WifiRemoteStation * station, uint32_t size) [member function]
    cls.add_method('DoGetDataTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('uint32_t', 'size')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): ns3::WifiTxVector ns3::WifiRemoteStationManager::DoGetRtsTxVector(ns3::WifiRemoteStation * station) [member function]
    cls.add_method('DoGetRtsTxVector', 
                   'ns3::WifiTxVector', 
                   [param('ns3::WifiRemoteStation *', 'station')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoNeedDataRetransmission(ns3::WifiRemoteStation * station, ns3::Ptr<ns3::Packet const> packet, bool normally) [member function]
    cls.add_method('DoNeedDataRetransmission', 
                   'bool', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('bool', 'normally')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoNeedFragmentation(ns3::WifiRemoteStation * station, ns3::Ptr<ns3::Packet const> packet, bool normally) [member function]
    cls.add_method('DoNeedFragmentation', 
                   'bool', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('bool', 'normally')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoNeedRts(ns3::WifiRemoteStation * station, ns3::Ptr<ns3::Packet const> packet, bool normally) [member function]
    cls.add_method('DoNeedRts', 
                   'bool', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('bool', 'normally')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::DoNeedRtsRetransmission(ns3::WifiRemoteStation * station, ns3::Ptr<ns3::Packet const> packet, bool normally) [member function]
    cls.add_method('DoNeedRtsRetransmission', 
                   'bool', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('ns3::Ptr< ns3::Packet const >', 'packet'), param('bool', 'normally')], 
                   visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoReportDataFailed(ns3::WifiRemoteStation * station) [member function]
    cls.add_method('DoReportDataFailed', 
                   'void', 
                   [param('ns3::WifiRemoteStation *', 'station')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoReportDataOk(ns3::WifiRemoteStation * station, double ackSnr, ns3::WifiMode ackMode, double dataSnr) [member function]
    cls.add_method('DoReportDataOk', 
                   'void', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('double', 'ackSnr'), param('ns3::WifiMode', 'ackMode'), param('double', 'dataSnr')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoReportFinalDataFailed(ns3::WifiRemoteStation * station) [member function]
    cls.add_method('DoReportFinalDataFailed', 
                   'void', 
                   [param('ns3::WifiRemoteStation *', 'station')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoReportFinalRtsFailed(ns3::WifiRemoteStation * station) [member function]
    cls.add_method('DoReportFinalRtsFailed', 
                   'void', 
                   [param('ns3::WifiRemoteStation *', 'station')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoReportRtsFailed(ns3::WifiRemoteStation * station) [member function]
    cls.add_method('DoReportRtsFailed', 
                   'void', 
                   [param('ns3::WifiRemoteStation *', 'station')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoReportRtsOk(ns3::WifiRemoteStation * station, double ctsSnr, ns3::WifiMode ctsMode, double rtsSnr) [member function]
    cls.add_method('DoReportRtsOk', 
                   'void', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('double', 'ctsSnr'), param('ns3::WifiMode', 'ctsMode'), param('double', 'rtsSnr')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): void ns3::WifiRemoteStationManager::DoReportRxOk(ns3::WifiRemoteStation * station, double rxSnr, ns3::WifiMode txMode) [member function]
    cls.add_method('DoReportRxOk', 
                   'void', 
                   [param('ns3::WifiRemoteStation *', 'station'), param('double', 'rxSnr'), param('ns3::WifiMode', 'txMode')], 
                   is_pure_virtual=True, visibility='private', is_virtual=True)
    ## wifi-remote-station-manager.h (module 'wifi'): bool ns3::WifiRemoteStationManager::IsLowLatency() const [member function]
    cls.add_method('IsLowLatency', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3ZetaRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ZetaRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ZetaRandomVariable::ZetaRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetValue(double alpha) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'alpha')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZetaRandomVariable::GetInteger(uint32_t alpha) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'alpha')])
    ## random-variable-stream.h (module 'core'): double ns3::ZetaRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZetaRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ZipfRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ZipfRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ZipfRandomVariable::ZipfRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetValue(uint32_t n, double alpha) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('uint32_t', 'n'), param('double', 'alpha')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetInteger(uint32_t n, uint32_t alpha) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'n'), param('uint32_t', 'alpha')])
    ## random-variable-stream.h (module 'core'): double ns3::ZipfRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ZipfRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3AttributeAccessor_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeAccessor::AttributeAccessor(ns3::AttributeAccessor const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeAccessor const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeAccessor::AttributeAccessor() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::Get(ns3::ObjectBase const * object, ns3::AttributeValue & attribute) const [member function]
    cls.add_method('Get', 
                   'bool', 
                   [param('ns3::ObjectBase const *', 'object'), param('ns3::AttributeValue &', 'attribute')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::HasGetter() const [member function]
    cls.add_method('HasGetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::HasSetter() const [member function]
    cls.add_method('HasSetter', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeAccessor::Set(ns3::ObjectBase * object, ns3::AttributeValue const & value) const [member function]
    cls.add_method('Set', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'object', transfer_ownership=False), param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeChecker_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeChecker::AttributeChecker(ns3::AttributeChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeChecker const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeChecker::AttributeChecker() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::Check(ns3::AttributeValue const & value) const [member function]
    cls.add_method('Check', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::Copy(ns3::AttributeValue const & source, ns3::AttributeValue & destination) const [member function]
    cls.add_method('Copy', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'source'), param('ns3::AttributeValue &', 'destination')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeChecker::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeChecker::CreateValidValue(ns3::AttributeValue const & value) const [member function]
    cls.add_method('CreateValidValue', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_const=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeChecker::GetUnderlyingTypeInformation() const [member function]
    cls.add_method('GetUnderlyingTypeInformation', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeChecker::GetValueTypeName() const [member function]
    cls.add_method('GetValueTypeName', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeChecker::HasUnderlyingTypeInformation() const [member function]
    cls.add_method('HasUnderlyingTypeInformation', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3AttributeValue_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::AttributeValue::AttributeValue(ns3::AttributeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AttributeValue const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::AttributeValue::AttributeValue() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::AttributeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::AttributeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::AttributeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3BooleanChecker_methods(root_module, cls):
    ## boolean.h (module 'core'): ns3::BooleanChecker::BooleanChecker() [constructor]
    cls.add_constructor([])
    ## boolean.h (module 'core'): ns3::BooleanChecker::BooleanChecker(ns3::BooleanChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BooleanChecker const &', 'arg0')])
    return

def register_Ns3BooleanValue_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## boolean.h (module 'core'): ns3::BooleanValue::BooleanValue(ns3::BooleanValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::BooleanValue const &', 'arg0')])
    ## boolean.h (module 'core'): ns3::BooleanValue::BooleanValue() [constructor]
    cls.add_constructor([])
    ## boolean.h (module 'core'): ns3::BooleanValue::BooleanValue(bool value) [constructor]
    cls.add_constructor([param('bool', 'value')])
    ## boolean.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::BooleanValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## boolean.h (module 'core'): bool ns3::BooleanValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## boolean.h (module 'core'): bool ns3::BooleanValue::Get() const [member function]
    cls.add_method('Get', 
                   'bool', 
                   [], 
                   is_const=True)
    ## boolean.h (module 'core'): std::string ns3::BooleanValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## boolean.h (module 'core'): void ns3::BooleanValue::Set(bool value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('bool', 'value')])
    return

def register_Ns3CalendarScheduler_methods(root_module, cls):
    ## calendar-scheduler.h (module 'core'): ns3::CalendarScheduler::CalendarScheduler(ns3::CalendarScheduler const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CalendarScheduler const &', 'arg0')])
    ## calendar-scheduler.h (module 'core'): ns3::CalendarScheduler::CalendarScheduler() [constructor]
    cls.add_constructor([])
    ## calendar-scheduler.h (module 'core'): static ns3::TypeId ns3::CalendarScheduler::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## calendar-scheduler.h (module 'core'): void ns3::CalendarScheduler::Insert(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## calendar-scheduler.h (module 'core'): bool ns3::CalendarScheduler::IsEmpty() const [member function]
    cls.add_method('IsEmpty', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## calendar-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::CalendarScheduler::PeekNext() const [member function]
    cls.add_method('PeekNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_const=True, is_virtual=True)
    ## calendar-scheduler.h (module 'core'): void ns3::CalendarScheduler::Remove(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## calendar-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::CalendarScheduler::RemoveNext() [member function]
    cls.add_method('RemoveNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3CallbackChecker_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackChecker::CallbackChecker() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackChecker::CallbackChecker(ns3::CallbackChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackChecker const &', 'arg0')])
    return

def register_Ns3CallbackImplBase_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackImplBase::CallbackImplBase() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackImplBase::CallbackImplBase(ns3::CallbackImplBase const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackImplBase const &', 'arg0')])
    ## callback.h (module 'core'): std::string ns3::CallbackImplBase::GetTypeid() const [member function]
    cls.add_method('GetTypeid', 
                   'std::string', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackImplBase::IsEqual(ns3::Ptr<ns3::CallbackImplBase const> other) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ptr< ns3::CallbackImplBase const >', 'other')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## callback.h (module 'core'): static std::string ns3::CallbackImplBase::Demangle(std::string const & mangled) [member function]
    cls.add_method('Demangle', 
                   'std::string', 
                   [param('std::string const &', 'mangled')], 
                   is_static=True, visibility='protected')
    return

def register_Ns3CallbackValue_methods(root_module, cls):
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue(ns3::CallbackValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CallbackValue const &', 'arg0')])
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue() [constructor]
    cls.add_constructor([])
    ## callback.h (module 'core'): ns3::CallbackValue::CallbackValue(ns3::CallbackBase const & base) [constructor]
    cls.add_constructor([param('ns3::CallbackBase const &', 'base')])
    ## callback.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::CallbackValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): bool ns3::CallbackValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## callback.h (module 'core'): std::string ns3::CallbackValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## callback.h (module 'core'): void ns3::CallbackValue::Set(ns3::CallbackBase base) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::CallbackBase', 'base')])
    return

def register_Ns3ConstantRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ConstantRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ConstantRandomVariable::ConstantRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetConstant() const [member function]
    cls.add_method('GetConstant', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetValue(double constant) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'constant')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ConstantRandomVariable::GetInteger(uint32_t constant) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'constant')])
    ## random-variable-stream.h (module 'core'): double ns3::ConstantRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ConstantRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3CtrlBAckRequestHeader_methods(root_module, cls):
    ## ctrl-headers.h (module 'wifi'): ns3::CtrlBAckRequestHeader::CtrlBAckRequestHeader(ns3::CtrlBAckRequestHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CtrlBAckRequestHeader const &', 'arg0')])
    ## ctrl-headers.h (module 'wifi'): ns3::CtrlBAckRequestHeader::CtrlBAckRequestHeader() [constructor]
    cls.add_constructor([])
    ## ctrl-headers.h (module 'wifi'): uint32_t ns3::CtrlBAckRequestHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): ns3::TypeId ns3::CtrlBAckRequestHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): uint32_t ns3::CtrlBAckRequestHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): uint16_t ns3::CtrlBAckRequestHeader::GetStartingSequence() const [member function]
    cls.add_method('GetStartingSequence', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): uint16_t ns3::CtrlBAckRequestHeader::GetStartingSequenceControl() const [member function]
    cls.add_method('GetStartingSequenceControl', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): uint8_t ns3::CtrlBAckRequestHeader::GetTidInfo() const [member function]
    cls.add_method('GetTidInfo', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): static ns3::TypeId ns3::CtrlBAckRequestHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckRequestHeader::IsBasic() const [member function]
    cls.add_method('IsBasic', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckRequestHeader::IsCompressed() const [member function]
    cls.add_method('IsCompressed', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckRequestHeader::IsMultiTid() const [member function]
    cls.add_method('IsMultiTid', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckRequestHeader::MustSendHtImmediateAck() const [member function]
    cls.add_method('MustSendHtImmediateAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckRequestHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckRequestHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckRequestHeader::SetHtImmediateAck(bool immediateAck) [member function]
    cls.add_method('SetHtImmediateAck', 
                   'void', 
                   [param('bool', 'immediateAck')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckRequestHeader::SetStartingSequence(uint16_t seq) [member function]
    cls.add_method('SetStartingSequence', 
                   'void', 
                   [param('uint16_t', 'seq')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckRequestHeader::SetTidInfo(uint8_t tid) [member function]
    cls.add_method('SetTidInfo', 
                   'void', 
                   [param('uint8_t', 'tid')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckRequestHeader::SetType(ns3::BlockAckType type) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::BlockAckType', 'type')])
    return

def register_Ns3CtrlBAckResponseHeader_methods(root_module, cls):
    ## ctrl-headers.h (module 'wifi'): ns3::CtrlBAckResponseHeader::CtrlBAckResponseHeader(ns3::CtrlBAckResponseHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::CtrlBAckResponseHeader const &', 'arg0')])
    ## ctrl-headers.h (module 'wifi'): ns3::CtrlBAckResponseHeader::CtrlBAckResponseHeader() [constructor]
    cls.add_constructor([])
    ## ctrl-headers.h (module 'wifi'): uint32_t ns3::CtrlBAckResponseHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): uint16_t const * ns3::CtrlBAckResponseHeader::GetBitmap() const [member function]
    cls.add_method('GetBitmap', 
                   'uint16_t const *', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): uint64_t ns3::CtrlBAckResponseHeader::GetCompressedBitmap() const [member function]
    cls.add_method('GetCompressedBitmap', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): ns3::TypeId ns3::CtrlBAckResponseHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): uint32_t ns3::CtrlBAckResponseHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): uint16_t ns3::CtrlBAckResponseHeader::GetStartingSequence() const [member function]
    cls.add_method('GetStartingSequence', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): uint16_t ns3::CtrlBAckResponseHeader::GetStartingSequenceControl() const [member function]
    cls.add_method('GetStartingSequenceControl', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): uint8_t ns3::CtrlBAckResponseHeader::GetTidInfo() const [member function]
    cls.add_method('GetTidInfo', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): static ns3::TypeId ns3::CtrlBAckResponseHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckResponseHeader::IsBasic() const [member function]
    cls.add_method('IsBasic', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckResponseHeader::IsCompressed() const [member function]
    cls.add_method('IsCompressed', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckResponseHeader::IsFragmentReceived(uint16_t seq, uint8_t frag) const [member function]
    cls.add_method('IsFragmentReceived', 
                   'bool', 
                   [param('uint16_t', 'seq'), param('uint8_t', 'frag')], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckResponseHeader::IsMultiTid() const [member function]
    cls.add_method('IsMultiTid', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckResponseHeader::IsPacketReceived(uint16_t seq) const [member function]
    cls.add_method('IsPacketReceived', 
                   'bool', 
                   [param('uint16_t', 'seq')], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): bool ns3::CtrlBAckResponseHeader::MustSendHtImmediateAck() const [member function]
    cls.add_method('MustSendHtImmediateAck', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::ResetBitmap() [member function]
    cls.add_method('ResetBitmap', 
                   'void', 
                   [])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::SetHtImmediateAck(bool immediateAck) [member function]
    cls.add_method('SetHtImmediateAck', 
                   'void', 
                   [param('bool', 'immediateAck')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::SetReceivedFragment(uint16_t seq, uint8_t frag) [member function]
    cls.add_method('SetReceivedFragment', 
                   'void', 
                   [param('uint16_t', 'seq'), param('uint8_t', 'frag')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::SetReceivedPacket(uint16_t seq) [member function]
    cls.add_method('SetReceivedPacket', 
                   'void', 
                   [param('uint16_t', 'seq')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::SetStartingSequence(uint16_t seq) [member function]
    cls.add_method('SetStartingSequence', 
                   'void', 
                   [param('uint16_t', 'seq')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::SetStartingSequenceControl(uint16_t seqControl) [member function]
    cls.add_method('SetStartingSequenceControl', 
                   'void', 
                   [param('uint16_t', 'seqControl')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::SetTidInfo(uint8_t tid) [member function]
    cls.add_method('SetTidInfo', 
                   'void', 
                   [param('uint8_t', 'tid')])
    ## ctrl-headers.h (module 'wifi'): void ns3::CtrlBAckResponseHeader::SetType(ns3::BlockAckType type) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('ns3::BlockAckType', 'type')])
    return

def register_Ns3Dcf_methods(root_module, cls):
    ## dcf.h (module 'wifi'): ns3::Dcf::Dcf() [constructor]
    cls.add_constructor([])
    ## dcf.h (module 'wifi'): ns3::Dcf::Dcf(ns3::Dcf const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Dcf const &', 'arg0')])
    ## dcf.h (module 'wifi'): uint32_t ns3::Dcf::GetAifsn() const [member function]
    cls.add_method('GetAifsn', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## dcf.h (module 'wifi'): uint32_t ns3::Dcf::GetMaxCw() const [member function]
    cls.add_method('GetMaxCw', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## dcf.h (module 'wifi'): uint32_t ns3::Dcf::GetMinCw() const [member function]
    cls.add_method('GetMinCw', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## dcf.h (module 'wifi'): static ns3::TypeId ns3::Dcf::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## dcf.h (module 'wifi'): void ns3::Dcf::SetAifsn(uint32_t aifsn) [member function]
    cls.add_method('SetAifsn', 
                   'void', 
                   [param('uint32_t', 'aifsn')], 
                   is_pure_virtual=True, is_virtual=True)
    ## dcf.h (module 'wifi'): void ns3::Dcf::SetMaxCw(uint32_t maxCw) [member function]
    cls.add_method('SetMaxCw', 
                   'void', 
                   [param('uint32_t', 'maxCw')], 
                   is_pure_virtual=True, is_virtual=True)
    ## dcf.h (module 'wifi'): void ns3::Dcf::SetMinCw(uint32_t minCw) [member function]
    cls.add_method('SetMinCw', 
                   'void', 
                   [param('uint32_t', 'minCw')], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3DefaultSimulatorImpl_methods(root_module, cls):
    ## default-simulator-impl.h (module 'core'): ns3::DefaultSimulatorImpl::DefaultSimulatorImpl(ns3::DefaultSimulatorImpl const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DefaultSimulatorImpl const &', 'arg0')])
    ## default-simulator-impl.h (module 'core'): ns3::DefaultSimulatorImpl::DefaultSimulatorImpl() [constructor]
    cls.add_constructor([])
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::Cancel(ns3::EventId const & id) [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::Destroy() [member function]
    cls.add_method('Destroy', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): uint32_t ns3::DefaultSimulatorImpl::GetContext() const [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## default-simulator-impl.h (module 'core'): ns3::Time ns3::DefaultSimulatorImpl::GetDelayLeft(ns3::EventId const & id) const [member function]
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [param('ns3::EventId const &', 'id')], 
                   is_const=True, is_virtual=True)
    ## default-simulator-impl.h (module 'core'): ns3::Time ns3::DefaultSimulatorImpl::GetMaximumSimulationTime() const [member function]
    cls.add_method('GetMaximumSimulationTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## default-simulator-impl.h (module 'core'): uint32_t ns3::DefaultSimulatorImpl::GetSystemId() const [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## default-simulator-impl.h (module 'core'): static ns3::TypeId ns3::DefaultSimulatorImpl::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## default-simulator-impl.h (module 'core'): bool ns3::DefaultSimulatorImpl::IsExpired(ns3::EventId const & id) const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [param('ns3::EventId const &', 'id')], 
                   is_const=True, is_virtual=True)
    ## default-simulator-impl.h (module 'core'): bool ns3::DefaultSimulatorImpl::IsFinished() const [member function]
    cls.add_method('IsFinished', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## default-simulator-impl.h (module 'core'): ns3::Time ns3::DefaultSimulatorImpl::Now() const [member function]
    cls.add_method('Now', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::Remove(ns3::EventId const & id) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::EventId const &', 'id')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::Run() [member function]
    cls.add_method('Run', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): ns3::EventId ns3::DefaultSimulatorImpl::Schedule(ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('Schedule', 
                   'ns3::EventId', 
                   [param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): ns3::EventId ns3::DefaultSimulatorImpl::ScheduleDestroy(ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleDestroy', 
                   'ns3::EventId', 
                   [param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): ns3::EventId ns3::DefaultSimulatorImpl::ScheduleNow(ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleNow', 
                   'ns3::EventId', 
                   [param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::ScheduleWithContext(uint32_t context, ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleWithContext', 
                   'void', 
                   [param('uint32_t', 'context'), param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::SetScheduler(ns3::ObjectFactory schedulerFactory) [member function]
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::ObjectFactory', 'schedulerFactory')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::Stop() [member function]
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::Stop(ns3::Time const & delay) [member function]
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time const &', 'delay')], 
                   is_virtual=True)
    ## default-simulator-impl.h (module 'core'): void ns3::DefaultSimulatorImpl::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3DeterministicRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::DeterministicRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::DeterministicRandomVariable::DeterministicRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::DeterministicRandomVariable::SetValueArray(double * values, uint64_t length) [member function]
    cls.add_method('SetValueArray', 
                   'void', 
                   [param('double *', 'values'), param('uint64_t', 'length')])
    ## random-variable-stream.h (module 'core'): double ns3::DeterministicRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::DeterministicRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3DoubleValue_methods(root_module, cls):
    ## double.h (module 'core'): ns3::DoubleValue::DoubleValue() [constructor]
    cls.add_constructor([])
    ## double.h (module 'core'): ns3::DoubleValue::DoubleValue(ns3::DoubleValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::DoubleValue const &', 'arg0')])
    ## double.h (module 'core'): ns3::DoubleValue::DoubleValue(double const & value) [constructor]
    cls.add_constructor([param('double const &', 'value')])
    ## double.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::DoubleValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## double.h (module 'core'): bool ns3::DoubleValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## double.h (module 'core'): double ns3::DoubleValue::Get() const [member function]
    cls.add_method('Get', 
                   'double', 
                   [], 
                   is_const=True)
    ## double.h (module 'core'): std::string ns3::DoubleValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## double.h (module 'core'): void ns3::DoubleValue::Set(double const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('double const &', 'value')])
    return

def register_Ns3EdcaTxopN_methods(root_module, cls):
    ## edca-txop-n.h (module 'wifi'): static ns3::TypeId ns3::EdcaTxopN::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## edca-txop-n.h (module 'wifi'): ns3::EdcaTxopN::EdcaTxopN() [constructor]
    cls.add_constructor([])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetLow(ns3::Ptr<ns3::MacLow> low) [member function]
    cls.add_method('SetLow', 
                   'void', 
                   [param('ns3::Ptr< ns3::MacLow >', 'low')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetTxMiddle(ns3::MacTxMiddle * txMiddle) [member function]
    cls.add_method('SetTxMiddle', 
                   'void', 
                   [param('ns3::MacTxMiddle *', 'txMiddle')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetManager(ns3::DcfManager * manager) [member function]
    cls.add_method('SetManager', 
                   'void', 
                   [param('ns3::DcfManager *', 'manager')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetTxOkCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetTxFailedCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxFailedCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> remoteManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'remoteManager')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetTypeOfStation(ns3::TypeOfStation type) [member function]
    cls.add_method('SetTypeOfStation', 
                   'void', 
                   [param('ns3::TypeOfStation', 'type')])
    ## edca-txop-n.h (module 'wifi'): ns3::TypeOfStation ns3::EdcaTxopN::GetTypeOfStation() const [member function]
    cls.add_method('GetTypeOfStation', 
                   'ns3::TypeOfStation', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): ns3::Ptr<ns3::WifiMacQueue> ns3::EdcaTxopN::GetEdcaQueue() const [member function]
    cls.add_method('GetEdcaQueue', 
                   'ns3::Ptr< ns3::WifiMacQueue >', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetMinCw(uint32_t minCw) [member function]
    cls.add_method('SetMinCw', 
                   'void', 
                   [param('uint32_t', 'minCw')], 
                   is_virtual=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetMaxCw(uint32_t maxCw) [member function]
    cls.add_method('SetMaxCw', 
                   'void', 
                   [param('uint32_t', 'maxCw')], 
                   is_virtual=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetAifsn(uint32_t aifsn) [member function]
    cls.add_method('SetAifsn', 
                   'void', 
                   [param('uint32_t', 'aifsn')], 
                   is_virtual=True)
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetMinCw() const [member function]
    cls.add_method('GetMinCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetMaxCw() const [member function]
    cls.add_method('GetMaxCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetAifsn() const [member function]
    cls.add_method('GetAifsn', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## edca-txop-n.h (module 'wifi'): ns3::Ptr<ns3::MacLow> ns3::EdcaTxopN::Low() [member function]
    cls.add_method('Low', 
                   'ns3::Ptr< ns3::MacLow >', 
                   [])
    ## edca-txop-n.h (module 'wifi'): ns3::Ptr<ns3::MsduAggregator> ns3::EdcaTxopN::GetMsduAggregator() const [member function]
    cls.add_method('GetMsduAggregator', 
                   'ns3::Ptr< ns3::MsduAggregator >', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::GetBaAgreementExists(ns3::Mac48Address address, uint8_t tid) [member function]
    cls.add_method('GetBaAgreementExists', 
                   'bool', 
                   [param('ns3::Mac48Address', 'address'), param('uint8_t', 'tid')])
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetNOutstandingPacketsInBa(ns3::Mac48Address address, uint8_t tid) [member function]
    cls.add_method('GetNOutstandingPacketsInBa', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'address'), param('uint8_t', 'tid')])
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetNRetryNeededPackets(ns3::Mac48Address recipient, uint8_t tid) const [member function]
    cls.add_method('GetNRetryNeededPackets', 
                   'uint32_t', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::CompleteAmpduTransfer(ns3::Mac48Address recipient, uint8_t tid) [member function]
    cls.add_method('CompleteAmpduTransfer', 
                   'void', 
                   [param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid')])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::NeedsAccess() const [member function]
    cls.add_method('NeedsAccess', 
                   'bool', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifyAccessGranted() [member function]
    cls.add_method('NotifyAccessGranted', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifyInternalCollision() [member function]
    cls.add_method('NotifyInternalCollision', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifyCollision() [member function]
    cls.add_method('NotifyCollision', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifyChannelSwitching() [member function]
    cls.add_method('NotifyChannelSwitching', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifyChannelSwitching(ns3::Time duration) [member function]
    cls.add_method('NotifyChannelSwitching', 
                   'void', 
                   [param('ns3::Time', 'duration')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifyChannelSensing() [member function]
    cls.add_method('NotifyChannelSensing', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifySleep() [member function]
    cls.add_method('NotifySleep', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NotifyWakeUp() [member function]
    cls.add_method('NotifyWakeUp', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::GotCts(double snr, ns3::WifiMode txMode) [member function]
    cls.add_method('GotCts', 
                   'void', 
                   [param('double', 'snr'), param('ns3::WifiMode', 'txMode')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::MissedCts() [member function]
    cls.add_method('MissedCts', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::GotAck(double snr, ns3::WifiMode txMode) [member function]
    cls.add_method('GotAck', 
                   'void', 
                   [param('double', 'snr'), param('ns3::WifiMode', 'txMode')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::GotBlockAck(ns3::CtrlBAckResponseHeader const * blockAck, ns3::Mac48Address recipient, ns3::WifiMode txMode) [member function]
    cls.add_method('GotBlockAck', 
                   'void', 
                   [param('ns3::CtrlBAckResponseHeader const *', 'blockAck'), param('ns3::Mac48Address', 'recipient'), param('ns3::WifiMode', 'txMode')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::MissedBlockAck() [member function]
    cls.add_method('MissedBlockAck', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::GotAddBaResponse(ns3::MgtAddBaResponseHeader const * respHdr, ns3::Mac48Address recipient) [member function]
    cls.add_method('GotAddBaResponse', 
                   'void', 
                   [param('ns3::MgtAddBaResponseHeader const *', 'respHdr'), param('ns3::Mac48Address', 'recipient')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::GotDelBaFrame(ns3::MgtDelBaHeader const * delBaHdr, ns3::Mac48Address recipient) [member function]
    cls.add_method('GotDelBaFrame', 
                   'void', 
                   [param('ns3::MgtDelBaHeader const *', 'delBaHdr'), param('ns3::Mac48Address', 'recipient')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::MissedAck() [member function]
    cls.add_method('MissedAck', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::StartNext() [member function]
    cls.add_method('StartNext', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::EndTxNoAck() [member function]
    cls.add_method('EndTxNoAck', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::RestartAccessIfNeeded() [member function]
    cls.add_method('RestartAccessIfNeeded', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::StartAccessIfNeeded() [member function]
    cls.add_method('StartAccessIfNeeded', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::NeedRts() [member function]
    cls.add_method('NeedRts', 
                   'bool', 
                   [])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::NeedRtsRetransmission() [member function]
    cls.add_method('NeedRtsRetransmission', 
                   'bool', 
                   [])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::NeedDataRetransmission() [member function]
    cls.add_method('NeedDataRetransmission', 
                   'bool', 
                   [])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::NeedBarRetransmission() [member function]
    cls.add_method('NeedBarRetransmission', 
                   'bool', 
                   [])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::NeedFragmentation() const [member function]
    cls.add_method('NeedFragmentation', 
                   'bool', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetNextFragmentSize() [member function]
    cls.add_method('GetNextFragmentSize', 
                   'uint32_t', 
                   [])
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetFragmentSize() [member function]
    cls.add_method('GetFragmentSize', 
                   'uint32_t', 
                   [])
    ## edca-txop-n.h (module 'wifi'): uint32_t ns3::EdcaTxopN::GetFragmentOffset() [member function]
    cls.add_method('GetFragmentOffset', 
                   'uint32_t', 
                   [])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::IsLastFragment() const [member function]
    cls.add_method('IsLastFragment', 
                   'bool', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::NextFragment() [member function]
    cls.add_method('NextFragment', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): ns3::Ptr<ns3::Packet> ns3::EdcaTxopN::GetFragmentPacket(ns3::WifiMacHeader * hdr) [member function]
    cls.add_method('GetFragmentPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('ns3::WifiMacHeader *', 'hdr')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetAccessCategory(ns3::AcIndex ac) [member function]
    cls.add_method('SetAccessCategory', 
                   'void', 
                   [param('ns3::AcIndex', 'ac')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::Queue(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('Queue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const &', 'hdr')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetMsduAggregator(ns3::Ptr<ns3::MsduAggregator> aggr) [member function]
    cls.add_method('SetMsduAggregator', 
                   'void', 
                   [param('ns3::Ptr< ns3::MsduAggregator >', 'aggr')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::PushFront(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('PushFront', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const &', 'hdr')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::CompleteConfig() [member function]
    cls.add_method('CompleteConfig', 
                   'void', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetBlockAckThreshold(uint8_t threshold) [member function]
    cls.add_method('SetBlockAckThreshold', 
                   'void', 
                   [param('uint8_t', 'threshold')])
    ## edca-txop-n.h (module 'wifi'): uint8_t ns3::EdcaTxopN::GetBlockAckThreshold() const [member function]
    cls.add_method('GetBlockAckThreshold', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetBlockAckInactivityTimeout(uint16_t timeout) [member function]
    cls.add_method('SetBlockAckInactivityTimeout', 
                   'void', 
                   [param('uint16_t', 'timeout')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SendDelbaFrame(ns3::Mac48Address addr, uint8_t tid, bool byOriginator) [member function]
    cls.add_method('SendDelbaFrame', 
                   'void', 
                   [param('ns3::Mac48Address', 'addr'), param('uint8_t', 'tid'), param('bool', 'byOriginator')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::CompleteMpduTx(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader hdr, ns3::Time tstamp) [member function]
    cls.add_method('CompleteMpduTx', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader', 'hdr'), param('ns3::Time', 'tstamp')])
    ## edca-txop-n.h (module 'wifi'): bool ns3::EdcaTxopN::GetAmpduExist() [member function]
    cls.add_method('GetAmpduExist', 
                   'bool', 
                   [])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::SetAmpduExist(bool ampdu) [member function]
    cls.add_method('SetAmpduExist', 
                   'void', 
                   [param('bool', 'ampdu')])
    ## edca-txop-n.h (module 'wifi'): uint16_t ns3::EdcaTxopN::GetNextSequenceNumberfor(ns3::WifiMacHeader * hdr) [member function]
    cls.add_method('GetNextSequenceNumberfor', 
                   'uint16_t', 
                   [param('ns3::WifiMacHeader *', 'hdr')])
    ## edca-txop-n.h (module 'wifi'): uint16_t ns3::EdcaTxopN::PeekNextSequenceNumberfor(ns3::WifiMacHeader * hdr) [member function]
    cls.add_method('PeekNextSequenceNumberfor', 
                   'uint16_t', 
                   [param('ns3::WifiMacHeader *', 'hdr')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::RemoveRetransmitPacket(uint8_t tid, ns3::Mac48Address recipient, uint16_t seqnumber) [member function]
    cls.add_method('RemoveRetransmitPacket', 
                   'void', 
                   [param('uint8_t', 'tid'), param('ns3::Mac48Address', 'recipient'), param('uint16_t', 'seqnumber')])
    ## edca-txop-n.h (module 'wifi'): ns3::Ptr<ns3::Packet const> ns3::EdcaTxopN::PeekNextRetransmitPacket(ns3::WifiMacHeader & header, ns3::Mac48Address recipient, uint8_t tid, ns3::Time * timestamp) [member function]
    cls.add_method('PeekNextRetransmitPacket', 
                   'ns3::Ptr< ns3::Packet const >', 
                   [param('ns3::WifiMacHeader &', 'header'), param('ns3::Mac48Address', 'recipient'), param('uint8_t', 'tid'), param('ns3::Time *', 'timestamp')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::BaTxOk(ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('BaTxOk', 
                   'void', 
                   [param('ns3::WifiMacHeader const &', 'hdr')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::BaTxFailed(ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('BaTxFailed', 
                   'void', 
                   [param('ns3::WifiMacHeader const &', 'hdr')])
    ## edca-txop-n.h (module 'wifi'): int64_t ns3::EdcaTxopN::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')])
    ## edca-txop-n.h (module 'wifi'): void ns3::EdcaTxopN::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3EmpiricalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): ns3::EmpiricalRandomVariable::EmpiricalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): void ns3::EmpiricalRandomVariable::CDF(double v, double c) [member function]
    cls.add_method('CDF', 
                   'void', 
                   [param('double', 'v'), param('double', 'c')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::EmpiricalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::EmpiricalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): double ns3::EmpiricalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): double ns3::EmpiricalRandomVariable::Interpolate(double c1, double c2, double v1, double v2, double r) [member function]
    cls.add_method('Interpolate', 
                   'double', 
                   [param('double', 'c1'), param('double', 'c2'), param('double', 'v1'), param('double', 'v2'), param('double', 'r')], 
                   visibility='private', is_virtual=True)
    ## random-variable-stream.h (module 'core'): void ns3::EmpiricalRandomVariable::Validate() [member function]
    cls.add_method('Validate', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3EmptyAttributeValue_methods(root_module, cls):
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue::EmptyAttributeValue(ns3::EmptyAttributeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EmptyAttributeValue const &', 'arg0')])
    ## attribute.h (module 'core'): ns3::EmptyAttributeValue::EmptyAttributeValue() [constructor]
    cls.add_constructor([])
    ## attribute.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EmptyAttributeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## attribute.h (module 'core'): bool ns3::EmptyAttributeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   visibility='private', is_virtual=True)
    ## attribute.h (module 'core'): std::string ns3::EmptyAttributeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3EnumChecker_methods(root_module, cls):
    ## enum.h (module 'core'): ns3::EnumChecker::EnumChecker(ns3::EnumChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EnumChecker const &', 'arg0')])
    ## enum.h (module 'core'): ns3::EnumChecker::EnumChecker() [constructor]
    cls.add_constructor([])
    ## enum.h (module 'core'): void ns3::EnumChecker::Add(int value, std::string name) [member function]
    cls.add_method('Add', 
                   'void', 
                   [param('int', 'value'), param('std::string', 'name')])
    ## enum.h (module 'core'): void ns3::EnumChecker::AddDefault(int value, std::string name) [member function]
    cls.add_method('AddDefault', 
                   'void', 
                   [param('int', 'value'), param('std::string', 'name')])
    ## enum.h (module 'core'): bool ns3::EnumChecker::Check(ns3::AttributeValue const & value) const [member function]
    cls.add_method('Check', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'value')], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): bool ns3::EnumChecker::Copy(ns3::AttributeValue const & src, ns3::AttributeValue & dst) const [member function]
    cls.add_method('Copy', 
                   'bool', 
                   [param('ns3::AttributeValue const &', 'src'), param('ns3::AttributeValue &', 'dst')], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EnumChecker::Create() const [member function]
    cls.add_method('Create', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): std::string ns3::EnumChecker::GetUnderlyingTypeInformation() const [member function]
    cls.add_method('GetUnderlyingTypeInformation', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): std::string ns3::EnumChecker::GetValueTypeName() const [member function]
    cls.add_method('GetValueTypeName', 
                   'std::string', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): bool ns3::EnumChecker::HasUnderlyingTypeInformation() const [member function]
    cls.add_method('HasUnderlyingTypeInformation', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3EnumValue_methods(root_module, cls):
    ## enum.h (module 'core'): ns3::EnumValue::EnumValue(ns3::EnumValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EnumValue const &', 'arg0')])
    ## enum.h (module 'core'): ns3::EnumValue::EnumValue() [constructor]
    cls.add_constructor([])
    ## enum.h (module 'core'): ns3::EnumValue::EnumValue(int value) [constructor]
    cls.add_constructor([param('int', 'value')])
    ## enum.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::EnumValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): bool ns3::EnumValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## enum.h (module 'core'): int ns3::EnumValue::Get() const [member function]
    cls.add_method('Get', 
                   'int', 
                   [], 
                   is_const=True)
    ## enum.h (module 'core'): std::string ns3::EnumValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## enum.h (module 'core'): void ns3::EnumValue::Set(int value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('int', 'value')])
    return

def register_Ns3ErlangRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ErlangRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ErlangRandomVariable::ErlangRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetK() const [member function]
    cls.add_method('GetK', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetLambda() const [member function]
    cls.add_method('GetLambda', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetValue(uint32_t k, double lambda) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('uint32_t', 'k'), param('double', 'lambda')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetInteger(uint32_t k, uint32_t lambda) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'k'), param('uint32_t', 'lambda')])
    ## random-variable-stream.h (module 'core'): double ns3::ErlangRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ErlangRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3EventImpl_methods(root_module, cls):
    ## event-impl.h (module 'core'): ns3::EventImpl::EventImpl(ns3::EventImpl const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::EventImpl const &', 'arg0')])
    ## event-impl.h (module 'core'): ns3::EventImpl::EventImpl() [constructor]
    cls.add_constructor([])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Cancel() [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Invoke() [member function]
    cls.add_method('Invoke', 
                   'void', 
                   [])
    ## event-impl.h (module 'core'): bool ns3::EventImpl::IsCancelled() [member function]
    cls.add_method('IsCancelled', 
                   'bool', 
                   [])
    ## event-impl.h (module 'core'): void ns3::EventImpl::Notify() [member function]
    cls.add_method('Notify', 
                   'void', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    return

def register_Ns3ExponentialRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ExponentialRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ExponentialRandomVariable::ExponentialRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetValue(double mean, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ExponentialRandomVariable::GetInteger(uint32_t mean, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::ExponentialRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ExponentialRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3FdReader_methods(root_module, cls):
    ## unix-fd-reader.h (module 'core'): ns3::FdReader::FdReader(ns3::FdReader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::FdReader const &', 'arg0')])
    ## unix-fd-reader.h (module 'core'): ns3::FdReader::FdReader() [constructor]
    cls.add_constructor([])
    ## unix-fd-reader.h (module 'core'): void ns3::FdReader::Start(int fd, ns3::Callback<void, unsigned char*, long, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> readCallback) [member function]
    cls.add_method('Start', 
                   'void', 
                   [param('int', 'fd'), param('ns3::Callback< void, unsigned char *, long, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'readCallback')])
    ## unix-fd-reader.h (module 'core'): void ns3::FdReader::Stop() [member function]
    cls.add_method('Stop', 
                   'void', 
                   [])
    ## unix-fd-reader.h (module 'core'): ns3::FdReader::Data ns3::FdReader::DoRead() [member function]
    cls.add_method('DoRead', 
                   'ns3::FdReader::Data', 
                   [], 
                   is_pure_virtual=True, visibility='protected', is_virtual=True)
    return

def register_Ns3GammaRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::GammaRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::GammaRandomVariable::GammaRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetAlpha() const [member function]
    cls.add_method('GetAlpha', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetBeta() const [member function]
    cls.add_method('GetBeta', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetValue(double alpha, double beta) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'alpha'), param('double', 'beta')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::GammaRandomVariable::GetInteger(uint32_t alpha, uint32_t beta) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'alpha'), param('uint32_t', 'beta')])
    ## random-variable-stream.h (module 'core'): double ns3::GammaRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::GammaRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HeapScheduler_methods(root_module, cls):
    ## heap-scheduler.h (module 'core'): ns3::HeapScheduler::HeapScheduler(ns3::HeapScheduler const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::HeapScheduler const &', 'arg0')])
    ## heap-scheduler.h (module 'core'): ns3::HeapScheduler::HeapScheduler() [constructor]
    cls.add_constructor([])
    ## heap-scheduler.h (module 'core'): static ns3::TypeId ns3::HeapScheduler::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## heap-scheduler.h (module 'core'): void ns3::HeapScheduler::Insert(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## heap-scheduler.h (module 'core'): bool ns3::HeapScheduler::IsEmpty() const [member function]
    cls.add_method('IsEmpty', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## heap-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::HeapScheduler::PeekNext() const [member function]
    cls.add_method('PeekNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_const=True, is_virtual=True)
    ## heap-scheduler.h (module 'core'): void ns3::HeapScheduler::Remove(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## heap-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::HeapScheduler::RemoveNext() [member function]
    cls.add_method('RemoveNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HtCapabilities_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilities::HtCapabilities(ns3::HtCapabilities const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::HtCapabilities const &', 'arg0')])
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilities::HtCapabilities() [constructor]
    cls.add_constructor([])
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::DeserializeInformationField(ns3::Buffer::Iterator start, uint8_t length) [member function]
    cls.add_method('DeserializeInformationField', 
                   'uint8_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint8_t', 'length')], 
                   is_virtual=True)
    ## ht-capabilities.h (module 'wifi'): ns3::WifiInformationElementId ns3::HtCapabilities::ElementId() const [member function]
    cls.add_method('ElementId', 
                   'ns3::WifiInformationElementId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetAmpduParameters() const [member function]
    cls.add_method('GetAmpduParameters', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetAntennaSelectionCapabilities() const [member function]
    cls.add_method('GetAntennaSelectionCapabilities', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint16_t ns3::HtCapabilities::GetExtendedHtCapabilities() const [member function]
    cls.add_method('GetExtendedHtCapabilities', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetGreenfield() const [member function]
    cls.add_method('GetGreenfield', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint16_t ns3::HtCapabilities::GetHtCapabilitiesInfo() const [member function]
    cls.add_method('GetHtCapabilitiesInfo', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetInformationFieldSize() const [member function]
    cls.add_method('GetInformationFieldSize', 
                   'uint8_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetLSigProtectionSupport() const [member function]
    cls.add_method('GetLSigProtectionSupport', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetLdpc() const [member function]
    cls.add_method('GetLdpc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetMaxAmpduLength() const [member function]
    cls.add_method('GetMaxAmpduLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetMaxAmsduLength() const [member function]
    cls.add_method('GetMaxAmsduLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint16_t ns3::HtCapabilities::GetRxHighestSupportedDataRate() const [member function]
    cls.add_method('GetRxHighestSupportedDataRate', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t * ns3::HtCapabilities::GetRxMcsBitmask() [member function]
    cls.add_method('GetRxMcsBitmask', 
                   'uint8_t *', 
                   [])
    ## ht-capabilities.h (module 'wifi'): uint16_t ns3::HtCapabilities::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetShortGuardInterval20() const [member function]
    cls.add_method('GetShortGuardInterval20', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetShortGuardInterval40() const [member function]
    cls.add_method('GetShortGuardInterval40', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetSupportedChannelWidth() const [member function]
    cls.add_method('GetSupportedChannelWidth', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint64_t ns3::HtCapabilities::GetSupportedMcsSet1() const [member function]
    cls.add_method('GetSupportedMcsSet1', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint64_t ns3::HtCapabilities::GetSupportedMcsSet2() const [member function]
    cls.add_method('GetSupportedMcsSet2', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint32_t ns3::HtCapabilities::GetTxBfCapabilities() const [member function]
    cls.add_method('GetTxBfCapabilities', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetTxMaxNSpatialStreams() const [member function]
    cls.add_method('GetTxMaxNSpatialStreams', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): uint8_t ns3::HtCapabilities::GetTxMcsSetDefined() const [member function]
    cls.add_method('GetTxMcsSetDefined', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): bool ns3::HtCapabilities::IsSupportedMcs(uint8_t mcs) [member function]
    cls.add_method('IsSupportedMcs', 
                   'bool', 
                   [param('uint8_t', 'mcs')])
    ## ht-capabilities.h (module 'wifi'): ns3::Buffer::Iterator ns3::HtCapabilities::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SerializeInformationField(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('SerializeInformationField', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetAmpduParameters(uint8_t ctrl) [member function]
    cls.add_method('SetAmpduParameters', 
                   'void', 
                   [param('uint8_t', 'ctrl')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetAntennaSelectionCapabilities(uint8_t ctrl) [member function]
    cls.add_method('SetAntennaSelectionCapabilities', 
                   'void', 
                   [param('uint8_t', 'ctrl')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetExtendedHtCapabilities(uint16_t ctrl) [member function]
    cls.add_method('SetExtendedHtCapabilities', 
                   'void', 
                   [param('uint16_t', 'ctrl')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetGreenfield(uint8_t greenfield) [member function]
    cls.add_method('SetGreenfield', 
                   'void', 
                   [param('uint8_t', 'greenfield')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetHtCapabilitiesInfo(uint16_t ctrl) [member function]
    cls.add_method('SetHtCapabilitiesInfo', 
                   'void', 
                   [param('uint16_t', 'ctrl')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetHtSupported(uint8_t htsupported) [member function]
    cls.add_method('SetHtSupported', 
                   'void', 
                   [param('uint8_t', 'htsupported')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetLSigProtectionSupport(uint8_t lsigprotection) [member function]
    cls.add_method('SetLSigProtectionSupport', 
                   'void', 
                   [param('uint8_t', 'lsigprotection')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetLdpc(uint8_t ldpc) [member function]
    cls.add_method('SetLdpc', 
                   'void', 
                   [param('uint8_t', 'ldpc')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetMaxAmpduLength(uint8_t maxampdulength) [member function]
    cls.add_method('SetMaxAmpduLength', 
                   'void', 
                   [param('uint8_t', 'maxampdulength')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetMaxAmsduLength(uint8_t maxamsdulength) [member function]
    cls.add_method('SetMaxAmsduLength', 
                   'void', 
                   [param('uint8_t', 'maxamsdulength')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetRxHighestSupportedDataRate(uint16_t maxsupportedrate) [member function]
    cls.add_method('SetRxHighestSupportedDataRate', 
                   'void', 
                   [param('uint16_t', 'maxsupportedrate')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetRxMcsBitmask(uint8_t index) [member function]
    cls.add_method('SetRxMcsBitmask', 
                   'void', 
                   [param('uint8_t', 'index')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetShortGuardInterval20(uint8_t shortguardinterval) [member function]
    cls.add_method('SetShortGuardInterval20', 
                   'void', 
                   [param('uint8_t', 'shortguardinterval')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetShortGuardInterval40(uint8_t shortguardinterval) [member function]
    cls.add_method('SetShortGuardInterval40', 
                   'void', 
                   [param('uint8_t', 'shortguardinterval')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetSupportedChannelWidth(uint8_t supportedchannelwidth) [member function]
    cls.add_method('SetSupportedChannelWidth', 
                   'void', 
                   [param('uint8_t', 'supportedchannelwidth')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetSupportedMcsSet(uint64_t ctrl1, uint64_t ctrl2) [member function]
    cls.add_method('SetSupportedMcsSet', 
                   'void', 
                   [param('uint64_t', 'ctrl1'), param('uint64_t', 'ctrl2')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetTxBfCapabilities(uint32_t ctrl) [member function]
    cls.add_method('SetTxBfCapabilities', 
                   'void', 
                   [param('uint32_t', 'ctrl')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetTxMaxNSpatialStreams(uint8_t maxtxspatialstreams) [member function]
    cls.add_method('SetTxMaxNSpatialStreams', 
                   'void', 
                   [param('uint8_t', 'maxtxspatialstreams')])
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilities::SetTxMcsSetDefined(uint8_t txmcssetdefined) [member function]
    cls.add_method('SetTxMcsSetDefined', 
                   'void', 
                   [param('uint8_t', 'txmcssetdefined')])
    return

def register_Ns3HtCapabilitiesChecker_methods(root_module, cls):
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilitiesChecker::HtCapabilitiesChecker() [constructor]
    cls.add_constructor([])
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilitiesChecker::HtCapabilitiesChecker(ns3::HtCapabilitiesChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::HtCapabilitiesChecker const &', 'arg0')])
    return

def register_Ns3HtCapabilitiesValue_methods(root_module, cls):
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilitiesValue::HtCapabilitiesValue() [constructor]
    cls.add_constructor([])
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilitiesValue::HtCapabilitiesValue(ns3::HtCapabilitiesValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::HtCapabilitiesValue const &', 'arg0')])
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilitiesValue::HtCapabilitiesValue(ns3::HtCapabilities const & value) [constructor]
    cls.add_constructor([param('ns3::HtCapabilities const &', 'value')])
    ## ht-capabilities.h (module 'wifi'): ns3::Ptr<ns3::AttributeValue> ns3::HtCapabilitiesValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ht-capabilities.h (module 'wifi'): bool ns3::HtCapabilitiesValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ht-capabilities.h (module 'wifi'): ns3::HtCapabilities ns3::HtCapabilitiesValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::HtCapabilities', 
                   [], 
                   is_const=True)
    ## ht-capabilities.h (module 'wifi'): std::string ns3::HtCapabilitiesValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ht-capabilities.h (module 'wifi'): void ns3::HtCapabilitiesValue::Set(ns3::HtCapabilities const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::HtCapabilities const &', 'value')])
    return

def register_Ns3IntegerValue_methods(root_module, cls):
    ## integer.h (module 'core'): ns3::IntegerValue::IntegerValue() [constructor]
    cls.add_constructor([])
    ## integer.h (module 'core'): ns3::IntegerValue::IntegerValue(ns3::IntegerValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::IntegerValue const &', 'arg0')])
    ## integer.h (module 'core'): ns3::IntegerValue::IntegerValue(int64_t const & value) [constructor]
    cls.add_constructor([param('int64_t const &', 'value')])
    ## integer.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::IntegerValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## integer.h (module 'core'): bool ns3::IntegerValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## integer.h (module 'core'): int64_t ns3::IntegerValue::Get() const [member function]
    cls.add_method('Get', 
                   'int64_t', 
                   [], 
                   is_const=True)
    ## integer.h (module 'core'): std::string ns3::IntegerValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## integer.h (module 'core'): void ns3::IntegerValue::Set(int64_t const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('int64_t const &', 'value')])
    return

def register_Ns3Ipv4AddressChecker_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker::Ipv4AddressChecker() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressChecker::Ipv4AddressChecker(ns3::Ipv4AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv4AddressValue_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue(ns3::Ipv4AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4AddressValue const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4AddressValue::Ipv4AddressValue(ns3::Ipv4Address const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv4Address const &', 'value')])
    ## ipv4-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv4AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Address ns3::Ipv4AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): std::string ns3::Ipv4AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4AddressValue::Set(ns3::Ipv4Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Address const &', 'value')])
    return

def register_Ns3Ipv4MaskChecker_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker::Ipv4MaskChecker() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskChecker::Ipv4MaskChecker(ns3::Ipv4MaskChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4MaskChecker const &', 'arg0')])
    return

def register_Ns3Ipv4MaskValue_methods(root_module, cls):
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue() [constructor]
    cls.add_constructor([])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue(ns3::Ipv4MaskValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4MaskValue const &', 'arg0')])
    ## ipv4-address.h (module 'network'): ns3::Ipv4MaskValue::Ipv4MaskValue(ns3::Ipv4Mask const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv4Mask const &', 'value')])
    ## ipv4-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv4MaskValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): bool ns3::Ipv4MaskValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv4-address.h (module 'network'): ns3::Ipv4Mask ns3::Ipv4MaskValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv4Mask', 
                   [], 
                   is_const=True)
    ## ipv4-address.h (module 'network'): std::string ns3::Ipv4MaskValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv4-address.h (module 'network'): void ns3::Ipv4MaskValue::Set(ns3::Ipv4Mask const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv4Mask const &', 'value')])
    return

def register_Ns3Ipv6AddressChecker_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker::Ipv6AddressChecker() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressChecker::Ipv6AddressChecker(ns3::Ipv6AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6AddressChecker const &', 'arg0')])
    return

def register_Ns3Ipv6AddressValue_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue(ns3::Ipv6AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6AddressValue const &', 'arg0')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6AddressValue::Ipv6AddressValue(ns3::Ipv6Address const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address const &', 'value')])
    ## ipv6-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv6AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv6Address ns3::Ipv6AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): std::string ns3::Ipv6AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6AddressValue::Set(ns3::Ipv6Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Address const &', 'value')])
    return

def register_Ns3Ipv6PrefixChecker_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker::Ipv6PrefixChecker() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixChecker::Ipv6PrefixChecker(ns3::Ipv6PrefixChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6PrefixChecker const &', 'arg0')])
    return

def register_Ns3Ipv6PrefixValue_methods(root_module, cls):
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue() [constructor]
    cls.add_constructor([])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue(ns3::Ipv6PrefixValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv6PrefixValue const &', 'arg0')])
    ## ipv6-address.h (module 'network'): ns3::Ipv6PrefixValue::Ipv6PrefixValue(ns3::Ipv6Prefix const & value) [constructor]
    cls.add_constructor([param('ns3::Ipv6Prefix const &', 'value')])
    ## ipv6-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Ipv6PrefixValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): bool ns3::Ipv6PrefixValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ipv6-address.h (module 'network'): ns3::Ipv6Prefix ns3::Ipv6PrefixValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ipv6Prefix', 
                   [], 
                   is_const=True)
    ## ipv6-address.h (module 'network'): std::string ns3::Ipv6PrefixValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ipv6-address.h (module 'network'): void ns3::Ipv6PrefixValue::Set(ns3::Ipv6Prefix const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ipv6Prefix const &', 'value')])
    return

def register_Ns3ListScheduler_methods(root_module, cls):
    ## list-scheduler.h (module 'core'): ns3::ListScheduler::ListScheduler(ns3::ListScheduler const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ListScheduler const &', 'arg0')])
    ## list-scheduler.h (module 'core'): ns3::ListScheduler::ListScheduler() [constructor]
    cls.add_constructor([])
    ## list-scheduler.h (module 'core'): static ns3::TypeId ns3::ListScheduler::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## list-scheduler.h (module 'core'): void ns3::ListScheduler::Insert(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## list-scheduler.h (module 'core'): bool ns3::ListScheduler::IsEmpty() const [member function]
    cls.add_method('IsEmpty', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## list-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::ListScheduler::PeekNext() const [member function]
    cls.add_method('PeekNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_const=True, is_virtual=True)
    ## list-scheduler.h (module 'core'): void ns3::ListScheduler::Remove(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## list-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::ListScheduler::RemoveNext() [member function]
    cls.add_method('RemoveNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3LogNormalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::LogNormalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::LogNormalRandomVariable::LogNormalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetMu() const [member function]
    cls.add_method('GetMu', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetSigma() const [member function]
    cls.add_method('GetSigma', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetValue(double mu, double sigma) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mu'), param('double', 'sigma')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::LogNormalRandomVariable::GetInteger(uint32_t mu, uint32_t sigma) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mu'), param('uint32_t', 'sigma')])
    ## random-variable-stream.h (module 'core'): double ns3::LogNormalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::LogNormalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3Mac48AddressChecker_methods(root_module, cls):
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker::Mac48AddressChecker() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressChecker::Mac48AddressChecker(ns3::Mac48AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Mac48AddressChecker const &', 'arg0')])
    return

def register_Ns3Mac48AddressValue_methods(root_module, cls):
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue() [constructor]
    cls.add_constructor([])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue(ns3::Mac48AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Mac48AddressValue const &', 'arg0')])
    ## mac48-address.h (module 'network'): ns3::Mac48AddressValue::Mac48AddressValue(ns3::Mac48Address const & value) [constructor]
    cls.add_constructor([param('ns3::Mac48Address const &', 'value')])
    ## mac48-address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::Mac48AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## mac48-address.h (module 'network'): bool ns3::Mac48AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## mac48-address.h (module 'network'): ns3::Mac48Address ns3::Mac48AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True)
    ## mac48-address.h (module 'network'): std::string ns3::Mac48AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## mac48-address.h (module 'network'): void ns3::Mac48AddressValue::Set(ns3::Mac48Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Mac48Address const &', 'value')])
    return

def register_Ns3MapScheduler_methods(root_module, cls):
    ## map-scheduler.h (module 'core'): ns3::MapScheduler::MapScheduler(ns3::MapScheduler const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::MapScheduler const &', 'arg0')])
    ## map-scheduler.h (module 'core'): ns3::MapScheduler::MapScheduler() [constructor]
    cls.add_constructor([])
    ## map-scheduler.h (module 'core'): static ns3::TypeId ns3::MapScheduler::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## map-scheduler.h (module 'core'): void ns3::MapScheduler::Insert(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## map-scheduler.h (module 'core'): bool ns3::MapScheduler::IsEmpty() const [member function]
    cls.add_method('IsEmpty', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## map-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::MapScheduler::PeekNext() const [member function]
    cls.add_method('PeekNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_const=True, is_virtual=True)
    ## map-scheduler.h (module 'core'): void ns3::MapScheduler::Remove(ns3::Scheduler::Event const & ev) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::Scheduler::Event const &', 'ev')], 
                   is_virtual=True)
    ## map-scheduler.h (module 'core'): ns3::Scheduler::Event ns3::MapScheduler::RemoveNext() [member function]
    cls.add_method('RemoveNext', 
                   'ns3::Scheduler::Event', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3NetDevice_methods(root_module, cls):
    ## net-device.h (module 'network'): ns3::NetDevice::NetDevice() [constructor]
    cls.add_constructor([])
    ## net-device.h (module 'network'): ns3::NetDevice::NetDevice(ns3::NetDevice const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::NetDevice const &', 'arg0')])
    ## net-device.h (module 'network'): void ns3::NetDevice::AddLinkChangeCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('AddLinkChangeCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetBroadcast() const [member function]
    cls.add_method('GetBroadcast', 
                   'ns3::Address', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Ptr<ns3::Channel> ns3::NetDevice::GetChannel() const [member function]
    cls.add_method('GetChannel', 
                   'ns3::Ptr< ns3::Channel >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): uint32_t ns3::NetDevice::GetIfIndex() const [member function]
    cls.add_method('GetIfIndex', 
                   'uint32_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): uint16_t ns3::NetDevice::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetMulticast(ns3::Ipv4Address multicastGroup) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv4Address', 'multicastGroup')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Address ns3::NetDevice::GetMulticast(ns3::Ipv6Address addr) const [member function]
    cls.add_method('GetMulticast', 
                   'ns3::Address', 
                   [param('ns3::Ipv6Address', 'addr')], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): ns3::Ptr<ns3::Node> ns3::NetDevice::GetNode() const [member function]
    cls.add_method('GetNode', 
                   'ns3::Ptr< ns3::Node >', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): static ns3::TypeId ns3::NetDevice::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsBridge() const [member function]
    cls.add_method('IsBridge', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsLinkUp() const [member function]
    cls.add_method('IsLinkUp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsMulticast() const [member function]
    cls.add_method('IsMulticast', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::IsPointToPoint() const [member function]
    cls.add_method('IsPointToPoint', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::NeedsArp() const [member function]
    cls.add_method('NeedsArp', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::Send(ns3::Ptr<ns3::Packet> packet, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('Send', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SendFrom(ns3::Ptr<ns3::Packet> packet, ns3::Address const & source, ns3::Address const & dest, uint16_t protocolNumber) [member function]
    cls.add_method('SendFrom', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Address const &', 'source'), param('ns3::Address const &', 'dest'), param('uint16_t', 'protocolNumber')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetAddress(ns3::Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'address')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetIfIndex(uint32_t const index) [member function]
    cls.add_method('SetIfIndex', 
                   'void', 
                   [param('uint32_t const', 'index')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SetMtu(uint16_t const mtu) [member function]
    cls.add_method('SetMtu', 
                   'bool', 
                   [param('uint16_t const', 'mtu')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetPromiscReceiveCallback(ns3::Callback<bool,ns3::Ptr<ns3::NetDevice>,ns3::Ptr<const ns3::Packet>,short unsigned int,const ns3::Address&,const ns3::Address&,ns3::NetDevice::PacketType,ns3::empty,ns3::empty,ns3::empty> cb) [member function]
    cls.add_method('SetPromiscReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, short unsigned int, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): void ns3::NetDevice::SetReceiveCallback(ns3::Callback<bool,ns3::Ptr<ns3::NetDevice>,ns3::Ptr<const ns3::Packet>,short unsigned int,const ns3::Address&,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> cb) [member function]
    cls.add_method('SetReceiveCallback', 
                   'void', 
                   [param('ns3::Callback< bool, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, short unsigned int, ns3::Address const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'cb')], 
                   is_pure_virtual=True, is_virtual=True)
    ## net-device.h (module 'network'): bool ns3::NetDevice::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3NixVector_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## nix-vector.h (module 'network'): ns3::NixVector::NixVector() [constructor]
    cls.add_constructor([])
    ## nix-vector.h (module 'network'): ns3::NixVector::NixVector(ns3::NixVector const & o) [copy constructor]
    cls.add_constructor([param('ns3::NixVector const &', 'o')])
    ## nix-vector.h (module 'network'): void ns3::NixVector::AddNeighborIndex(uint32_t newBits, uint32_t numberOfBits) [member function]
    cls.add_method('AddNeighborIndex', 
                   'void', 
                   [param('uint32_t', 'newBits'), param('uint32_t', 'numberOfBits')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::BitCount(uint32_t numberOfNeighbors) const [member function]
    cls.add_method('BitCount', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfNeighbors')], 
                   is_const=True)
    ## nix-vector.h (module 'network'): ns3::Ptr<ns3::NixVector> ns3::NixVector::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::Deserialize(uint32_t const * buffer, uint32_t size) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('uint32_t const *', 'buffer'), param('uint32_t', 'size')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::ExtractNeighborIndex(uint32_t numberOfBits) [member function]
    cls.add_method('ExtractNeighborIndex', 
                   'uint32_t', 
                   [param('uint32_t', 'numberOfBits')])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::GetRemainingBits() [member function]
    cls.add_method('GetRemainingBits', 
                   'uint32_t', 
                   [])
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## nix-vector.h (module 'network'): uint32_t ns3::NixVector::Serialize(uint32_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint32_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    return

def register_Ns3Node_methods(root_module, cls):
    ## node.h (module 'network'): ns3::Node::Node(ns3::Node const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Node const &', 'arg0')])
    ## node.h (module 'network'): ns3::Node::Node() [constructor]
    cls.add_constructor([])
    ## node.h (module 'network'): ns3::Node::Node(uint32_t systemId) [constructor]
    cls.add_constructor([param('uint32_t', 'systemId')])
    ## node.h (module 'network'): uint32_t ns3::Node::AddApplication(ns3::Ptr<ns3::Application> application) [member function]
    cls.add_method('AddApplication', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::Application >', 'application')])
    ## node.h (module 'network'): uint32_t ns3::Node::AddDevice(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('AddDevice', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')])
    ## node.h (module 'network'): static bool ns3::Node::ChecksumEnabled() [member function]
    cls.add_method('ChecksumEnabled', 
                   'bool', 
                   [], 
                   is_static=True)
    ## node.h (module 'network'): ns3::Ptr<ns3::Application> ns3::Node::GetApplication(uint32_t index) const [member function]
    cls.add_method('GetApplication', 
                   'ns3::Ptr< ns3::Application >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    ## node.h (module 'network'): ns3::Ptr<ns3::NetDevice> ns3::Node::GetDevice(uint32_t index) const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'index')], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetId() const [member function]
    cls.add_method('GetId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetNApplications() const [member function]
    cls.add_method('GetNApplications', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetNDevices() const [member function]
    cls.add_method('GetNDevices', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): uint32_t ns3::Node::GetSystemId() const [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## node.h (module 'network'): static ns3::TypeId ns3::Node::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## node.h (module 'network'): bool ns3::Node::IsCognitiveRadio() [member function]
    cls.add_method('IsCognitiveRadio', 
                   'bool', 
                   [])
    ## node.h (module 'network'): void ns3::Node::RegisterDeviceAdditionListener(ns3::Callback<void,ns3::Ptr<ns3::NetDevice>,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> listener) [member function]
    cls.add_method('RegisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    ## node.h (module 'network'): void ns3::Node::RegisterProtocolHandler(ns3::Callback<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> handler, uint16_t protocolType, ns3::Ptr<ns3::NetDevice> device, bool promiscuous=false) [member function]
    cls.add_method('RegisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler'), param('uint16_t', 'protocolType'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('bool', 'promiscuous', default_value='false')])
    ## node.h (module 'network'): void ns3::Node::SetCognitiveRadio(bool isCR) [member function]
    cls.add_method('SetCognitiveRadio', 
                   'void', 
                   [param('bool', 'isCR')])
    ## node.h (module 'network'): void ns3::Node::UnregisterDeviceAdditionListener(ns3::Callback<void,ns3::Ptr<ns3::NetDevice>,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty,ns3::empty> listener) [member function]
    cls.add_method('UnregisterDeviceAdditionListener', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'listener')])
    ## node.h (module 'network'): void ns3::Node::UnregisterProtocolHandler(ns3::Callback<void, ns3::Ptr<ns3::NetDevice>, ns3::Ptr<ns3::Packet const>, unsigned short, ns3::Address const&, ns3::Address const&, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty> handler) [member function]
    cls.add_method('UnregisterProtocolHandler', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::NetDevice >, ns3::Ptr< ns3::Packet const >, unsigned short, ns3::Address const &, ns3::Address const &, ns3::NetDevice::PacketType, ns3::empty, ns3::empty, ns3::empty >', 'handler')])
    ## node.h (module 'network'): void ns3::Node::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## node.h (module 'network'): void ns3::Node::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3NormalRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable::INFINITE_VALUE [variable]
    cls.add_static_attribute('INFINITE_VALUE', 'double const', is_const=True)
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::NormalRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::NormalRandomVariable::NormalRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetVariance() const [member function]
    cls.add_method('GetVariance', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetValue(double mean, double variance, double bound=ns3::NormalRandomVariable::INFINITE_VALUE) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'variance'), param('double', 'bound', default_value='ns3::NormalRandomVariable::INFINITE_VALUE')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::NormalRandomVariable::GetInteger(uint32_t mean, uint32_t variance, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'variance'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::NormalRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::NormalRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3ObjectFactoryChecker_methods(root_module, cls):
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker::ObjectFactoryChecker() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryChecker::ObjectFactoryChecker(ns3::ObjectFactoryChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectFactoryChecker const &', 'arg0')])
    return

def register_Ns3ObjectFactoryValue_methods(root_module, cls):
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue() [constructor]
    cls.add_constructor([])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue(ns3::ObjectFactoryValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectFactoryValue const &', 'arg0')])
    ## object-factory.h (module 'core'): ns3::ObjectFactoryValue::ObjectFactoryValue(ns3::ObjectFactory const & value) [constructor]
    cls.add_constructor([param('ns3::ObjectFactory const &', 'value')])
    ## object-factory.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::ObjectFactoryValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object-factory.h (module 'core'): bool ns3::ObjectFactoryValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## object-factory.h (module 'core'): ns3::ObjectFactory ns3::ObjectFactoryValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::ObjectFactory', 
                   [], 
                   is_const=True)
    ## object-factory.h (module 'core'): std::string ns3::ObjectFactoryValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## object-factory.h (module 'core'): void ns3::ObjectFactoryValue::Set(ns3::ObjectFactory const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::ObjectFactory const &', 'value')])
    return

def register_Ns3ObjectPtrContainerAccessor_methods(root_module, cls):
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerAccessor::ObjectPtrContainerAccessor() [constructor]
    cls.add_constructor([])
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerAccessor::ObjectPtrContainerAccessor(ns3::ObjectPtrContainerAccessor const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectPtrContainerAccessor const &', 'arg0')])
    ## object-ptr-container.h (module 'core'): bool ns3::ObjectPtrContainerAccessor::Get(ns3::ObjectBase const * object, ns3::AttributeValue & value) const [member function]
    cls.add_method('Get', 
                   'bool', 
                   [param('ns3::ObjectBase const *', 'object'), param('ns3::AttributeValue &', 'value')], 
                   is_const=True, is_virtual=True)
    ## object-ptr-container.h (module 'core'): bool ns3::ObjectPtrContainerAccessor::HasGetter() const [member function]
    cls.add_method('HasGetter', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object-ptr-container.h (module 'core'): bool ns3::ObjectPtrContainerAccessor::HasSetter() const [member function]
    cls.add_method('HasSetter', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object-ptr-container.h (module 'core'): bool ns3::ObjectPtrContainerAccessor::Set(ns3::ObjectBase * object, ns3::AttributeValue const & value) const [member function]
    cls.add_method('Set', 
                   'bool', 
                   [param('ns3::ObjectBase *', 'object'), param('ns3::AttributeValue const &', 'value')], 
                   is_const=True, is_virtual=True)
    ## object-ptr-container.h (module 'core'): ns3::Ptr<ns3::Object> ns3::ObjectPtrContainerAccessor::DoGet(ns3::ObjectBase const * object, uint32_t i, uint32_t * index) const [member function]
    cls.add_method('DoGet', 
                   'ns3::Ptr< ns3::Object >', 
                   [param('ns3::ObjectBase const *', 'object'), param('uint32_t', 'i'), param('uint32_t *', 'index')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    ## object-ptr-container.h (module 'core'): bool ns3::ObjectPtrContainerAccessor::DoGetN(ns3::ObjectBase const * object, uint32_t * n) const [member function]
    cls.add_method('DoGetN', 
                   'bool', 
                   [param('ns3::ObjectBase const *', 'object'), param('uint32_t *', 'n')], 
                   is_pure_virtual=True, is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3ObjectPtrContainerChecker_methods(root_module, cls):
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerChecker::ObjectPtrContainerChecker() [constructor]
    cls.add_constructor([])
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerChecker::ObjectPtrContainerChecker(ns3::ObjectPtrContainerChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectPtrContainerChecker const &', 'arg0')])
    ## object-ptr-container.h (module 'core'): ns3::TypeId ns3::ObjectPtrContainerChecker::GetItemTypeId() const [member function]
    cls.add_method('GetItemTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3ObjectPtrContainerValue_methods(root_module, cls):
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerValue::ObjectPtrContainerValue(ns3::ObjectPtrContainerValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ObjectPtrContainerValue const &', 'arg0')])
    ## object-ptr-container.h (module 'core'): ns3::ObjectPtrContainerValue::ObjectPtrContainerValue() [constructor]
    cls.add_constructor([])
    ## object-ptr-container.h (module 'core'): std::_Rb_tree_const_iterator<std::pair<const unsigned int, ns3::Ptr<ns3::Object> > > ns3::ObjectPtrContainerValue::Begin() const [member function]
    cls.add_method('Begin', 
                   'std::_Rb_tree_const_iterator< std::pair< unsigned int const, ns3::Ptr< ns3::Object > > >', 
                   [], 
                   is_const=True)
    ## object-ptr-container.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::ObjectPtrContainerValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## object-ptr-container.h (module 'core'): bool ns3::ObjectPtrContainerValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## object-ptr-container.h (module 'core'): std::_Rb_tree_const_iterator<std::pair<const unsigned int, ns3::Ptr<ns3::Object> > > ns3::ObjectPtrContainerValue::End() const [member function]
    cls.add_method('End', 
                   'std::_Rb_tree_const_iterator< std::pair< unsigned int const, ns3::Ptr< ns3::Object > > >', 
                   [], 
                   is_const=True)
    ## object-ptr-container.h (module 'core'): ns3::Ptr<ns3::Object> ns3::ObjectPtrContainerValue::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Object >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## object-ptr-container.h (module 'core'): uint32_t ns3::ObjectPtrContainerValue::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## object-ptr-container.h (module 'core'): std::string ns3::ObjectPtrContainerValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3Packet_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## packet.h (module 'network'): ns3::Packet::Packet() [constructor]
    cls.add_constructor([])
    ## packet.h (module 'network'): ns3::Packet::Packet(ns3::Packet const & o) [copy constructor]
    cls.add_constructor([param('ns3::Packet const &', 'o')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint32_t size) [constructor]
    cls.add_constructor([param('uint32_t', 'size')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint8_t const * buffer, uint32_t size, bool magic) [constructor]
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size'), param('bool', 'magic')])
    ## packet.h (module 'network'): ns3::Packet::Packet(uint8_t const * buffer, uint32_t size) [constructor]
    cls.add_constructor([param('uint8_t const *', 'buffer'), param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::AddAtEnd(ns3::Ptr<ns3::Packet const> packet) [member function]
    cls.add_method('AddAtEnd', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet')])
    ## packet.h (module 'network'): void ns3::Packet::AddByteTag(ns3::Tag const & tag) const [member function]
    cls.add_method('AddByteTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::AddHeader(ns3::Header const & header) [member function]
    cls.add_method('AddHeader', 
                   'void', 
                   [param('ns3::Header const &', 'header')])
    ## packet.h (module 'network'): void ns3::Packet::AddPacketTag(ns3::Tag const & tag) const [member function]
    cls.add_method('AddPacketTag', 
                   'void', 
                   [param('ns3::Tag const &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::AddPaddingAtEnd(uint32_t size) [member function]
    cls.add_method('AddPaddingAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::AddTrailer(ns3::Trailer const & trailer) [member function]
    cls.add_method('AddTrailer', 
                   'void', 
                   [param('ns3::Trailer const &', 'trailer')])
    ## packet.h (module 'network'): ns3::PacketMetadata::ItemIterator ns3::Packet::BeginItem() const [member function]
    cls.add_method('BeginItem', 
                   'ns3::PacketMetadata::ItemIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Packet::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::CopyData(uint8_t * buffer, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'size')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::CopyData(std::ostream * os, uint32_t size) const [member function]
    cls.add_method('CopyData', 
                   'void', 
                   [param('std::ostream *', 'os'), param('uint32_t', 'size')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::Packet> ns3::Packet::CreateFragment(uint32_t start, uint32_t length) const [member function]
    cls.add_method('CreateFragment', 
                   'ns3::Ptr< ns3::Packet >', 
                   [param('uint32_t', 'start'), param('uint32_t', 'length')], 
                   is_const=True)
    ## packet.h (module 'network'): static void ns3::Packet::EnableChecking() [member function]
    cls.add_method('EnableChecking', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet.h (module 'network'): static void ns3::Packet::EnablePrinting() [member function]
    cls.add_method('EnablePrinting', 
                   'void', 
                   [], 
                   is_static=True)
    ## packet.h (module 'network'): bool ns3::Packet::FindFirstMatchingByteTag(ns3::Tag & tag) const [member function]
    cls.add_method('FindFirstMatchingByteTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::ByteTagIterator ns3::Packet::GetByteTagIterator() const [member function]
    cls.add_method('GetByteTagIterator', 
                   'ns3::ByteTagIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::Ptr<ns3::NixVector> ns3::Packet::GetNixVector() const [member function]
    cls.add_method('GetNixVector', 
                   'ns3::Ptr< ns3::NixVector >', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): ns3::PacketTagIterator ns3::Packet::GetPacketTagIterator() const [member function]
    cls.add_method('GetPacketTagIterator', 
                   'ns3::PacketTagIterator', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::GetSize() const [member function]
    cls.add_method('GetSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint64_t ns3::Packet::GetUid() const [member function]
    cls.add_method('GetUid', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::PeekHeader(ns3::Header & header) const [member function]
    cls.add_method('PeekHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')], 
                   is_const=True)
    ## packet.h (module 'network'): bool ns3::Packet::PeekPacketTag(ns3::Tag & tag) const [member function]
    cls.add_method('PeekPacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')], 
                   is_const=True)
    ## packet.h (module 'network'): uint32_t ns3::Packet::PeekTrailer(ns3::Trailer & trailer) [member function]
    cls.add_method('PeekTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    ## packet.h (module 'network'): void ns3::Packet::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::PrintByteTags(std::ostream & os) const [member function]
    cls.add_method('PrintByteTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::PrintPacketTags(std::ostream & os) const [member function]
    cls.add_method('PrintPacketTags', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::RemoveAllByteTags() [member function]
    cls.add_method('RemoveAllByteTags', 
                   'void', 
                   [])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAllPacketTags() [member function]
    cls.add_method('RemoveAllPacketTags', 
                   'void', 
                   [])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAtEnd(uint32_t size) [member function]
    cls.add_method('RemoveAtEnd', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): void ns3::Packet::RemoveAtStart(uint32_t size) [member function]
    cls.add_method('RemoveAtStart', 
                   'void', 
                   [param('uint32_t', 'size')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::RemoveHeader(ns3::Header & header) [member function]
    cls.add_method('RemoveHeader', 
                   'uint32_t', 
                   [param('ns3::Header &', 'header')])
    ## packet.h (module 'network'): bool ns3::Packet::RemovePacketTag(ns3::Tag & tag) [member function]
    cls.add_method('RemovePacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::RemoveTrailer(ns3::Trailer & trailer) [member function]
    cls.add_method('RemoveTrailer', 
                   'uint32_t', 
                   [param('ns3::Trailer &', 'trailer')])
    ## packet.h (module 'network'): bool ns3::Packet::ReplacePacketTag(ns3::Tag & tag) [member function]
    cls.add_method('ReplacePacketTag', 
                   'bool', 
                   [param('ns3::Tag &', 'tag')])
    ## packet.h (module 'network'): uint32_t ns3::Packet::Serialize(uint8_t * buffer, uint32_t maxSize) const [member function]
    cls.add_method('Serialize', 
                   'uint32_t', 
                   [param('uint8_t *', 'buffer'), param('uint32_t', 'maxSize')], 
                   is_const=True)
    ## packet.h (module 'network'): void ns3::Packet::SetNixVector(ns3::Ptr<ns3::NixVector> nixVector) [member function]
    cls.add_method('SetNixVector', 
                   'void', 
                   [param('ns3::Ptr< ns3::NixVector >', 'nixVector')])
    ## packet.h (module 'network'): std::string ns3::Packet::ToString() const [member function]
    cls.add_method('ToString', 
                   'std::string', 
                   [], 
                   is_const=True)
    return

def register_Ns3ParetoRandomVariable_methods(root_module, cls):
    ## random-variable-stream.h (module 'core'): static ns3::TypeId ns3::ParetoRandomVariable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## random-variable-stream.h (module 'core'): ns3::ParetoRandomVariable::ParetoRandomVariable() [constructor]
    cls.add_constructor([])
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetMean() const [member function]
    cls.add_method('GetMean', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetShape() const [member function]
    cls.add_method('GetShape', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetBound() const [member function]
    cls.add_method('GetBound', 
                   'double', 
                   [], 
                   is_const=True)
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetValue(double mean, double shape, double bound) [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [param('double', 'mean'), param('double', 'shape'), param('double', 'bound')])
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ParetoRandomVariable::GetInteger(uint32_t mean, uint32_t shape, uint32_t bound) [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [param('uint32_t', 'mean'), param('uint32_t', 'shape'), param('uint32_t', 'bound')])
    ## random-variable-stream.h (module 'core'): double ns3::ParetoRandomVariable::GetValue() [member function]
    cls.add_method('GetValue', 
                   'double', 
                   [], 
                   is_virtual=True)
    ## random-variable-stream.h (module 'core'): uint32_t ns3::ParetoRandomVariable::GetInteger() [member function]
    cls.add_method('GetInteger', 
                   'uint32_t', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3PointerChecker_methods(root_module, cls):
    ## pointer.h (module 'core'): ns3::PointerChecker::PointerChecker() [constructor]
    cls.add_constructor([])
    ## pointer.h (module 'core'): ns3::PointerChecker::PointerChecker(ns3::PointerChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PointerChecker const &', 'arg0')])
    ## pointer.h (module 'core'): ns3::TypeId ns3::PointerChecker::GetPointeeTypeId() const [member function]
    cls.add_method('GetPointeeTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    return

def register_Ns3PointerValue_methods(root_module, cls):
    ## pointer.h (module 'core'): ns3::PointerValue::PointerValue(ns3::PointerValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::PointerValue const &', 'arg0')])
    ## pointer.h (module 'core'): ns3::PointerValue::PointerValue() [constructor]
    cls.add_constructor([])
    ## pointer.h (module 'core'): ns3::PointerValue::PointerValue(ns3::Ptr<ns3::Object> object) [constructor]
    cls.add_constructor([param('ns3::Ptr< ns3::Object >', 'object')])
    ## pointer.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::PointerValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## pointer.h (module 'core'): bool ns3::PointerValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## pointer.h (module 'core'): ns3::Ptr<ns3::Object> ns3::PointerValue::GetObject() const [member function]
    cls.add_method('GetObject', 
                   'ns3::Ptr< ns3::Object >', 
                   [], 
                   is_const=True)
    ## pointer.h (module 'core'): std::string ns3::PointerValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## pointer.h (module 'core'): void ns3::PointerValue::SetObject(ns3::Ptr<ns3::Object> object) [member function]
    cls.add_method('SetObject', 
                   'void', 
                   [param('ns3::Ptr< ns3::Object >', 'object')])
    return

def register_Ns3RealtimeSimulatorImpl_methods(root_module, cls):
    ## realtime-simulator-impl.h (module 'core'): ns3::RealtimeSimulatorImpl::RealtimeSimulatorImpl(ns3::RealtimeSimulatorImpl const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RealtimeSimulatorImpl const &', 'arg0')])
    ## realtime-simulator-impl.h (module 'core'): ns3::RealtimeSimulatorImpl::RealtimeSimulatorImpl() [constructor]
    cls.add_constructor([])
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::Cancel(ns3::EventId const & ev) [member function]
    cls.add_method('Cancel', 
                   'void', 
                   [param('ns3::EventId const &', 'ev')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::Destroy() [member function]
    cls.add_method('Destroy', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): uint32_t ns3::RealtimeSimulatorImpl::GetContext() const [member function]
    cls.add_method('GetContext', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::Time ns3::RealtimeSimulatorImpl::GetDelayLeft(ns3::EventId const & id) const [member function]
    cls.add_method('GetDelayLeft', 
                   'ns3::Time', 
                   [param('ns3::EventId const &', 'id')], 
                   is_const=True, is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::Time ns3::RealtimeSimulatorImpl::GetHardLimit() const [member function]
    cls.add_method('GetHardLimit', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::Time ns3::RealtimeSimulatorImpl::GetMaximumSimulationTime() const [member function]
    cls.add_method('GetMaximumSimulationTime', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::RealtimeSimulatorImpl::SynchronizationMode ns3::RealtimeSimulatorImpl::GetSynchronizationMode() const [member function]
    cls.add_method('GetSynchronizationMode', 
                   'ns3::RealtimeSimulatorImpl::SynchronizationMode', 
                   [], 
                   is_const=True)
    ## realtime-simulator-impl.h (module 'core'): uint32_t ns3::RealtimeSimulatorImpl::GetSystemId() const [member function]
    cls.add_method('GetSystemId', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): static ns3::TypeId ns3::RealtimeSimulatorImpl::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## realtime-simulator-impl.h (module 'core'): bool ns3::RealtimeSimulatorImpl::IsExpired(ns3::EventId const & ev) const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [param('ns3::EventId const &', 'ev')], 
                   is_const=True, is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): bool ns3::RealtimeSimulatorImpl::IsFinished() const [member function]
    cls.add_method('IsFinished', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::Time ns3::RealtimeSimulatorImpl::Now() const [member function]
    cls.add_method('Now', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::Time ns3::RealtimeSimulatorImpl::RealtimeNow() const [member function]
    cls.add_method('RealtimeNow', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::Remove(ns3::EventId const & ev) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::EventId const &', 'ev')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::Run() [member function]
    cls.add_method('Run', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::EventId ns3::RealtimeSimulatorImpl::Schedule(ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('Schedule', 
                   'ns3::EventId', 
                   [param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::EventId ns3::RealtimeSimulatorImpl::ScheduleDestroy(ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleDestroy', 
                   'ns3::EventId', 
                   [param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): ns3::EventId ns3::RealtimeSimulatorImpl::ScheduleNow(ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleNow', 
                   'ns3::EventId', 
                   [param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::ScheduleRealtime(ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleRealtime', 
                   'void', 
                   [param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')])
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::ScheduleRealtimeNow(ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleRealtimeNow', 
                   'void', 
                   [param('ns3::EventImpl *', 'event')])
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::ScheduleRealtimeNowWithContext(uint32_t context, ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleRealtimeNowWithContext', 
                   'void', 
                   [param('uint32_t', 'context'), param('ns3::EventImpl *', 'event')])
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::ScheduleRealtimeWithContext(uint32_t context, ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleRealtimeWithContext', 
                   'void', 
                   [param('uint32_t', 'context'), param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')])
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::ScheduleWithContext(uint32_t context, ns3::Time const & delay, ns3::EventImpl * event) [member function]
    cls.add_method('ScheduleWithContext', 
                   'void', 
                   [param('uint32_t', 'context'), param('ns3::Time const &', 'delay'), param('ns3::EventImpl *', 'event')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::SetHardLimit(ns3::Time limit) [member function]
    cls.add_method('SetHardLimit', 
                   'void', 
                   [param('ns3::Time', 'limit')])
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::SetScheduler(ns3::ObjectFactory schedulerFactory) [member function]
    cls.add_method('SetScheduler', 
                   'void', 
                   [param('ns3::ObjectFactory', 'schedulerFactory')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::SetSynchronizationMode(ns3::RealtimeSimulatorImpl::SynchronizationMode mode) [member function]
    cls.add_method('SetSynchronizationMode', 
                   'void', 
                   [param('ns3::RealtimeSimulatorImpl::SynchronizationMode', 'mode')])
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::Stop() [member function]
    cls.add_method('Stop', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::Stop(ns3::Time const & delay) [member function]
    cls.add_method('Stop', 
                   'void', 
                   [param('ns3::Time const &', 'delay')], 
                   is_virtual=True)
    ## realtime-simulator-impl.h (module 'core'): void ns3::RealtimeSimulatorImpl::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3RefCountBase_methods(root_module, cls):
    ## ref-count-base.h (module 'core'): ns3::RefCountBase::RefCountBase() [constructor]
    cls.add_constructor([])
    ## ref-count-base.h (module 'core'): ns3::RefCountBase::RefCountBase(ns3::RefCountBase const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::RefCountBase const &', 'arg0')])
    return

def register_Ns3RegularWifiMac_methods(root_module, cls):
    ## regular-wifi-mac.h (module 'wifi'): static ns3::TypeId ns3::RegularWifiMac::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::RegularWifiMac::RegularWifiMac() [constructor]
    cls.add_constructor([])
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetSlot(ns3::Time slotTime) [member function]
    cls.add_method('SetSlot', 
                   'void', 
                   [param('ns3::Time', 'slotTime')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetSifs(ns3::Time sifs) [member function]
    cls.add_method('SetSifs', 
                   'void', 
                   [param('ns3::Time', 'sifs')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetEifsNoDifs(ns3::Time eifsNoDifs) [member function]
    cls.add_method('SetEifsNoDifs', 
                   'void', 
                   [param('ns3::Time', 'eifsNoDifs')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetPifs(ns3::Time pifs) [member function]
    cls.add_method('SetPifs', 
                   'void', 
                   [param('ns3::Time', 'pifs')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetRifs(ns3::Time rifs) [member function]
    cls.add_method('SetRifs', 
                   'void', 
                   [param('ns3::Time', 'rifs')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetCtsTimeout(ns3::Time ctsTimeout) [member function]
    cls.add_method('SetCtsTimeout', 
                   'void', 
                   [param('ns3::Time', 'ctsTimeout')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetAckTimeout(ns3::Time ackTimeout) [member function]
    cls.add_method('SetAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'ackTimeout')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetRifs() const [member function]
    cls.add_method('GetRifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetPifs() const [member function]
    cls.add_method('GetPifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetSifs() const [member function]
    cls.add_method('GetSifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetSlot() const [member function]
    cls.add_method('GetSlot', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetEifsNoDifs() const [member function]
    cls.add_method('GetEifsNoDifs', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetCtsTimeout() const [member function]
    cls.add_method('GetCtsTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetAckTimeout() const [member function]
    cls.add_method('GetAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetCtsToSelfSupported(bool enable) [member function]
    cls.add_method('SetCtsToSelfSupported', 
                   'void', 
                   [param('bool', 'enable')])
    ## regular-wifi-mac.h (module 'wifi'): bool ns3::RegularWifiMac::GetCtsToSelfSupported() const [member function]
    cls.add_method('GetCtsToSelfSupported', 
                   'bool', 
                   [], 
                   is_const=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Mac48Address ns3::RegularWifiMac::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ssid ns3::RegularWifiMac::GetSsid() const [member function]
    cls.add_method('GetSsid', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetAddress(ns3::Mac48Address address) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Mac48Address', 'address')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetSsid(ns3::Ssid ssid) [member function]
    cls.add_method('SetSsid', 
                   'void', 
                   [param('ns3::Ssid', 'ssid')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetBssid(ns3::Mac48Address bssid) [member function]
    cls.add_method('SetBssid', 
                   'void', 
                   [param('ns3::Mac48Address', 'bssid')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Mac48Address ns3::RegularWifiMac::GetBssid() const [member function]
    cls.add_method('GetBssid', 
                   'ns3::Mac48Address', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetPromisc() [member function]
    cls.add_method('SetPromisc', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to, ns3::Mac48Address from) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to'), param('ns3::Mac48Address', 'from')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): bool ns3::RegularWifiMac::SupportsSendFrom() const [member function]
    cls.add_method('SupportsSendFrom', 
                   'bool', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::Enqueue(ns3::Ptr<ns3::Packet const> packet, ns3::Mac48Address to) [member function]
    cls.add_method('Enqueue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::Mac48Address', 'to')], 
                   is_pure_virtual=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetWifiPhy(ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetWifiPhy', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::WifiPhy> ns3::RegularWifiMac::GetWifiPhy() const [member function]
    cls.add_method('GetWifiPhy', 
                   'ns3::Ptr< ns3::WifiPhy >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::ResetWifiPhy() [member function]
    cls.add_method('ResetWifiPhy', 
                   'void', 
                   [], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> stationManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'stationManager')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::WifiRemoteStationManager> ns3::RegularWifiMac::GetWifiRemoteStationManager() const [member function]
    cls.add_method('GetWifiRemoteStationManager', 
                   'ns3::Ptr< ns3::WifiRemoteStationManager >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetForwardUpCallback(ns3::Callback<void, ns3::Ptr<ns3::Packet>, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> upCallback) [member function]
    cls.add_method('SetForwardUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::Packet >, ns3::Mac48Address, ns3::Mac48Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'upCallback')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetLinkUpCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkUp) [member function]
    cls.add_method('SetLinkUpCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkUp')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetLinkDownCallback(ns3::Callback<void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> linkDown) [member function]
    cls.add_method('SetLinkDownCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'linkDown')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetBasicBlockAckTimeout(ns3::Time blockAckTimeout) [member function]
    cls.add_method('SetBasicBlockAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'blockAckTimeout')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetBasicBlockAckTimeout() const [member function]
    cls.add_method('GetBasicBlockAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetCompressedBlockAckTimeout(ns3::Time blockAckTimeout) [member function]
    cls.add_method('SetCompressedBlockAckTimeout', 
                   'void', 
                   [param('ns3::Time', 'blockAckTimeout')], 
                   is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Time ns3::RegularWifiMac::GetCompressedBlockAckTimeout() const [member function]
    cls.add_method('GetCompressedBlockAckTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True, is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::RestartAccess() [member function]
    cls.add_method('RestartAccess', 
                   'void', 
                   [])
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::DcaTxop> ns3::RegularWifiMac::GetDcaTxop() const [member function]
    cls.add_method('GetDcaTxop', 
                   'ns3::Ptr< ns3::DcaTxop >', 
                   [], 
                   is_const=True, visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::EdcaTxopN> ns3::RegularWifiMac::GetVOQueue() const [member function]
    cls.add_method('GetVOQueue', 
                   'ns3::Ptr< ns3::EdcaTxopN >', 
                   [], 
                   is_const=True, visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::EdcaTxopN> ns3::RegularWifiMac::GetVIQueue() const [member function]
    cls.add_method('GetVIQueue', 
                   'ns3::Ptr< ns3::EdcaTxopN >', 
                   [], 
                   is_const=True, visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::EdcaTxopN> ns3::RegularWifiMac::GetBEQueue() const [member function]
    cls.add_method('GetBEQueue', 
                   'ns3::Ptr< ns3::EdcaTxopN >', 
                   [], 
                   is_const=True, visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): ns3::Ptr<ns3::EdcaTxopN> ns3::RegularWifiMac::GetBKQueue() const [member function]
    cls.add_method('GetBKQueue', 
                   'ns3::Ptr< ns3::EdcaTxopN >', 
                   [], 
                   is_const=True, visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::FinishConfigureStandard(ns3::WifiPhyStandard standard) [member function]
    cls.add_method('FinishConfigureStandard', 
                   'void', 
                   [param('ns3::WifiPhyStandard', 'standard')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetTypeOfStation(ns3::TypeOfStation type) [member function]
    cls.add_method('SetTypeOfStation', 
                   'void', 
                   [param('ns3::TypeOfStation', 'type')], 
                   visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::Receive(ns3::Ptr<ns3::Packet> packet, ns3::WifiMacHeader const * hdr) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::WifiMacHeader const *', 'hdr')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::TxOk(ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('TxOk', 
                   'void', 
                   [param('ns3::WifiMacHeader const &', 'hdr')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::TxFailed(ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('TxFailed', 
                   'void', 
                   [param('ns3::WifiMacHeader const &', 'hdr')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::ForwardUp(ns3::Ptr<ns3::Packet> packet, ns3::Mac48Address from, ns3::Mac48Address to) [member function]
    cls.add_method('ForwardUp', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Mac48Address', 'from'), param('ns3::Mac48Address', 'to')], 
                   visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::DeaggregateAmsduAndForward(ns3::Ptr<ns3::Packet> aggregatedPacket, ns3::WifiMacHeader const * hdr) [member function]
    cls.add_method('DeaggregateAmsduAndForward', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'aggregatedPacket'), param('ns3::WifiMacHeader const *', 'hdr')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SendAddBaResponse(ns3::MgtAddBaRequestHeader const * reqHdr, ns3::Mac48Address originator) [member function]
    cls.add_method('SendAddBaResponse', 
                   'void', 
                   [param('ns3::MgtAddBaRequestHeader const *', 'reqHdr'), param('ns3::Mac48Address', 'originator')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetQosSupported(bool enable) [member function]
    cls.add_method('SetQosSupported', 
                   'void', 
                   [param('bool', 'enable')], 
                   visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): bool ns3::RegularWifiMac::GetQosSupported() const [member function]
    cls.add_method('GetQosSupported', 
                   'bool', 
                   [], 
                   is_const=True, visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): bool ns3::RegularWifiMac::IsTxRadio() [member function]
    cls.add_method('IsTxRadio', 
                   'bool', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetTxRadio(bool isTx) [member function]
    cls.add_method('SetTxRadio', 
                   'void', 
                   [param('bool', 'isTx')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): bool ns3::RegularWifiMac::IsRxRadio() [member function]
    cls.add_method('IsRxRadio', 
                   'bool', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetRxRadio(bool isRx, ns3::Ptr<ns3::Node> node, ns3::Ptr<ns3::Repository> repo, ns3::Ptr<ns3::PUModel> puModel, ns3::Ptr<ns3::WifiPhy> phy) [member function]
    cls.add_method('SetRxRadio', 
                   'void', 
                   [param('bool', 'isRx'), param('ns3::Ptr< ns3::Node >', 'node'), param('ns3::Ptr< ns3::Repository >', 'repo'), param('ns3::Ptr< ns3::PUModel >', 'puModel'), param('ns3::Ptr< ns3::WifiPhy >', 'phy')], 
                   visibility='protected', is_virtual=True)
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetHtSupported(bool enable) [member function]
    cls.add_method('SetHtSupported', 
                   'void', 
                   [param('bool', 'enable')], 
                   visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): bool ns3::RegularWifiMac::GetHtSupported() const [member function]
    cls.add_method('GetHtSupported', 
                   'bool', 
                   [], 
                   is_const=True, visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): void ns3::RegularWifiMac::SetVhtSupported(bool enable) [member function]
    cls.add_method('SetVhtSupported', 
                   'void', 
                   [param('bool', 'enable')], 
                   visibility='protected')
    ## regular-wifi-mac.h (module 'wifi'): bool ns3::RegularWifiMac::GetVhtSupported() const [member function]
    cls.add_method('GetVhtSupported', 
                   'bool', 
                   [], 
                   is_const=True, visibility='protected')
    return

def register_Ns3Ssid_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## ssid.h (module 'wifi'): ns3::Ssid::Ssid(ns3::Ssid const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ssid const &', 'arg0')])
    ## ssid.h (module 'wifi'): ns3::Ssid::Ssid() [constructor]
    cls.add_constructor([])
    ## ssid.h (module 'wifi'): ns3::Ssid::Ssid(std::string s) [constructor]
    cls.add_constructor([param('std::string', 's')])
    ## ssid.h (module 'wifi'): ns3::Ssid::Ssid(char const * ssid, uint8_t length) [constructor]
    cls.add_constructor([param('char const *', 'ssid'), param('uint8_t', 'length')])
    ## ssid.h (module 'wifi'): uint8_t ns3::Ssid::DeserializeInformationField(ns3::Buffer::Iterator start, uint8_t length) [member function]
    cls.add_method('DeserializeInformationField', 
                   'uint8_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint8_t', 'length')], 
                   is_virtual=True)
    ## ssid.h (module 'wifi'): ns3::WifiInformationElementId ns3::Ssid::ElementId() const [member function]
    cls.add_method('ElementId', 
                   'ns3::WifiInformationElementId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ssid.h (module 'wifi'): uint8_t ns3::Ssid::GetInformationFieldSize() const [member function]
    cls.add_method('GetInformationFieldSize', 
                   'uint8_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ssid.h (module 'wifi'): bool ns3::Ssid::IsBroadcast() const [member function]
    cls.add_method('IsBroadcast', 
                   'bool', 
                   [], 
                   is_const=True)
    ## ssid.h (module 'wifi'): bool ns3::Ssid::IsEqual(ns3::Ssid const & o) const [member function]
    cls.add_method('IsEqual', 
                   'bool', 
                   [param('ns3::Ssid const &', 'o')], 
                   is_const=True)
    ## ssid.h (module 'wifi'): char * ns3::Ssid::PeekString() const [member function]
    cls.add_method('PeekString', 
                   'char *', 
                   [], 
                   is_const=True)
    ## ssid.h (module 'wifi'): void ns3::Ssid::SerializeInformationField(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('SerializeInformationField', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    return

def register_Ns3SsidChecker_methods(root_module, cls):
    ## ssid.h (module 'wifi'): ns3::SsidChecker::SsidChecker() [constructor]
    cls.add_constructor([])
    ## ssid.h (module 'wifi'): ns3::SsidChecker::SsidChecker(ns3::SsidChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SsidChecker const &', 'arg0')])
    return

def register_Ns3SsidValue_methods(root_module, cls):
    ## ssid.h (module 'wifi'): ns3::SsidValue::SsidValue() [constructor]
    cls.add_constructor([])
    ## ssid.h (module 'wifi'): ns3::SsidValue::SsidValue(ns3::SsidValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::SsidValue const &', 'arg0')])
    ## ssid.h (module 'wifi'): ns3::SsidValue::SsidValue(ns3::Ssid const & value) [constructor]
    cls.add_constructor([param('ns3::Ssid const &', 'value')])
    ## ssid.h (module 'wifi'): ns3::Ptr<ns3::AttributeValue> ns3::SsidValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ssid.h (module 'wifi'): bool ns3::SsidValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## ssid.h (module 'wifi'): ns3::Ssid ns3::SsidValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Ssid', 
                   [], 
                   is_const=True)
    ## ssid.h (module 'wifi'): std::string ns3::SsidValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## ssid.h (module 'wifi'): void ns3::SsidValue::Set(ns3::Ssid const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Ssid const &', 'value')])
    return

def register_Ns3StringChecker_methods(root_module, cls):
    ## string.h (module 'core'): ns3::StringChecker::StringChecker() [constructor]
    cls.add_constructor([])
    ## string.h (module 'core'): ns3::StringChecker::StringChecker(ns3::StringChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::StringChecker const &', 'arg0')])
    return

def register_Ns3StringValue_methods(root_module, cls):
    ## string.h (module 'core'): ns3::StringValue::StringValue() [constructor]
    cls.add_constructor([])
    ## string.h (module 'core'): ns3::StringValue::StringValue(ns3::StringValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::StringValue const &', 'arg0')])
    ## string.h (module 'core'): ns3::StringValue::StringValue(std::string const & value) [constructor]
    cls.add_constructor([param('std::string const &', 'value')])
    ## string.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::StringValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## string.h (module 'core'): bool ns3::StringValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## string.h (module 'core'): std::string ns3::StringValue::Get() const [member function]
    cls.add_method('Get', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## string.h (module 'core'): std::string ns3::StringValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## string.h (module 'core'): void ns3::StringValue::Set(std::string const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string const &', 'value')])
    return

def register_Ns3TimeValue_methods(root_module, cls):
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue() [constructor]
    cls.add_constructor([])
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue(ns3::TimeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TimeValue const &', 'arg0')])
    ## nstime.h (module 'core'): ns3::TimeValue::TimeValue(ns3::Time const & value) [constructor]
    cls.add_constructor([param('ns3::Time const &', 'value')])
    ## nstime.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::TimeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## nstime.h (module 'core'): bool ns3::TimeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## nstime.h (module 'core'): ns3::Time ns3::TimeValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## nstime.h (module 'core'): std::string ns3::TimeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## nstime.h (module 'core'): void ns3::TimeValue::Set(ns3::Time const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Time const &', 'value')])
    return

def register_Ns3TypeIdChecker_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeIdChecker::TypeIdChecker() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeIdChecker::TypeIdChecker(ns3::TypeIdChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeIdChecker const &', 'arg0')])
    return

def register_Ns3TypeIdValue_methods(root_module, cls):
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue() [constructor]
    cls.add_constructor([])
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue(ns3::TypeIdValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TypeIdValue const &', 'arg0')])
    ## type-id.h (module 'core'): ns3::TypeIdValue::TypeIdValue(ns3::TypeId const & value) [constructor]
    cls.add_constructor([param('ns3::TypeId const &', 'value')])
    ## type-id.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::TypeIdValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## type-id.h (module 'core'): bool ns3::TypeIdValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## type-id.h (module 'core'): ns3::TypeId ns3::TypeIdValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True)
    ## type-id.h (module 'core'): std::string ns3::TypeIdValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## type-id.h (module 'core'): void ns3::TypeIdValue::Set(ns3::TypeId const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::TypeId const &', 'value')])
    return

def register_Ns3UintegerValue_methods(root_module, cls):
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue() [constructor]
    cls.add_constructor([])
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue(ns3::UintegerValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UintegerValue const &', 'arg0')])
    ## uinteger.h (module 'core'): ns3::UintegerValue::UintegerValue(uint64_t const & value) [constructor]
    cls.add_constructor([param('uint64_t const &', 'value')])
    ## uinteger.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::UintegerValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## uinteger.h (module 'core'): bool ns3::UintegerValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## uinteger.h (module 'core'): uint64_t ns3::UintegerValue::Get() const [member function]
    cls.add_method('Get', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## uinteger.h (module 'core'): std::string ns3::UintegerValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## uinteger.h (module 'core'): void ns3::UintegerValue::Set(uint64_t const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('uint64_t const &', 'value')])
    return

def register_Ns3Vector2DChecker_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector2DChecker::Vector2DChecker() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2DChecker::Vector2DChecker(ns3::Vector2DChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector2DChecker const &', 'arg0')])
    return

def register_Ns3Vector2DValue_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue(ns3::Vector2DValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector2DValue const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector2DValue::Vector2DValue(ns3::Vector2D const & value) [constructor]
    cls.add_constructor([param('ns3::Vector2D const &', 'value')])
    ## vector.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::Vector2DValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): bool ns3::Vector2DValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## vector.h (module 'core'): ns3::Vector2D ns3::Vector2DValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Vector2D', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): std::string ns3::Vector2DValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): void ns3::Vector2DValue::Set(ns3::Vector2D const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Vector2D const &', 'value')])
    return

def register_Ns3Vector3DChecker_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector3DChecker::Vector3DChecker() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3DChecker::Vector3DChecker(ns3::Vector3DChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector3DChecker const &', 'arg0')])
    return

def register_Ns3Vector3DValue_methods(root_module, cls):
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue() [constructor]
    cls.add_constructor([])
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue(ns3::Vector3DValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Vector3DValue const &', 'arg0')])
    ## vector.h (module 'core'): ns3::Vector3DValue::Vector3DValue(ns3::Vector3D const & value) [constructor]
    cls.add_constructor([param('ns3::Vector3D const &', 'value')])
    ## vector.h (module 'core'): ns3::Ptr<ns3::AttributeValue> ns3::Vector3DValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): bool ns3::Vector3DValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## vector.h (module 'core'): ns3::Vector3D ns3::Vector3DValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Vector3D', 
                   [], 
                   is_const=True)
    ## vector.h (module 'core'): std::string ns3::Vector3DValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## vector.h (module 'core'): void ns3::Vector3DValue::Set(ns3::Vector3D const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Vector3D const &', 'value')])
    return

def register_Ns3VhtCapabilities_methods(root_module, cls):
    cls.add_output_stream_operator()
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilities::VhtCapabilities(ns3::VhtCapabilities const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::VhtCapabilities const &', 'arg0')])
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilities::VhtCapabilities() [constructor]
    cls.add_constructor([])
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::DeserializeInformationField(ns3::Buffer::Iterator start, uint8_t length) [member function]
    cls.add_method('DeserializeInformationField', 
                   'uint8_t', 
                   [param('ns3::Buffer::Iterator', 'start'), param('uint8_t', 'length')], 
                   is_virtual=True)
    ## vht-capabilities.h (module 'wifi'): ns3::WifiInformationElementId ns3::VhtCapabilities::ElementId() const [member function]
    cls.add_method('ElementId', 
                   'ns3::WifiInformationElementId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetInformationFieldSize() const [member function]
    cls.add_method('GetInformationFieldSize', 
                   'uint8_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetMaxAmpduLengthExponent() const [member function]
    cls.add_method('GetMaxAmpduLengthExponent', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetMaxMpduLength() const [member function]
    cls.add_method('GetMaxMpduLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint16_t ns3::VhtCapabilities::GetRxHighestSupportedLgiDataRate() const [member function]
    cls.add_method('GetRxHighestSupportedLgiDataRate', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetRxLdpc() const [member function]
    cls.add_method('GetRxLdpc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint16_t ns3::VhtCapabilities::GetRxMcsMap() const [member function]
    cls.add_method('GetRxMcsMap', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetRxStbc() const [member function]
    cls.add_method('GetRxStbc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint16_t ns3::VhtCapabilities::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetShortGuardIntervalFor160Mhz() const [member function]
    cls.add_method('GetShortGuardIntervalFor160Mhz', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetShortGuardIntervalFor80Mhz() const [member function]
    cls.add_method('GetShortGuardIntervalFor80Mhz', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetSupportedChannelWidthSet() const [member function]
    cls.add_method('GetSupportedChannelWidthSet', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint64_t ns3::VhtCapabilities::GetSupportedMcsAndNssSet() const [member function]
    cls.add_method('GetSupportedMcsAndNssSet', 
                   'uint64_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint16_t ns3::VhtCapabilities::GetTxHighestSupportedLgiDataRate() const [member function]
    cls.add_method('GetTxHighestSupportedLgiDataRate', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint16_t ns3::VhtCapabilities::GetTxMcsMap() const [member function]
    cls.add_method('GetTxMcsMap', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint8_t ns3::VhtCapabilities::GetTxStbc() const [member function]
    cls.add_method('GetTxStbc', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): uint32_t ns3::VhtCapabilities::GetVhtCapabilitiesInfo() const [member function]
    cls.add_method('GetVhtCapabilitiesInfo', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): bool ns3::VhtCapabilities::IsSupportedMcs(uint8_t mcs, uint8_t Nss) const [member function]
    cls.add_method('IsSupportedMcs', 
                   'bool', 
                   [param('uint8_t', 'mcs'), param('uint8_t', 'Nss')], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): bool ns3::VhtCapabilities::IsSupportedRxMcs(uint8_t mcs) const [member function]
    cls.add_method('IsSupportedRxMcs', 
                   'bool', 
                   [param('uint8_t', 'mcs')], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): bool ns3::VhtCapabilities::IsSupportedTxMcs(uint8_t mcs) const [member function]
    cls.add_method('IsSupportedTxMcs', 
                   'bool', 
                   [param('uint8_t', 'mcs')], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): ns3::Buffer::Iterator ns3::VhtCapabilities::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'ns3::Buffer::Iterator', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SerializeInformationField(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('SerializeInformationField', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetMaxAmpduLengthExponent(uint8_t exponent) [member function]
    cls.add_method('SetMaxAmpduLengthExponent', 
                   'void', 
                   [param('uint8_t', 'exponent')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetMaxMpduLength(uint8_t length) [member function]
    cls.add_method('SetMaxMpduLength', 
                   'void', 
                   [param('uint8_t', 'length')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetRxHighestSupportedLgiDataRate(uint16_t supporteddatarate) [member function]
    cls.add_method('SetRxHighestSupportedLgiDataRate', 
                   'void', 
                   [param('uint16_t', 'supporteddatarate')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetRxLdpc(uint8_t rxldpc) [member function]
    cls.add_method('SetRxLdpc', 
                   'void', 
                   [param('uint8_t', 'rxldpc')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetRxMcsMap(uint16_t map) [member function]
    cls.add_method('SetRxMcsMap', 
                   'void', 
                   [param('uint16_t', 'map')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetRxMcsMap(uint8_t mcs, uint8_t nss) [member function]
    cls.add_method('SetRxMcsMap', 
                   'void', 
                   [param('uint8_t', 'mcs'), param('uint8_t', 'nss')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetRxStbc(uint8_t rxstbc) [member function]
    cls.add_method('SetRxStbc', 
                   'void', 
                   [param('uint8_t', 'rxstbc')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetShortGuardIntervalFor160Mhz(uint8_t shortguardinterval) [member function]
    cls.add_method('SetShortGuardIntervalFor160Mhz', 
                   'void', 
                   [param('uint8_t', 'shortguardinterval')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetShortGuardIntervalFor80Mhz(uint8_t shortguardinterval) [member function]
    cls.add_method('SetShortGuardIntervalFor80Mhz', 
                   'void', 
                   [param('uint8_t', 'shortguardinterval')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetSupportedChannelWidthSet(uint8_t channelwidthset) [member function]
    cls.add_method('SetSupportedChannelWidthSet', 
                   'void', 
                   [param('uint8_t', 'channelwidthset')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetSupportedMcsAndNssSet(uint64_t ctrl) [member function]
    cls.add_method('SetSupportedMcsAndNssSet', 
                   'void', 
                   [param('uint64_t', 'ctrl')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetTxHighestSupportedLgiDataRate(uint16_t supporteddatarate) [member function]
    cls.add_method('SetTxHighestSupportedLgiDataRate', 
                   'void', 
                   [param('uint16_t', 'supporteddatarate')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetTxMcsMap(uint16_t map) [member function]
    cls.add_method('SetTxMcsMap', 
                   'void', 
                   [param('uint16_t', 'map')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetTxMcsMap(uint8_t mcs, uint8_t nss) [member function]
    cls.add_method('SetTxMcsMap', 
                   'void', 
                   [param('uint8_t', 'mcs'), param('uint8_t', 'nss')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetTxStbc(uint8_t txstbc) [member function]
    cls.add_method('SetTxStbc', 
                   'void', 
                   [param('uint8_t', 'txstbc')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetVhtCapabilitiesInfo(uint32_t ctrl) [member function]
    cls.add_method('SetVhtCapabilitiesInfo', 
                   'void', 
                   [param('uint32_t', 'ctrl')])
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilities::SetVhtSupported(uint8_t vhtsupported) [member function]
    cls.add_method('SetVhtSupported', 
                   'void', 
                   [param('uint8_t', 'vhtsupported')])
    return

def register_Ns3VhtCapabilitiesChecker_methods(root_module, cls):
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilitiesChecker::VhtCapabilitiesChecker() [constructor]
    cls.add_constructor([])
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilitiesChecker::VhtCapabilitiesChecker(ns3::VhtCapabilitiesChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::VhtCapabilitiesChecker const &', 'arg0')])
    return

def register_Ns3VhtCapabilitiesValue_methods(root_module, cls):
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilitiesValue::VhtCapabilitiesValue() [constructor]
    cls.add_constructor([])
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilitiesValue::VhtCapabilitiesValue(ns3::VhtCapabilitiesValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::VhtCapabilitiesValue const &', 'arg0')])
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilitiesValue::VhtCapabilitiesValue(ns3::VhtCapabilities const & value) [constructor]
    cls.add_constructor([param('ns3::VhtCapabilities const &', 'value')])
    ## vht-capabilities.h (module 'wifi'): ns3::Ptr<ns3::AttributeValue> ns3::VhtCapabilitiesValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## vht-capabilities.h (module 'wifi'): bool ns3::VhtCapabilitiesValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## vht-capabilities.h (module 'wifi'): ns3::VhtCapabilities ns3::VhtCapabilitiesValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::VhtCapabilities', 
                   [], 
                   is_const=True)
    ## vht-capabilities.h (module 'wifi'): std::string ns3::VhtCapabilitiesValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## vht-capabilities.h (module 'wifi'): void ns3::VhtCapabilitiesValue::Set(ns3::VhtCapabilities const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::VhtCapabilities const &', 'value')])
    return

def register_Ns3WifiModeChecker_methods(root_module, cls):
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeChecker::WifiModeChecker() [constructor]
    cls.add_constructor([])
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeChecker::WifiModeChecker(ns3::WifiModeChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiModeChecker const &', 'arg0')])
    return

def register_Ns3WifiModeValue_methods(root_module, cls):
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeValue::WifiModeValue() [constructor]
    cls.add_constructor([])
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeValue::WifiModeValue(ns3::WifiModeValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::WifiModeValue const &', 'arg0')])
    ## wifi-mode.h (module 'wifi'): ns3::WifiModeValue::WifiModeValue(ns3::WifiMode const & value) [constructor]
    cls.add_constructor([param('ns3::WifiMode const &', 'value')])
    ## wifi-mode.h (module 'wifi'): ns3::Ptr<ns3::AttributeValue> ns3::WifiModeValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## wifi-mode.h (module 'wifi'): bool ns3::WifiModeValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## wifi-mode.h (module 'wifi'): ns3::WifiMode ns3::WifiModeValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::WifiMode', 
                   [], 
                   is_const=True)
    ## wifi-mode.h (module 'wifi'): std::string ns3::WifiModeValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## wifi-mode.h (module 'wifi'): void ns3::WifiModeValue::Set(ns3::WifiMode const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::WifiMode const &', 'value')])
    return

def register_Ns3AddressChecker_methods(root_module, cls):
    ## address.h (module 'network'): ns3::AddressChecker::AddressChecker() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::AddressChecker::AddressChecker(ns3::AddressChecker const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AddressChecker const &', 'arg0')])
    return

def register_Ns3AddressValue_methods(root_module, cls):
    ## address.h (module 'network'): ns3::AddressValue::AddressValue() [constructor]
    cls.add_constructor([])
    ## address.h (module 'network'): ns3::AddressValue::AddressValue(ns3::AddressValue const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::AddressValue const &', 'arg0')])
    ## address.h (module 'network'): ns3::AddressValue::AddressValue(ns3::Address const & value) [constructor]
    cls.add_constructor([param('ns3::Address const &', 'value')])
    ## address.h (module 'network'): ns3::Ptr<ns3::AttributeValue> ns3::AddressValue::Copy() const [member function]
    cls.add_method('Copy', 
                   'ns3::Ptr< ns3::AttributeValue >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## address.h (module 'network'): bool ns3::AddressValue::DeserializeFromString(std::string value, ns3::Ptr<ns3::AttributeChecker const> checker) [member function]
    cls.add_method('DeserializeFromString', 
                   'bool', 
                   [param('std::string', 'value'), param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_virtual=True)
    ## address.h (module 'network'): ns3::Address ns3::AddressValue::Get() const [member function]
    cls.add_method('Get', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    ## address.h (module 'network'): std::string ns3::AddressValue::SerializeToString(ns3::Ptr<ns3::AttributeChecker const> checker) const [member function]
    cls.add_method('SerializeToString', 
                   'std::string', 
                   [param('ns3::Ptr< ns3::AttributeChecker const >', 'checker')], 
                   is_const=True, is_virtual=True)
    ## address.h (module 'network'): void ns3::AddressValue::Set(ns3::Address const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('ns3::Address const &', 'value')])
    return

def register_Ns3DcaTxop_methods(root_module, cls):
    ## dca-txop.h (module 'wifi'): ns3::DcaTxop::DcaTxop() [constructor]
    cls.add_constructor([])
    ## dca-txop.h (module 'wifi'): int64_t ns3::DcaTxop::AssignStreams(int64_t stream) [member function]
    cls.add_method('AssignStreams', 
                   'int64_t', 
                   [param('int64_t', 'stream')])
    ## dca-txop.h (module 'wifi'): uint32_t ns3::DcaTxop::GetAifsn() const [member function]
    cls.add_method('GetAifsn', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dca-txop.h (module 'wifi'): uint32_t ns3::DcaTxop::GetMaxCw() const [member function]
    cls.add_method('GetMaxCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dca-txop.h (module 'wifi'): uint32_t ns3::DcaTxop::GetMinCw() const [member function]
    cls.add_method('GetMinCw', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## dca-txop.h (module 'wifi'): ns3::Ptr<ns3::WifiMacQueue> ns3::DcaTxop::GetQueue() const [member function]
    cls.add_method('GetQueue', 
                   'ns3::Ptr< ns3::WifiMacQueue >', 
                   [], 
                   is_const=True)
    ## dca-txop.h (module 'wifi'): static ns3::TypeId ns3::DcaTxop::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::Queue(ns3::Ptr<ns3::Packet const> packet, ns3::WifiMacHeader const & hdr) [member function]
    cls.add_method('Queue', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'packet'), param('ns3::WifiMacHeader const &', 'hdr')])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::RestartAccessIfNeeded() [member function]
    cls.add_method('RestartAccessIfNeeded', 
                   'void', 
                   [])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetAifsn(uint32_t aifsn) [member function]
    cls.add_method('SetAifsn', 
                   'void', 
                   [param('uint32_t', 'aifsn')], 
                   is_virtual=True)
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetLow(ns3::Ptr<ns3::MacLow> low) [member function]
    cls.add_method('SetLow', 
                   'void', 
                   [param('ns3::Ptr< ns3::MacLow >', 'low')])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetManager(ns3::DcfManager * manager) [member function]
    cls.add_method('SetManager', 
                   'void', 
                   [param('ns3::DcfManager *', 'manager')])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetMaxCw(uint32_t maxCw) [member function]
    cls.add_method('SetMaxCw', 
                   'void', 
                   [param('uint32_t', 'maxCw')], 
                   is_virtual=True)
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetMinCw(uint32_t minCw) [member function]
    cls.add_method('SetMinCw', 
                   'void', 
                   [param('uint32_t', 'minCw')], 
                   is_virtual=True)
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetTxFailedCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxFailedCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetTxMiddle(ns3::MacTxMiddle * txMiddle) [member function]
    cls.add_method('SetTxMiddle', 
                   'void', 
                   [param('ns3::MacTxMiddle *', 'txMiddle')])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetTxOkCallback(ns3::Callback<void, ns3::WifiMacHeader const&, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> callback) [member function]
    cls.add_method('SetTxOkCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::WifiMacHeader const &, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'callback')])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::SetWifiRemoteStationManager(ns3::Ptr<ns3::WifiRemoteStationManager> remoteManager) [member function]
    cls.add_method('SetWifiRemoteStationManager', 
                   'void', 
                   [param('ns3::Ptr< ns3::WifiRemoteStationManager >', 'remoteManager')])
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    ## dca-txop.h (module 'wifi'): void ns3::DcaTxop::DoInitialize() [member function]
    cls.add_method('DoInitialize', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3ConfigMatchContainer_methods(root_module, cls):
    ## config.h (module 'core'): ns3::Config::MatchContainer::MatchContainer(ns3::Config::MatchContainer const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Config::MatchContainer const &', 'arg0')])
    ## config.h (module 'core'): ns3::Config::MatchContainer::MatchContainer() [constructor]
    cls.add_constructor([])
    ## config.h (module 'core'): ns3::Config::MatchContainer::MatchContainer(std::vector<ns3::Ptr<ns3::Object>, std::allocator<ns3::Ptr<ns3::Object> > > const & objects, std::vector<std::string, std::allocator<std::string> > const & contexts, std::string path) [constructor]
    cls.add_constructor([param('std::vector< ns3::Ptr< ns3::Object > > const &', 'objects'), param('std::vector< std::string > const &', 'contexts'), param('std::string', 'path')])
    ## config.h (module 'core'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Object>*,std::vector<ns3::Ptr<ns3::Object>, std::allocator<ns3::Ptr<ns3::Object> > > > ns3::Config::MatchContainer::Begin() const [member function]
    cls.add_method('Begin', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Object > const, std::vector< ns3::Ptr< ns3::Object > > >', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): void ns3::Config::MatchContainer::Connect(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('Connect', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): void ns3::Config::MatchContainer::ConnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('ConnectWithoutContext', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): void ns3::Config::MatchContainer::Disconnect(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('Disconnect', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): void ns3::Config::MatchContainer::DisconnectWithoutContext(std::string name, ns3::CallbackBase const & cb) [member function]
    cls.add_method('DisconnectWithoutContext', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::CallbackBase const &', 'cb')])
    ## config.h (module 'core'): __gnu_cxx::__normal_iterator<const ns3::Ptr<ns3::Object>*,std::vector<ns3::Ptr<ns3::Object>, std::allocator<ns3::Ptr<ns3::Object> > > > ns3::Config::MatchContainer::End() const [member function]
    cls.add_method('End', 
                   '__gnu_cxx::__normal_iterator< ns3::Ptr< ns3::Object > const, std::vector< ns3::Ptr< ns3::Object > > >', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): ns3::Ptr<ns3::Object> ns3::Config::MatchContainer::Get(uint32_t i) const [member function]
    cls.add_method('Get', 
                   'ns3::Ptr< ns3::Object >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## config.h (module 'core'): std::string ns3::Config::MatchContainer::GetMatchedPath(uint32_t i) const [member function]
    cls.add_method('GetMatchedPath', 
                   'std::string', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## config.h (module 'core'): uint32_t ns3::Config::MatchContainer::GetN() const [member function]
    cls.add_method('GetN', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): std::string ns3::Config::MatchContainer::GetPath() const [member function]
    cls.add_method('GetPath', 
                   'std::string', 
                   [], 
                   is_const=True)
    ## config.h (module 'core'): void ns3::Config::MatchContainer::Set(std::string name, ns3::AttributeValue const & value) [member function]
    cls.add_method('Set', 
                   'void', 
                   [param('std::string', 'name'), param('ns3::AttributeValue const &', 'value')])
    return

def register_Ns3HashImplementation_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Implementation::Implementation(ns3::Hash::Implementation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Implementation const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Implementation::Implementation() [constructor]
    cls.add_constructor([])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Implementation::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_pure_virtual=True, is_virtual=True)
    ## hash-function.h (module 'core'): uint64_t ns3::Hash::Implementation::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Implementation::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_pure_virtual=True, is_virtual=True)
    return

def register_Ns3HashFunctionFnv1a_methods(root_module, cls):
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a::Fnv1a(ns3::Hash::Function::Fnv1a const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Fnv1a const &', 'arg0')])
    ## hash-fnv.h (module 'core'): ns3::Hash::Function::Fnv1a::Fnv1a() [constructor]
    cls.add_constructor([])
    ## hash-fnv.h (module 'core'): uint32_t ns3::Hash::Function::Fnv1a::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-fnv.h (module 'core'): uint64_t ns3::Hash::Function::Fnv1a::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-fnv.h (module 'core'): void ns3::Hash::Function::Fnv1a::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionHash32_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32::Hash32(ns3::Hash::Function::Hash32 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Hash32 const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash32::Hash32(ns3::Hash::Hash32Function_ptr hp) [constructor]
    cls.add_constructor([param('ns3::Hash::Hash32Function_ptr', 'hp')])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Function::Hash32::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Function::Hash32::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionHash64_methods(root_module, cls):
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64::Hash64(ns3::Hash::Function::Hash64 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Hash64 const &', 'arg0')])
    ## hash-function.h (module 'core'): ns3::Hash::Function::Hash64::Hash64(ns3::Hash::Hash64Function_ptr hp) [constructor]
    cls.add_constructor([param('ns3::Hash::Hash64Function_ptr', 'hp')])
    ## hash-function.h (module 'core'): uint32_t ns3::Hash::Function::Hash64::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): uint64_t ns3::Hash::Function::Hash64::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-function.h (module 'core'): void ns3::Hash::Function::Hash64::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_Ns3HashFunctionMurmur3_methods(root_module, cls):
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3::Murmur3(ns3::Hash::Function::Murmur3 const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Hash::Function::Murmur3 const &', 'arg0')])
    ## hash-murmur3.h (module 'core'): ns3::Hash::Function::Murmur3::Murmur3() [constructor]
    cls.add_constructor([])
    ## hash-murmur3.h (module 'core'): uint32_t ns3::Hash::Function::Murmur3::GetHash32(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash32', 
                   'uint32_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-murmur3.h (module 'core'): uint64_t ns3::Hash::Function::Murmur3::GetHash64(char const * buffer, size_t const size) [member function]
    cls.add_method('GetHash64', 
                   'uint64_t', 
                   [param('char const *', 'buffer'), param('size_t const', 'size')], 
                   is_virtual=True)
    ## hash-murmur3.h (module 'core'): void ns3::Hash::Function::Murmur3::clear() [member function]
    cls.add_method('clear', 
                   'void', 
                   [], 
                   is_virtual=True)
    return

def register_functions(root_module):
    module = root_module
    register_functions_ns3_CommandLineHelper(module.get_submodule('CommandLineHelper'), root_module)
    register_functions_ns3_Config(module.get_submodule('Config'), root_module)
    register_functions_ns3_FatalImpl(module.get_submodule('FatalImpl'), root_module)
    register_functions_ns3_Hash(module.get_submodule('Hash'), root_module)
    register_functions_ns3_SystemPath(module.get_submodule('SystemPath'), root_module)
    register_functions_ns3_TracedValueCallback(module.get_submodule('TracedValueCallback'), root_module)
    register_functions_ns3_internal(module.get_submodule('internal'), root_module)
    return

def register_functions_ns3_CommandLineHelper(module, root_module):
    return

def register_functions_ns3_Config(module, root_module):
    return

def register_functions_ns3_FatalImpl(module, root_module):
    return

def register_functions_ns3_Hash(module, root_module):
    register_functions_ns3_Hash_Function(module.get_submodule('Function'), root_module)
    return

def register_functions_ns3_Hash_Function(module, root_module):
    return

def register_functions_ns3_SystemPath(module, root_module):
    return

def register_functions_ns3_TracedValueCallback(module, root_module):
    return

def register_functions_ns3_internal(module, root_module):
    return

def main():
    out = FileCodeSink(sys.stdout)
    root_module = module_init()
    register_types(root_module)
    register_methods(root_module)
    register_functions(root_module)
    root_module.generate(out)

if __name__ == '__main__':
    main()


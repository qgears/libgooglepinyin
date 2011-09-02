set(IBUS_PREFIX /usr)
set(pkgdatadir ${IBUS_PREFIX}/share/ibus-googlepinyin)
set(VERSION 0.0.1)

configure_file(googlepinyin.xml.in ${CMAKE_CURRENT_SOURCE_DIR}/googlepinyin.xml)

install(PROGRAMS main.py       DESTINATION ${IBUS_PREFIX}/share/ibus-googlepinyin)
install(FILES engine.py factory.py googlepinyin.py libopencc.py pygooglepinyin.py DESTINATION ${IBUS_PREFIX}/share/ibus-googlepinyin)
install(FILES googlepinyin.xml DESTINATION ${IBUS_PREFIX}/share/ibus/component/)
install(DIRECTORY icons/       DESTINATION ${IBUS_PREFIX}/share/ibus-googlepinyin/icons)


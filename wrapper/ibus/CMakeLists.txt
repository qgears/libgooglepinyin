set(pkgdatadir ${CMAKE_INSTALL_PREFIX}/share/ibus-googlepinyin)
set(VERSION 0.0.1)

configure_file(googlepinyin.xml.in ${CMAKE_CURRENT_SOURCE_DIR}/googlepinyin.xml)

install(PROGRAMS main.py       DESTINATION share/ibus-googlepinyin)
install(FILES engine.py factory.py googlepinyin.py libopencc.py pygooglepinyin.py DESTINATION share/ibus-googlepinyin)
install(FILES googlepinyin.xml DESTINATION share/ibus/component/)
install(DIRECTORY icons/       DESTINATION share/ibus-googlepinyin/icons)


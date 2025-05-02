<jm:menu_and_toolbar_customizations xmlns:jm="http://www.jmp.com/ns/menu" version="3">
	<jm:insert_in_main_menu>
		<jm:insert_after>
			<jm:menu>
				<jm:name>ASECL</jm:name>
				<jm:caption>ASECL</jm:caption>
				<jm:menu>
					<jm:name>ASSY</jm:name>
					<jm:caption>ASSY</jm:caption>
					<jm:command>
						<jm:name>JMP_ANA02</jm:name>
						<jm:caption>WB Yield Analysis | WB良率分析</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\ASSY\Reports\JMP_ANA02\ANA02_DataQuery_Main.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>ASSY_ANA03</jm:name>
					<jm:caption>ASSY</jm:caption>
					<jm:command>
						<jm:name>ANA03</jm:name>
						<jm:caption>ANA03- WB Log Mapping</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\ASSY\Reports\JMP_ANA03\ANA03_DataQuery_Main.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>ASSY_ANA04</jm:name>
					<jm:caption>ASSY</jm:caption>
					<jm:command>
						<jm:name>ANA04</jm:name>
						<jm:caption>ANA04- WB SPC By Program</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\ASSY\Reports\JMP_ANA04\ANA04_DataQuery_Main.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>BUMP</jm:name>
					<jm:caption>BUMP</jm:caption>
					<jm:command>
						<jm:name>Wafer Map</jm:name>
						<jm:caption>Wafer Map | 疊圖分析 [此功能遠端電腦無法使用, 請用共用電腦]</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\CPBP\Reports\CPBP_WaferMap\WaferMap_DataQuery.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
					<jm:command>
						<jm:name>Wafer Map</jm:name>
						<jm:caption>Wafer Map by Hold Lot | 疊圖分析 by Hold Lot [此功能遠端電腦無法使用, 請用共用電腦]</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\CPBP\Reports\CPBP_WaferMap\WafermapBumpHoldLot.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
					<jm:command>
						<jm:name>Wafer Map</jm:name>
						<jm:caption>Wafer Map | 疊圖分析 (test)</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\Bump小精靈\WaferMapping_CPBP\Reports\CPBP_WaferMap\WaferMap_DataQuery.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>CP</jm:name>
					<jm:caption>CP</jm:caption>
					<jm:command>
						<jm:name>Wafer Map</jm:name>
						<jm:caption>Wafer Map | 疊圖分析 [此功能遠端電腦無法使用, 請用共用電腦]</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\CPBP\Reports\CPBP_WaferMap\WaferMap_DataQuery.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
					<jm:command>
						<jm:name>Wafer Map</jm:name>
						<jm:caption>Dr. Yield | 整合分析平台</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\CP\CP\Reports\CPBP_WaferMap\WaferMap_DataQuery.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Dr. Yield VER(2023011101)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>KVM</jm:name>
						<jm:caption>KVM</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\CP\KVM\KVM.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>KVM VER(2023010501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>MTBA</jm:name>
						<jm:caption>MTBA</jm:caption>
						<jm:action type="path">I:\JMP\APP\PRD\CP\CP_MTBA\CP_MTBA_project.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>MTBA VER(2023010501)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>FT</jm:name>
					<jm:caption>FT</jm:caption>
					<jm:menu>
						<jm:name>RLK</jm:name>
						<jm:caption>RLK</jm:caption>
						<jm:command>
							<jm:name>RLK Report</jm:name>
							<jm:caption>RLK Yield | RAW</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\RLK\RLK_RAW.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>RLK Yield VER(2022030901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>RLK Report</jm:name>
							<jm:caption>RLK Yield | Gap</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\RLK\RLK_P2.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>RLK Yield VER(2022030901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>RLK Report</jm:name>
							<jm:caption>RLK Yield | Final Defect</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\RLK\RLK_P3.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>RLK Yield VER(2022030901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>RLK Report</jm:name>
							<jm:caption>RLK Yield | Recovery Rate</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\RLK\RLK_P4.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>RLK Yield VER(2022030901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>RLK Report</jm:name>
							<jm:caption>RLK Yield | Tooling</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\RLK\RLK_P7.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>RLK Yield VER(2022030901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>RLK Report</jm:name>
							<jm:caption>RLK Machine | Status</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\RLK\RLK_P6.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>RLK Machine VER(2022031701)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>RLK Report</jm:name>
							<jm:caption>RLK Machine | Tester</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\RLK\RLK_P8.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>RLK Machine VER(2022112401)</jm:tip>
						</jm:command>
					</jm:menu>
					<jm:menu>
						<jm:name>MTM</jm:name>
						<jm:caption>MTM</jm:caption>
						<jm:command>
							<jm:name>MTM project</jm:name>
							<jm:caption>MTM project</jm:caption>
							<jm:action type="path">I:\JMP\APP\PRD\FT\MTM\FT_MTM_project.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>MTM project VER(2023010501)</jm:tip>
						</jm:command>
					</jm:menu>
				</jm:menu>
				<jm:menu>
					<jm:name>System</jm:name>
					<jm:caption>System</jm:caption>
					<jm:command>
						<jm:name>System Check</jm:name>
						<jm:caption>System Check | 確認系統環境 </jm:caption>
						<jm:action type="path">I:\JMP\SYSTEM\system_check.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
					<jm:command>
						<jm:name>Open Source </jm:name>
						<jm:caption>Open Working Directory | 開啟暫存資料夾 </jm:caption>
						<jm:action type="path">I:\JMP\SYSTEM\open_sourcepath.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
					<jm:command>
						<jm:name>Open Source </jm:name>
						<jm:caption>Connection Test | 連線測試 </jm:caption>
						<jm:action type="path">I:\JMP\SYSTEM\ConnectionTest.jsl</jm:action>
						<jm:icon type="none"/>
					</jm:command>
				</jm:menu>
			</jm:menu>
		</jm:insert_after>
		<jm:insert_after>
			<jm:menu>
				<jm:name>ASECL_Wizard</jm:name>
				<jm:caption>ASSY小精靈</jm:caption>
				<jm:menu>
					<jm:name>AOI</jm:name>
					<jm:caption>AOI</jm:caption>
					<jm:command>
						<jm:name>AOI Report</jm:name>
						<jm:caption>AOI Report</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\AOI\ASSY小精靈_AOI_AOI Report.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>AOI Report VER(2023020201)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>FVI Log精靈</jm:name>
						<jm:caption>FVI Log精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\AOI\ASSY小精靈_AOI_FVI Log精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>FVI Log精靈 VER(2022112301)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>OS Analysis</jm:name>
						<jm:caption>OS Analysis</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\AOI\ASSY小精靈_AOI_OS Analysis.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>OS Analysis VER(2024101401)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>OS 工程模式 log解析</jm:name>
						<jm:caption>OS 工程模式 log解析</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\AOI\ASSY小精靈_AOI_OS 工程模式 log解析.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>OS 工程模式 log解析 VER(2022111501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>OS電壓值精靈</jm:name>
						<jm:caption>OS電壓值精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\AOI\ASSY小精靈_AOI_OS電壓值精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>OS電壓值精靈 VER(2023061901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>OS精靈</jm:name>
						<jm:caption>OS精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\AOI\ASSY小精靈_AOI_OS精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>OS精靈 VER(2024101501)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>BUMP</jm:name>
					<jm:caption>BUMP</jm:caption>
					<jm:command>
						<jm:name>Abnormal Lot</jm:name>
						<jm:caption>Abnormal Lot</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Abnormal type analysis.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Abnormal Lot VER(2021122701)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Back End Query</jm:name>
						<jm:caption>Back End Query</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Back End Query.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Back End Query VER(2022112201)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Chemical life time</jm:name>
						<jm:caption>Chemical life time</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_Chemical life time.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Chemical life time VER(2024041801)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Combine BH data</jm:name>
						<jm:caption>Combine BH data</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_Combine BH data.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Combine BH data VER(2024071901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>CP Map Pattern</jm:name>
						<jm:caption>CP Map Pattern</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_CP Map Pattern.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>CP Map Pattern VER(2024071901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Process Mapping</jm:name>
						<jm:caption>Process Mapping</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_Process Mapping.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Process Mapping VER(2024082901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>PSK mapping</jm:name>
						<jm:caption>PSK mapping</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_PSK mapping.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>PSK mapping VER(2024071901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>SPC query by DCOP</jm:name>
						<jm:caption>SPC query by DCOP</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_SPC query by DCOP.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>SPC query by DCOP VER(2022112901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>疊圖疊Die</jm:name>
						<jm:caption>疊圖疊Die</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_疊圖疊Die.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>疊圖疊Die VER(2023082801)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Yield Report</jm:name>
						<jm:caption>Yield Report</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Yield_ Yield Report.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Yield Report VER(2022031701)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Yield by LOTID</jm:name>
						<jm:caption>Yield by LOTID</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Yield_ Yield by LOTID, WAFERLOT or MASKID.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Yield by LOTID VER(2022080401)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>DB</jm:name>
					<jm:caption>DB</jm:caption>
					<jm:command>
						<jm:name>自動Mapping生成精靈</jm:name>
						<jm:caption>自動Mapping生成精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\DB\ASSY小精靈_DB_自動Mapping生成精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>自動Mapping生成精靈 VER(2024050901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>DB參數檢驗精靈</jm:name>
						<jm:caption>DB參數檢驗精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\DB\ASSY小精靈_DB_DB參數檢驗精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>DB參數檢驗精靈 VER(2023020901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>EDC Analysis and Comparison</jm:name>
						<jm:caption>EDC Analysis and Comparison</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\DB\ASSY小精靈_DB_EDC Analysis and Comparison.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>EDC Analysis and Comparison VER(2023031401)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>E142 XML檔撈取精靈</jm:name>
						<jm:caption>E142 XML檔撈取精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\DB\ASSY小精靈_DB_E142 XML檔撈取精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>E142 XML檔撈取精靈 VER(2024092401)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>E142資料撈取精靈</jm:name>
						<jm:caption>E142資料撈取精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\DB\ASSY小精靈_DB_E142資料撈取精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>E142資料撈取精靈 VER(2023110201)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>E142手動補資料</jm:name>
						<jm:caption>E142手動補資料</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\DB\ASSY小精靈_DB_E142手動補資料.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>E142手動補資料 VER(2024111301)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>SWI撈取精靈</jm:name>
						<jm:caption>SWI撈取精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\DB\ASSY小精靈_DB_SWI撈取精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>SWI撈取精靈 VER(2023062001)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>LG</jm:name>
					<jm:caption>LG</jm:caption>
					<jm:command>
						<jm:name>PM精靈</jm:name>
						<jm:caption>PM精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\LG\ASSY小精靈_LG_PM精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>PM精靈 VER(2023112401)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Smart MTBA Analysis</jm:name>
						<jm:caption>Smart MTBA Analysis</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\LG\ASSY小精靈_LG_LaserGrooving MTBA Analysis Report.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Smart MTBA Analysis VER(2022121901)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>MD</jm:name>
					<jm:caption>MD</jm:caption>
					<jm:command>
						<jm:name>Molding MTBA Analysis Report</jm:name>
						<jm:caption>Molding MTBA Analysis Report</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\MD\ASSY小精靈_MD_Molding MTBA Analysis Report.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Molding MTBA Analysis Report VER(2022121901)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>QA</jm:name>
					<jm:caption>QA</jm:caption>
					<jm:command>
						<jm:name>ASSY SPC Control Chart</jm:name>
						<jm:caption>ASSY SPC Control Chart</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\QA\ASSY小精靈_QA_ASSY SPC Control Chart Auto Analysis Tool.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>ASSY SPC Control Chart VER(2022081801)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>NPI Script sas</jm:name>
						<jm:caption>NPI Script sas</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\QA\ASSY小精靈_QA_NPI_Script_sas.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>NPI Script sas VER(2022112901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>PSN Rate Report</jm:name>
						<jm:caption>PSN Rate Report</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\QA\ASSY小精靈_QA_PSN Rate Report.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>PSN Rate Report VER(2022091901)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>SS</jm:name>
					<jm:caption>SS</jm:caption>
                    <jm:command>
						<jm:name>HighEnd MTBA Analysis Report</jm:name>
						<jm:caption>HighEnd MTBA Analysis Report</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\SS\ASSY小精靈_SS_Jig_HighEnd MTBA Analysis Report.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>HighEnd MTBA Analysis Report VER(2022121901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Lighting Tracking(A6 TEST)</jm:name>
						<jm:caption>Lighting Tracking(A6 TEST)</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\SS\ASSY小精靈_SS_Smart_MTM_Lighting_Report(A6 TEST).jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Lighting Tracking(A6 TEST) VER(2023100601)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>SS Axis Trend Report</jm:name>
						<jm:caption>SS Axis Trend Report</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\SS\ASSY小精靈_SS_SS Axis Trend Report.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>SS Axis Trend Report VER(2024102401)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>Saw</jm:name>
					<jm:caption>Saw</jm:caption>
					<jm:menu>
						<jm:name>WS</jm:name>
						<jm:caption>WS</jm:caption>
						<jm:command>
							<jm:name>Kerf Center Tracking</jm:name>
							<jm:caption>Kerf Center Tracking</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\Saw\ASSY小精靈_Saw_Kerfcenter Report.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Kerf Center Tracking VER(2023112901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Lighting Tracking</jm:name>
							<jm:caption>Lighting Tracking</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\Saw\ASSY小精靈_Saw_ Lighting Report.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Lighting Tracking VER(2023061901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>NCS_CT Gap(A8)</jm:name>
							<jm:caption>NCS_CT Gap(A8)</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\Saw\ASSY小精靈_Saw_NCS_CT Gap(A8).jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>NCS_CT Gap(A8) VER(2023082201)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Smart MTBA 2.0 Analysis</jm:name>
							<jm:caption>Smart MTBA 2.0 Analysis</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\Saw\ASSY小精靈_Saw_WS-Smart MTBA 2.0 Analysis.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Smart MTBA 2.0 Analysis VER(2023110201)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Wafer回推Strip</jm:name>
							<jm:caption>Wafer回推Strip</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\Saw\ASSY小精靈_Saw_Wafer回推Strip.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Wafer回推Strip VER(2024060501)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>吃錯Mapping神燈精靈</jm:name>
							<jm:caption>吃錯Mapping神燈精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\Saw\ASSY小精靈_Saw_吃錯Mapping神燈精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>吃錯Mapping神燈精靈 VER(2024112101)</jm:tip>
						</jm:command>
					</jm:menu>
				</jm:menu>
            <jm:menu>
					<jm:name>WB</jm:name>
					<jm:caption>WB</jm:caption>
					<jm:command>
						<jm:name>鋼嘴歪歪</jm:name>
						<jm:caption>鋼嘴歪歪</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\WB\ASSY小精靈_WB_鋼嘴歪歪.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>鋼嘴歪歪 VER(2024042901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>鋼嘴歪歪人機分析</jm:name>
						<jm:caption>鋼嘴歪歪人機分析</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\WB\ASSY小精靈_WB_鋼嘴歪歪人機分析.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>鋼嘴歪歪人機分析 VER(2023051901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>WB四大天王</jm:name>
						<jm:caption>WB四大天王</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\WB\ASSY小精靈_WB_WB四大天王.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>WB四大天王 VER(2022051901)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>廠別</jm:name>
					<jm:caption>廠別</jm:caption>
					<jm:menu>
						<jm:name>ASSY1+ASSY3</jm:name>
						<jm:caption>ASSY1+ASSY3</jm:caption>
						<jm:command>
							<jm:name>地震影響批精靈</jm:name>
							<jm:caption>地震影響批精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY1+ASSY3\ASSY小精靈_廠別_ASSY1+ASSY3_地震影響批精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>地震影響批精靈 VER(2024042901)</jm:tip>
						</jm:command>
					</jm:menu>
					<jm:menu>
						<jm:name>ASSY6+ASSY7</jm:name>
						<jm:caption>ASSY6+ASSY7</jm:caption>
						<jm:command>
							<jm:name>A6 WI &amp; SWI Report</jm:name>
							<jm:caption>A6 WI &amp; SWI Report</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_A6 WI &amp; SWI Report.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>A6 WI &amp; SWI Report VER(2024100801)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>A6AOI補資料精靈</jm:name>
							<jm:caption>A6AOI補資料精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_A6AOI補資料精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>A6AOI補資料精靈 VER(2024100801)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>A6FCB製程時間計算</jm:name>
							<jm:caption>A6FCB製程時間計算</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_A6FCB製程時間計算.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>A6FCB製程時間計算 VER(2024022901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>A7 Bleed 分析</jm:name>
							<jm:caption>A7 Bleed 分析</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_A7 Bleed 分析.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>A7 Bleed 分析 VER(2024070101)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>AOI分析精靈</jm:name>
							<jm:caption>AOI分析精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_AOI分析精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>AOI分析精靈 VER(2024100801)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Chip to Wafer</jm:name>
							<jm:caption>Chip to Wafer</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Chip to Wafer.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Chip to Wafer VER(2024051501)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Defect PPM by MC</jm:name>
							<jm:caption>Defect PPM by MC</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Defect PPM by MC.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Defect PPM by MC VER(2022071301)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>dipping plate查詢精靈</jm:name>
							<jm:caption>dipping plate查詢精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_dipping plate查詢精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>dipping plate查詢精靈 VER(2024031201)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>EDC Analysis and Comparison</jm:name>
							<jm:caption>EDC Analysis and Comparison</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_EDC Analysis and Comparison.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>EDC Analysis and Comparison VER(2023031401)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Exposed die TOTAL_THK Report</jm:name>
							<jm:caption>Exposed die TOTAL_THK Report</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Exposed die TOTAL_THK Report.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Exposed die TOTAL_THK Report VER(2024061401)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>FC B E142手動補資料</jm:name>
							<jm:caption>FCB E142手動補資料</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_FCB E142手動補資料.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>FCB E142手動補資料 VER(2024112101)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>FC IDT 2DID data 比對</jm:name>
							<jm:caption>FC IDT 2DID data 比對</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_FC IDT 2DID data 比對.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>FC IDT 2DID data 比對 VER(2024050901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>FCB製程時間計算</jm:name>
							<jm:caption>FCB製程時間計算</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_FCB製程時間計算.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>FCB製程時間計算 VER(2024031201)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Flux Clean Program查詢</jm:name>
							<jm:caption>Flux Clean Program查詢</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Flux Clean Program查詢.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Flux Clean Program查詢 VER(2024082001)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>FluxClean ALID 分析精靈</jm:name>
							<jm:caption>FluxClean ALID 分析精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_FluxClean ALID 分析精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>FluxClean ALID 分析精靈 VER(2024112101)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Flux查詢精靈 AO版</jm:name>
							<jm:caption>Flux查詢精靈 AO版</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Flux查詢精靈 AO版.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Flux查詢精靈 AO版 VER(2024051001)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Flux查詢精靈 BD版</jm:name>
							<jm:caption>Flux查詢精靈 BD版</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Flux查詢精靈 BD版.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Flux查詢精靈 BD版 VER(2024051001)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>ICOSAI分析精靈</jm:name>
							<jm:caption>ICOSAI分析精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_ICOSAI分析精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>ICOSAI分析精靈 VER(2024111101)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Lab追蹤表單</jm:name>
							<jm:caption>Lab追蹤表單</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Lab追蹤表單.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Lab追蹤表單 VER(2024091901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>MUF check list</jm:name>
							<jm:caption>MUF check list</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_MUF check list.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>MUF check list VER(2024070301)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>OEECOEE</jm:name>
							<jm:caption>OEECOEE</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_OEECOEE.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>OEECOEE VER(2024080601)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>OUTPUT計算</jm:name>
							<jm:caption>OUTPUT計算</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_OUTPUT計算.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>OUTPUT計算 VER(2024043001)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>PD06Log分析</jm:name>
							<jm:caption>PD06Log分析</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_PD06Log分析.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>PD06Log分析 VER(2024020201)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Reflow profile</jm:name>
							<jm:caption>Reflow profile</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Reflow profile.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Reflow profile VER(2024011801)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Rework前Defect</jm:name>
							<jm:caption>Rework前Defect</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Rework前Defect.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Rework前Defect VER(2024091301)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>SCT分析精靈</jm:name>
							<jm:caption>SCT分析精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_SCT分析精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>SCT分析精靈 VER(2024110101)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>Staging time tracking</jm:name>
							<jm:caption>Staging time tracking</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_Enginner lot Hold and Wait tracking.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Staging time tracking VER(2022122901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>TCB bonding profile</jm:name>
							<jm:caption>TCB bonding profile</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_TCB bonding profile.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>TCB bonding profile VER(2024091901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>線上程式機型List</jm:name>
							<jm:caption>線上程式機型List</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_線上程式機型List.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>線上程式機型List VER(2024100801)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>早會快問快答</jm:name>
							<jm:caption>早會快問快答</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY6+ASSY7\ASSY小精靈_廠別_ASSY6+ASSY7_早會快問快答.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>早會快問快答 VER(2024092501)</jm:tip>
						</jm:command>
					</jm:menu>
					<jm:menu>
						<jm:name>ASSY9</jm:name>
						<jm:caption>ASSY9</jm:caption>
						<jm:command>
							<jm:name>NCS電壓精靈</jm:name>
							<jm:caption>NCS電壓精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY9\ASSY小精靈_廠別_ASSY9_NCS電壓精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>NCS電壓精靈 VER(2023092201)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>NXP SetupLimit</jm:name>
							<jm:caption>NXP SetupLimit</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY9\ASSY小精靈_廠別_ASSY9_NXP_SetupLimit_UI.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>NXP SetupLimit VER(2023020601)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>OTD管理報表</jm:name>
							<jm:caption>OTD管理報表</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY9\ASSY小精靈_廠別_ASSY9_OTD管理報表.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>OTD管理報表 VER(2023022201)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>小停機精靈</jm:name>
							<jm:caption>小停機精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY9\ASSY小精靈_廠別_ASSY9_小停機精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>小停機精靈 VER(2023092501)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>髒髒精靈補資料</jm:name>
							<jm:caption>髒髒精靈補資料</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY9\ASSY小精靈_廠別_ASSY9_髒髒精靈補資料.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>髒髒精靈補資料 VER(2023041301)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>髒髒小精靈</jm:name>
							<jm:caption>髒髒小精靈</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY9\ASSY小精靈_廠別_ASSY9_髒髒小精靈.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>髒髒小精靈 VER(2024010901)</jm:tip>
						</jm:command>
						<jm:command>
							<jm:name>走路工監控</jm:name>
							<jm:caption>走路工監控</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\ASSY9\ASSY小精靈_廠別_ASSY9_走路工監控.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>走路工監控 VER(2023090601)</jm:tip>
						</jm:command>
					</jm:menu>
					<jm:menu>
						<jm:name>Plating</jm:name>
						<jm:caption>Plating</jm:caption>
						<jm:command>
							<jm:name>Plating Area</jm:name>
							<jm:caption>Plating Area</jm:caption>
							<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\廠別\Plating\ASSY小精靈_廠別_Plating_Plating Area.jsl</jm:action>
							<jm:icon type="none"/>
							<jm:tip>Plating Area VER(2024032101)</jm:tip>
						</jm:command>
					</jm:menu>
				</jm:menu>
				<jm:menu>
					<jm:name>神燈精靈</jm:name>
					<jm:caption>神燈精靈</jm:caption>
					<jm:command>
						<jm:name>Auto Process Mapping神燈精靈</jm:name>
						<jm:caption>Auto Process Mapping神燈精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_Auto Process Mapping神燈精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Auto Process Mapping神燈精靈 VER(2024090501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>ASSY Defect 精靈</jm:name>
						<jm:caption>ASSY Defect 精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_ASSY Defect 精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>ASSY Defect 精靈 VER(2024091901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>ASSY Yield 精靈</jm:name>
						<jm:caption>ASSY Yield 精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_ASSY Yield 精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>ASSY Yield 精靈 VER(2023111501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>CPK精靈</jm:name>
						<jm:caption>CPK精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_CPK精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>CPK精靈 VER(2023081601)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>COC DATA查詢精靈</jm:name>
						<jm:caption>COC DATA查詢精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_COC DATA查詢精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>COC DATA查詢精靈 VER(2024112601)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>常態分佈模擬器</jm:name>
						<jm:caption>常態分佈模擬器</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_常態分佈模擬器.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>常態分佈模擬器 VER(2023060901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>常態檢定</jm:name>
						<jm:caption>常態檢定</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_常態檢定.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>常態檢定 VER(2022121901)</jm:tip>
					</jm:command>
                    <jm:command>
						<jm:name>KeyFactor精靈</jm:name>
						<jm:caption>KeyFactor精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_KeyFactor精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>KeyFactor精靈 VER(2021102701)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>LF標記精靈</jm:name>
						<jm:caption>LF標記精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_LF標記精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>LF標記精靈 VER(2023091301)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Machine log神燈精靈</jm:name>
						<jm:caption>Machine log神燈精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_Machine log神燈精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Machine log神燈精靈 VER(2023081701)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>PM精靈</jm:name>
						<jm:caption>PM精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_PM精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>PM精靈 VER(2023072601)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>RSM DOE Window輔助精靈</jm:name>
						<jm:caption>RSM DOE Window輔助精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_RSM DOE Window輔助精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>RSM DOE Window輔助精靈 VER(2023120501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>SPC分析精靈</jm:name>
						<jm:caption>SPC分析精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_SPC分析精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>SPC分析精靈 VER(2024102501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>SPC模擬器</jm:name>
						<jm:caption>SPC模擬器</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_SPC模擬器.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>SPC模擬器 VER(2024082201)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Strip回推Wafer</jm:name>
						<jm:caption>Strip回推Wafer</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_Strip回推Wafer.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Strip回推Wafer VER(2024112101)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>Strip回推Wafer(FPP047)</jm:name>
						<jm:caption>Strip回推Wafer(FPP047)</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_Strip回推Wafer(FPP047).jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>Strip回推Wafer(FPP047) VER(2024050901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>UPH精靈</jm:name>
						<jm:caption>UPH精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_UPH精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>UPH精靈 VER(2024111301)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>XML解碼器</jm:name>
						<jm:caption>XML解碼器</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_XML解碼器.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>XML解碼器 VER(2024110701)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>常態檢定</jm:name>
						<jm:caption>常態檢定</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_常態檢定.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>常態檢定 VER(2022121901)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>合批精靈</jm:name>
						<jm:caption>合批精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_合批精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>合批精靈 VER(2024071501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>檢定神燈精靈</jm:name>
						<jm:caption>檢定神燈精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_檢定神燈精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>檢定神燈精靈 VER(2023121201)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>參數精靈</jm:name>
						<jm:caption>參數精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_參數精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>參數精靈 VER(2022121301)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>連檢定</jm:name>
						<jm:caption>連檢定</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_連檢定.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>連檢定 VER(2023011801)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>製程時間計算</jm:name>
						<jm:caption>製程時間計算</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_製程時間計算.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>製程時間計算 VER(2024072201)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>前段Defect 時間趨勢</jm:name>
						<jm:caption>前段Defect 時間趨勢</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_前段Defect 時間趨勢.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>前段Defect 時間趨勢 VER(2024010501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>快問快答 (綠帶教學)</jm:name>
						<jm:caption>快問快答 (綠帶教學)</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_快問快答 (綠帶教學).jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>快問快答 (綠帶教學) VER(2024011501)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>追料精靈</jm:name>
						<jm:caption>追料精靈</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_追料精靈.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>追料精靈 VER(2023080101)</jm:tip>
					</jm:command>
					<jm:command>
						<jm:name>混料機會站點</jm:name>
						<jm:caption>混料機會站點</jm:caption>
						<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\ASSY小精靈\神燈精靈\ASSY小精靈_神燈精靈_混料機會站點.jsl</jm:action>
						<jm:icon type="none"/>
						<jm:tip>混料機會站點 VER(2024111801)</jm:tip>
					</jm:command>
				</jm:menu>
				<jm:menu>
					<jm:name>BUMP_Wizard</jm:name>
					<jm:caption>BUMP小精靈</jm:caption>					
				</jm:menu>
			</jm:menu>
		</jm:insert_after>
		</jm:insert_after>
			<jm:menu>
				<jm:name>BUMP_Wizard</jm:name>
				<jm:caption>BUMP小精靈</jm:caption>
				<jm:command>
					<jm:name>Abnormal Lot</jm:name>
					<jm:caption>Abnormal Lot</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Abnormal type analysis.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>Abnormal Lot VER(2021122701)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>Back End Query</jm:name>
					<jm:caption>Back End Query</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Back End Query.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>Back End Query VER(2022112201)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>Chemical life time</jm:name>
					<jm:caption>Chemical life time</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_Chemical life time.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>Chemical life time VER(2024041801)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>Combine BH data</jm:name>
					<jm:caption>Combine BH data</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_Combine BH data.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>Combine BH data VER(2024071901)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>CP Map Pattern</jm:name>
					<jm:caption>CP Map Pattern</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_CP Map Pattern.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>CP Map Pattern VER(2024071901)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>Process Mapping</jm:name>
					<jm:caption>Process Mapping</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_Process Mapping.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>Process Mapping VER(2024082901)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>PSK mapping</jm:name>
					<jm:caption>PSK mapping</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Process Mapping_PSK mapping.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>PSK mapping VER(2024071901)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>SPC query by DCOP</jm:name>
					<jm:caption>SPC query by DCOP</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_SPC query by DCOP.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>SPC query by DCOP VER(2022112901)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>Yield Report</jm:name>
					<jm:caption>Yield Report</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Yield_ Yield Report.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>Yield Report VER(2022031701)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>Yield by LOTID</jm:name>
					<jm:caption>Yield by LOTID</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_Yield_ Yield by LOTID, WAFERLOT or MASKID.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>Yield by LOTID VER(2022080401)</jm:tip>
				</jm:command>
				<jm:command>
					<jm:name>疊圖疊Die</jm:name>
					<jm:caption>疊圖疊Die</jm:caption>
					<jm:action type="path">\\asecl-fs1\share_data$\JMP\APP\PRD\Bump小精靈\BUMP小精靈_疊圖疊Die.jsl</jm:action>
					<jm:icon type="none"/>
					<jm:tip>疊圖疊Die VER(2023082801)</jm:tip>
				</jm:command>
			</jm:menu>
		</jm:insert_after>
	</jm:insert_in_main_menu>
</jm:menu_and_toolbar_customizations>
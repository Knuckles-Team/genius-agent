# MCP_AGENTS.md - Dynamic Agent Registry

This file tracks the generated agents from MCP servers. You can manually modify the 'Tools' list to customize agent expertise.

## Agent Mapping Table

| Name | Description | System Prompt | Tools | Tag | Source MCP |
|------|-------------|---------------|-------|-----|------------|
| Adguard-Home Dhcp Specialist | Expert specialist for dhcp domain tasks. | You are a Adguard-Home Dhcp specialist. Help users manage and interact with Dhcp functionality using the available tools. | adguard-home-agent_dhcp_toolset | dhcp | adguard-home-agent |
| Adguard-Home Blocked Services Specialist | Expert specialist for blocked_services domain tasks. | You are a Adguard-Home Blocked Services specialist. Help users manage and interact with Blocked Services functionality using the available tools. | adguard-home-agent_blocked_services_toolset | blocked_services | adguard-home-agent |
| Adguard-Home Access Specialist | Expert specialist for access domain tasks. | You are a Adguard-Home Access specialist. Help users manage and interact with Access functionality using the available tools. | adguard-home-agent_access_toolset | access | adguard-home-agent |
| Adguard-Home System Specialist | Expert specialist for system domain tasks. | You are a Adguard-Home System specialist. Help users manage and interact with System functionality using the available tools. | adguard-home-agent_system_toolset, container-manager-mcp_system_toolset, documentdb-mcp_system_toolset, jellyfin-mcp_system_toolset, systems-manager_system_toolset | system | adguard-home-agent |
| Adguard-Home Settings Specialist | Expert specialist for settings domain tasks. | You are a Adguard-Home Settings specialist. Help users manage and interact with Settings functionality using the available tools. | adguard-home-agent_settings_toolset | settings | adguard-home-agent |
| Adguard-Home Rewrites Specialist | Expert specialist for rewrites domain tasks. | You are a Adguard-Home Rewrites specialist. Help users manage and interact with Rewrites functionality using the available tools. | adguard-home-agent_rewrites_toolset | rewrites | adguard-home-agent |
| Adguard-Home Filtering Specialist | Expert specialist for filtering domain tasks. | You are a Adguard-Home Filtering specialist. Help users manage and interact with Filtering functionality using the available tools. | adguard-home-agent_filtering_toolset | filtering | adguard-home-agent |
| Adguard-Home Tls Specialist | Expert specialist for tls domain tasks. | You are a Adguard-Home Tls specialist. Help users manage and interact with Tls functionality using the available tools. | adguard-home-agent_tls_toolset | tls | adguard-home-agent |
| Adguard-Home Mobile Specialist | Expert specialist for mobile domain tasks. | You are a Adguard-Home Mobile specialist. Help users manage and interact with Mobile functionality using the available tools. | adguard-home-agent_mobile_toolset | mobile | adguard-home-agent |
| Adguard-Home Stats Specialist | Expert specialist for stats domain tasks. | You are a Adguard-Home Stats specialist. Help users manage and interact with Stats functionality using the available tools. | adguard-home-agent_stats_toolset | stats | adguard-home-agent |
| Adguard-Home Clients Specialist | Expert specialist for clients domain tasks. | You are a Adguard-Home Clients specialist. Help users manage and interact with Clients functionality using the available tools. | adguard-home-agent_clients_toolset | clients | adguard-home-agent |
| Adguard-Home Dns Specialist | Expert specialist for dns domain tasks. | You are a Adguard-Home Dns specialist. Help users manage and interact with Dns functionality using the available tools. | adguard-home-agent_dns_toolset | dns | adguard-home-agent |
| Adguard-Home Profile Specialist | Expert specialist for profile domain tasks. | You are a Adguard-Home Profile specialist. Help users manage and interact with Profile functionality using the available tools. | adguard-home-agent_profile_toolset | profile | adguard-home-agent |
| Adguard-Home Query Log Specialist | Expert specialist for query_log domain tasks. | You are a Adguard-Home Query Log specialist. Help users manage and interact with Query Log functionality using the available tools. | adguard-home-agent_query_log_toolset | query_log | adguard-home-agent |
| Adguard-Home Misc Specialist | Expert specialist for misc domain tasks. | You are a Adguard-Home Misc specialist. Help users manage and interact with Misc functionality using the available tools. | adguard-home-agent_misc_toolset, archivebox-mcp_misc_toolset, audio-transcriber-mcp_misc_toolset, container-manager-mcp_misc_toolset, documentdb-mcp_misc_toolset, gitlab-api_misc_toolset, jellyfin-mcp_misc_toolset, media-downloader-mcp_misc_toolset, microsoft-agent_misc_toolset, nextcloud-agent_misc_toolset, repository-manager_misc_toolset, searxng-mcp_misc_toolset, servicenow-api_misc_toolset, systems-manager_misc_toolset, vector-mcp_misc_toolset | misc | adguard-home-agent |
| Ansible-Tower Specialist | Expert specialist for ansible-tower domain tasks. | You are a Ansible-Tower specialist. Help users manage and interact with Ansible-Tower functionality using the available tools. | ansible-tower-mcp_general_tools | ansible-tower | ansible-tower-mcp |
| Archivebox Authentication Specialist | Expert specialist for authentication domain tasks. | You are a Archivebox Authentication specialist. Help users manage and interact with Authentication functionality using the available tools. | archivebox-mcp_authentication_toolset | authentication | archivebox-mcp |
| Archivebox Cli Specialist | Expert specialist for cli domain tasks. | You are a Archivebox Cli specialist. Help users manage and interact with Cli functionality using the available tools. | archivebox-mcp_cli_toolset | cli | archivebox-mcp |
| Archivebox Core Specialist | Expert specialist for core domain tasks. | You are a Archivebox Core specialist. Help users manage and interact with Core functionality using the available tools. | archivebox-mcp_core_toolset | core | archivebox-mcp |
| Sonarr Downloads Specialist | Expert specialist for sonarr_downloads domain tasks. | You are a Sonarr Downloads specialist. Help users manage and interact with Sonarr Downloads functionality using the available tools. | arr-mcp_sonarr_downloads_toolset | sonarr_downloads | arr-mcp |
| Prowlarr System Specialist | Expert specialist for prowlarr_system domain tasks. | You are a Prowlarr System specialist. Help users manage and interact with Prowlarr System functionality using the available tools. | arr-mcp_prowlarr_system_toolset | prowlarr_system | arr-mcp |
| Prowlarr History Specialist | Expert specialist for prowlarr_history domain tasks. | You are a Prowlarr History specialist. Help users manage and interact with Prowlarr History functionality using the available tools. | arr-mcp_prowlarr_history_toolset | prowlarr_history | arr-mcp |
| Chaptarr Queue Specialist | Expert specialist for chaptarr_queue domain tasks. | You are a Chaptarr Queue specialist. Help users manage and interact with Chaptarr Queue functionality using the available tools. | arr-mcp_chaptarr_queue_toolset | chaptarr_queue | arr-mcp |
| Prowlarr Search Specialist | Expert specialist for prowlarr_search domain tasks. | You are a Prowlarr Search specialist. Help users manage and interact with Prowlarr Search functionality using the available tools. | arr-mcp_prowlarr_search_toolset | prowlarr_search | arr-mcp |
| Lidarr Config Specialist | Expert specialist for lidarr_config domain tasks. | You are a Lidarr Config specialist. Help users manage and interact with Lidarr Config functionality using the available tools. | arr-mcp_lidarr_config_toolset | lidarr_config | arr-mcp |
| Sonarr System Specialist | Expert specialist for sonarr_system domain tasks. | You are a Sonarr System specialist. Help users manage and interact with Sonarr System functionality using the available tools. | arr-mcp_sonarr_system_toolset | sonarr_system | arr-mcp |
| Sonarr Profiles Specialist | Expert specialist for sonarr_profiles domain tasks. | You are a Sonarr Profiles specialist. Help users manage and interact with Sonarr Profiles functionality using the available tools. | arr-mcp_sonarr_profiles_toolset | sonarr_profiles | arr-mcp |
| Lidarr History Specialist | Expert specialist for lidarr_history domain tasks. | You are a Lidarr History specialist. Help users manage and interact with Lidarr History functionality using the available tools. | arr-mcp_lidarr_history_toolset | lidarr_history | arr-mcp |
| Lidarr Catalog Specialist | Expert specialist for lidarr_catalog domain tasks. | You are a Lidarr Catalog specialist. Help users manage and interact with Lidarr Catalog functionality using the available tools. | arr-mcp_lidarr_catalog_toolset | lidarr_catalog | arr-mcp |
| Bazarr Catalog Specialist | Expert specialist for bazarr_catalog domain tasks. | You are a Bazarr Catalog specialist. Help users manage and interact with Bazarr Catalog functionality using the available tools. | arr-mcp_bazarr_catalog_toolset | bazarr_catalog | arr-mcp |
| Bazarr History Specialist | Expert specialist for bazarr_history domain tasks. | You are a Bazarr History specialist. Help users manage and interact with Bazarr History functionality using the available tools. | arr-mcp_bazarr_history_toolset | bazarr_history | arr-mcp |
| Sonarr History Specialist | Expert specialist for sonarr_history domain tasks. | You are a Sonarr History specialist. Help users manage and interact with Sonarr History functionality using the available tools. | arr-mcp_sonarr_history_toolset | sonarr_history | arr-mcp |
| Sonarr Queue Specialist | Expert specialist for sonarr_queue domain tasks. | You are a Sonarr Queue specialist. Help users manage and interact with Sonarr Queue functionality using the available tools. | arr-mcp_sonarr_queue_toolset | sonarr_queue | arr-mcp |
| Radarr Downloads Specialist | Expert specialist for radarr_downloads domain tasks. | You are a Radarr Downloads specialist. Help users manage and interact with Radarr Downloads functionality using the available tools. | arr-mcp_radarr_downloads_toolset | radarr_downloads | arr-mcp |
| Chaptarr Downloads Specialist | Expert specialist for chaptarr_downloads domain tasks. | You are a Chaptarr Downloads specialist. Help users manage and interact with Chaptarr Downloads functionality using the available tools. | arr-mcp_chaptarr_downloads_toolset | chaptarr_downloads | arr-mcp |
| Chaptarr History Specialist | Expert specialist for chaptarr_history domain tasks. | You are a Chaptarr History specialist. Help users manage and interact with Chaptarr History functionality using the available tools. | arr-mcp_chaptarr_history_toolset | chaptarr_history | arr-mcp |
| Lidarr Downloads Specialist | Expert specialist for lidarr_downloads domain tasks. | You are a Lidarr Downloads specialist. Help users manage and interact with Lidarr Downloads functionality using the available tools. | arr-mcp_lidarr_downloads_toolset | lidarr_downloads | arr-mcp |
| Lidarr Profiles Specialist | Expert specialist for lidarr_profiles domain tasks. | You are a Lidarr Profiles specialist. Help users manage and interact with Lidarr Profiles functionality using the available tools. | arr-mcp_lidarr_profiles_toolset | lidarr_profiles | arr-mcp |
| Chaptarr Config Specialist | Expert specialist for chaptarr_config domain tasks. | You are a Chaptarr Config specialist. Help users manage and interact with Chaptarr Config functionality using the available tools. | arr-mcp_chaptarr_config_toolset | chaptarr_config | arr-mcp |
| Radarr Indexer Specialist | Expert specialist for radarr_indexer domain tasks. | You are a Radarr Indexer specialist. Help users manage and interact with Radarr Indexer functionality using the available tools. | arr-mcp_radarr_indexer_toolset | radarr_indexer | arr-mcp |
| Chaptarr Indexer Specialist | Expert specialist for chaptarr_indexer domain tasks. | You are a Chaptarr Indexer specialist. Help users manage and interact with Chaptarr Indexer functionality using the available tools. | arr-mcp_chaptarr_indexer_toolset | chaptarr_indexer | arr-mcp |
| Radarr Catalog Specialist | Expert specialist for radarr_catalog domain tasks. | You are a Radarr Catalog specialist. Help users manage and interact with Radarr Catalog functionality using the available tools. | arr-mcp_radarr_catalog_toolset | radarr_catalog | arr-mcp |
| Radarr Profiles Specialist | Expert specialist for radarr_profiles domain tasks. | You are a Radarr Profiles specialist. Help users manage and interact with Radarr Profiles functionality using the available tools. | arr-mcp_radarr_profiles_toolset | radarr_profiles | arr-mcp |
| Bazarr System Specialist | Expert specialist for bazarr_system domain tasks. | You are a Bazarr System specialist. Help users manage and interact with Bazarr System functionality using the available tools. | arr-mcp_bazarr_system_toolset | bazarr_system | arr-mcp |
| Chaptarr Profiles Specialist | Expert specialist for chaptarr_profiles domain tasks. | You are a Chaptarr Profiles specialist. Help users manage and interact with Chaptarr Profiles functionality using the available tools. | arr-mcp_chaptarr_profiles_toolset | chaptarr_profiles | arr-mcp |
| Lidarr Indexer Specialist | Expert specialist for lidarr_indexer domain tasks. | You are a Lidarr Indexer specialist. Help users manage and interact with Lidarr Indexer functionality using the available tools. | arr-mcp_lidarr_indexer_toolset | lidarr_indexer | arr-mcp |
| Arr Seerr System Specialist | Expert specialist for seerr_system domain tasks. | You are a Arr Seerr System specialist. Help users manage and interact with Seerr System functionality using the available tools. | arr-mcp_seerr_system_toolset | seerr_system | arr-mcp |
| Chaptarr Search Specialist | Expert specialist for chaptarr_search domain tasks. | You are a Chaptarr Search specialist. Help users manage and interact with Chaptarr Search functionality using the available tools. | arr-mcp_chaptarr_search_toolset | chaptarr_search | arr-mcp |
| Radarr History Specialist | Expert specialist for radarr_history domain tasks. | You are a Radarr History specialist. Help users manage and interact with Radarr History functionality using the available tools. | arr-mcp_radarr_history_toolset | radarr_history | arr-mcp |
| Prowlarr Config Specialist | Expert specialist for prowlarr_config domain tasks. | You are a Prowlarr Config specialist. Help users manage and interact with Prowlarr Config functionality using the available tools. | arr-mcp_prowlarr_config_toolset | prowlarr_config | arr-mcp |
| Sonarr Config Specialist | Expert specialist for sonarr_config domain tasks. | You are a Sonarr Config specialist. Help users manage and interact with Sonarr Config functionality using the available tools. | arr-mcp_sonarr_config_toolset | sonarr_config | arr-mcp |
| Chaptarr Operations Specialist | Expert specialist for chaptarr_operations domain tasks. | You are a Chaptarr Operations specialist. Help users manage and interact with Chaptarr Operations functionality using the available tools. | arr-mcp_chaptarr_operations_toolset | chaptarr_operations | arr-mcp |
| Arr Seerr Catalog Specialist | Expert specialist for seerr_catalog domain tasks. | You are a Arr Seerr Catalog specialist. Help users manage and interact with Seerr Catalog functionality using the available tools. | arr-mcp_seerr_catalog_toolset | seerr_catalog | arr-mcp |
| Prowlarr Indexer Specialist | Expert specialist for prowlarr_indexer domain tasks. | You are a Prowlarr Indexer specialist. Help users manage and interact with Prowlarr Indexer functionality using the available tools. | arr-mcp_prowlarr_indexer_toolset | prowlarr_indexer | arr-mcp |
| Prowlarr Operations Specialist | Expert specialist for prowlarr_operations domain tasks. | You are a Prowlarr Operations specialist. Help users manage and interact with Prowlarr Operations functionality using the available tools. | arr-mcp_prowlarr_operations_toolset | prowlarr_operations | arr-mcp |
| Prowlarr Downloads Specialist | Expert specialist for prowlarr_downloads domain tasks. | You are a Prowlarr Downloads specialist. Help users manage and interact with Prowlarr Downloads functionality using the available tools. | arr-mcp_prowlarr_downloads_toolset | prowlarr_downloads | arr-mcp |
| Radarr Config Specialist | Expert specialist for radarr_config domain tasks. | You are a Radarr Config specialist. Help users manage and interact with Radarr Config functionality using the available tools. | arr-mcp_radarr_config_toolset | radarr_config | arr-mcp |
| Prowlarr Profiles Specialist | Expert specialist for prowlarr_profiles domain tasks. | You are a Prowlarr Profiles specialist. Help users manage and interact with Prowlarr Profiles functionality using the available tools. | arr-mcp_prowlarr_profiles_toolset | prowlarr_profiles | arr-mcp |
| Sonarr Catalog Specialist | Expert specialist for sonarr_catalog domain tasks. | You are a Sonarr Catalog specialist. Help users manage and interact with Sonarr Catalog functionality using the available tools. | arr-mcp_sonarr_catalog_toolset | sonarr_catalog | arr-mcp |
| Sonarr Indexer Specialist | Expert specialist for sonarr_indexer domain tasks. | You are a Sonarr Indexer specialist. Help users manage and interact with Sonarr Indexer functionality using the available tools. | arr-mcp_sonarr_indexer_toolset | sonarr_indexer | arr-mcp |
| Sonarr Operations Specialist | Expert specialist for sonarr_operations domain tasks. | You are a Sonarr Operations specialist. Help users manage and interact with Sonarr Operations functionality using the available tools. | arr-mcp_sonarr_operations_toolset | sonarr_operations | arr-mcp |
| Lidarr System Specialist | Expert specialist for lidarr_system domain tasks. | You are a Lidarr System specialist. Help users manage and interact with Lidarr System functionality using the available tools. | arr-mcp_lidarr_system_toolset | lidarr_system | arr-mcp |
| Radarr System Specialist | Expert specialist for radarr_system domain tasks. | You are a Radarr System specialist. Help users manage and interact with Radarr System functionality using the available tools. | arr-mcp_radarr_system_toolset | radarr_system | arr-mcp |
| Radarr Queue Specialist | Expert specialist for radarr_queue domain tasks. | You are a Radarr Queue specialist. Help users manage and interact with Radarr Queue functionality using the available tools. | arr-mcp_radarr_queue_toolset | radarr_queue | arr-mcp |
| Lidarr Queue Specialist | Expert specialist for lidarr_queue domain tasks. | You are a Lidarr Queue specialist. Help users manage and interact with Lidarr Queue functionality using the available tools. | arr-mcp_lidarr_queue_toolset | lidarr_queue | arr-mcp |
| Arr Seerr Search Specialist | Expert specialist for seerr_search domain tasks. | You are a Arr Seerr Search specialist. Help users manage and interact with Seerr Search functionality using the available tools. | arr-mcp_seerr_search_toolset | seerr_search | arr-mcp |
| Chaptarr System Specialist | Expert specialist for chaptarr_system domain tasks. | You are a Chaptarr System specialist. Help users manage and interact with Chaptarr System functionality using the available tools. | arr-mcp_chaptarr_system_toolset | chaptarr_system | arr-mcp |
| Radarr Operations Specialist | Expert specialist for radarr_operations domain tasks. | You are a Radarr Operations specialist. Help users manage and interact with Radarr Operations functionality using the available tools. | arr-mcp_radarr_operations_toolset | radarr_operations | arr-mcp |
| Lidarr Operations Specialist | Expert specialist for lidarr_operations domain tasks. | You are a Lidarr Operations specialist. Help users manage and interact with Lidarr Operations functionality using the available tools. | arr-mcp_lidarr_operations_toolset | lidarr_operations | arr-mcp |
| Lidarr Search Specialist | Expert specialist for lidarr_search domain tasks. | You are a Lidarr Search specialist. Help users manage and interact with Lidarr Search functionality using the available tools. | arr-mcp_lidarr_search_toolset | lidarr_search | arr-mcp |
| Atlassian Specialist | Expert specialist for atlassian domain tasks. | You are a Atlassian specialist. Help users manage and interact with Atlassian functionality using the available tools. | atlassian_general_tools | atlassian | atlassian |
| Audio-Transcriber Audio Processing Specialist | Expert specialist for audio_processing domain tasks. | You are a Audio-Transcriber Audio Processing specialist. Help users manage and interact with Audio Processing functionality using the available tools. | audio-transcriber-mcp_audio_processing_toolset | audio_processing | audio-transcriber-mcp |
| Container-Manager Log Specialist | Expert specialist for log domain tasks. | You are a Container-Manager Log specialist. Help users manage and interact with Log functionality using the available tools. | container-manager-mcp_log_toolset, systems-manager_log_toolset | log | container-manager-mcp |
| Container-Manager Info Specialist | Expert specialist for info domain tasks. | You are a Container-Manager Info specialist. Help users manage and interact with Info functionality using the available tools. | container-manager-mcp_info_toolset | info | container-manager-mcp |
| Container-Manager Image Specialist | Expert specialist for image domain tasks. | You are a Container-Manager Image specialist. Help users manage and interact with Image functionality using the available tools. | container-manager-mcp_image_toolset, jellyfin-mcp_image_toolset | image | container-manager-mcp |
| Container-Manager Network Specialist | Expert specialist for network domain tasks. | You are a Container-Manager Network specialist. Help users manage and interact with Network functionality using the available tools. | container-manager-mcp_network_toolset, systems-manager_network_toolset | network | container-manager-mcp |
| Container-Manager Swarm Specialist | Expert specialist for swarm domain tasks. | You are a Container-Manager Swarm specialist. Help users manage and interact with Swarm functionality using the available tools. | container-manager-mcp_swarm_toolset | swarm | container-manager-mcp |
| Container-Manager Container Specialist | Expert specialist for container domain tasks. | You are a Container-Manager Container specialist. Help users manage and interact with Container functionality using the available tools. | container-manager-mcp_container_toolset | container | container-manager-mcp |
| Container-Manager Compose Specialist | Expert specialist for compose domain tasks. | You are a Container-Manager Compose specialist. Help users manage and interact with Compose functionality using the available tools. | container-manager-mcp_compose_toolset | compose | container-manager-mcp |
| Container-Manager Volume Specialist | Expert specialist for volume domain tasks. | You are a Container-Manager Volume specialist. Help users manage and interact with Volume functionality using the available tools. | container-manager-mcp_volume_toolset | volume | container-manager-mcp |
| Documentdb Analysis Specialist | Expert specialist for analysis domain tasks. | You are a Documentdb Analysis specialist. Help users manage and interact with Analysis functionality using the available tools. | documentdb-mcp_analysis_toolset | analysis | documentdb-mcp |
| Documentdb Users Specialist | Expert specialist for users domain tasks. | You are a Documentdb Users specialist. Help users manage and interact with Users functionality using the available tools. | documentdb-mcp_users_toolset, get_token, oauth_login, oauth_callback, refresh_token, logout, register_new_user, get_logged_in_user, get_logged_in_user_ratings, get_logged_in_user_rating_for_recipe, get_logged_in_user_favorites, update_password, update_user, forgot_password, reset_password, update_user_image, create, delete, get_ratings, get_favorites, set_rating, add_favorite, remove_favorite, list_users, get_me | users | documentdb-mcp |
| Documentdb Collections Specialist | Expert specialist for collections domain tasks. | You are a Documentdb Collections specialist. Help users manage and interact with Collections functionality using the available tools. | documentdb-mcp_collections_toolset | collections | documentdb-mcp |
| Documentdb Crud Specialist | Expert specialist for crud domain tasks. | You are a Documentdb Crud specialist. Help users manage and interact with Crud functionality using the available tools. | documentdb-mcp_crud_toolset | crud | documentdb-mcp |
| Github Repos Specialist | Expert specialist for repos domain tasks. | You are a Github Repos specialist. Help users manage and interact with Repos functionality using the available tools. | github_list_repos, github_get_repo | repos | github-mcp |
| Github Issues Specialist | Expert specialist for issues domain tasks. | You are a Github Issues specialist. Help users manage and interact with Issues functionality using the available tools. | github_list_issues | issues | github-mcp |
| Github Pulls Specialist | Expert specialist for pulls domain tasks. | You are a Github Pulls specialist. Help users manage and interact with Pulls functionality using the available tools. | github_list_pull_requests | pulls | github-mcp |
| Github Contents Specialist | Expert specialist for contents domain tasks. | You are a Github Contents specialist. Help users manage and interact with Contents functionality using the available tools. | github_get_contents | contents | github-mcp |
| Gitlab-Api Groups Specialist | Expert specialist for groups domain tasks. | You are a Gitlab-Api Groups specialist. Help users manage and interact with Groups functionality using the available tools. | gitlab-api_groups_toolset, get_all_households, get_one_household, get_logged_in_user_group, get_group_members, get_group_member, get_group_preferences, update_group_preferences, get_storage, start_data_migration, get_groups_reports, get_groups_reports_item_id, delete_groups_reports_item_id, get_groups_labels, post_groups_labels, get_groups_labels_item_id, put_groups_labels_item_id, delete_groups_labels_item_id, seed_foods, seed_labels, seed_units, microsoft-agent_groups_toolset | groups | gitlab-api |
| Gitlab-Api Protected Branches Specialist | Expert specialist for protected_branches domain tasks. | You are a Gitlab-Api Protected Branches specialist. Help users manage and interact with Protected Branches functionality using the available tools. | gitlab-api_protected_branches_toolset | protected_branches | gitlab-api |
| Gitlab-Api Pipelines Specialist | Expert specialist for pipelines domain tasks. | You are a Gitlab-Api Pipelines specialist. Help users manage and interact with Pipelines functionality using the available tools. | gitlab-api_pipelines_toolset | pipelines | gitlab-api |
| Gitlab-Api Merge Requests Specialist | Expert specialist for merge_requests domain tasks. | You are a Gitlab-Api Merge Requests specialist. Help users manage and interact with Merge Requests functionality using the available tools. | gitlab-api_merge_requests_toolset | merge_requests | gitlab-api |
| Gitlab-Api Packages Specialist | Expert specialist for packages domain tasks. | You are a Gitlab-Api Packages specialist. Help users manage and interact with Packages functionality using the available tools. | gitlab-api_packages_toolset | packages | gitlab-api |
| Gitlab-Api Deploy Tokens Specialist | Expert specialist for deploy_tokens domain tasks. | You are a Gitlab-Api Deploy Tokens specialist. Help users manage and interact with Deploy Tokens functionality using the available tools. | gitlab-api_deploy_tokens_toolset | deploy_tokens | gitlab-api |
| Gitlab-Api Custom Api Specialist | Expert specialist for custom_api domain tasks. | You are a Gitlab-Api Custom Api specialist. Help users manage and interact with Custom Api functionality using the available tools. | gitlab-api_custom_api_toolset, servicenow-api_custom_api_toolset | custom_api | gitlab-api |
| Gitlab-Api Pipeline Schedules Specialist | Expert specialist for pipeline_schedules domain tasks. | You are a Gitlab-Api Pipeline Schedules specialist. Help users manage and interact with Pipeline Schedules functionality using the available tools. | gitlab-api_pipeline_schedules_toolset | pipeline_schedules | gitlab-api |
| Gitlab-Api Merge Rules Specialist | Expert specialist for merge_rules domain tasks. | You are a Gitlab-Api Merge Rules specialist. Help users manage and interact with Merge Rules functionality using the available tools. | gitlab-api_merge_rules_toolset | merge_rules | gitlab-api |
| Gitlab-Api Commits Specialist | Expert specialist for commits domain tasks. | You are a Gitlab-Api Commits specialist. Help users manage and interact with Commits functionality using the available tools. | gitlab-api_commits_toolset | commits | gitlab-api |
| Gitlab-Api Branches Specialist | Expert specialist for branches domain tasks. | You are a Gitlab-Api Branches specialist. Help users manage and interact with Branches functionality using the available tools. | gitlab-api_branches_toolset | branches | gitlab-api |
| Gitlab-Api Jobs Specialist | Expert specialist for jobs domain tasks. | You are a Gitlab-Api Jobs specialist. Help users manage and interact with Jobs functionality using the available tools. | gitlab-api_jobs_toolset | jobs | gitlab-api |
| Gitlab-Api Tags Specialist | Expert specialist for tags domain tasks. | You are a Gitlab-Api Tags specialist. Help users manage and interact with Tags functionality using the available tools. | gitlab-api_tags_toolset | tags | gitlab-api |
| Gitlab-Api Members Specialist | Expert specialist for members domain tasks. | You are a Gitlab-Api Members specialist. Help users manage and interact with Members functionality using the available tools. | gitlab-api_members_toolset | members | gitlab-api |
| Gitlab-Api Environments Specialist | Expert specialist for environments domain tasks. | You are a Gitlab-Api Environments specialist. Help users manage and interact with Environments functionality using the available tools. | gitlab-api_environments_toolset | environments | gitlab-api |
| Gitlab-Api Projects Specialist | Expert specialist for projects domain tasks. | You are a Gitlab-Api Projects specialist. Help users manage and interact with Projects functionality using the available tools. | gitlab-api_projects_toolset, list_projects, retrieve_project | projects | gitlab-api |
| Gitlab-Api Releases Specialist | Expert specialist for releases domain tasks. | You are a Gitlab-Api Releases specialist. Help users manage and interact with Releases functionality using the available tools. | gitlab-api_releases_toolset | releases | gitlab-api |
| Gitlab-Api Runners Specialist | Expert specialist for runners domain tasks. | You are a Gitlab-Api Runners specialist. Help users manage and interact with Runners functionality using the available tools. | gitlab-api_runners_toolset | runners | gitlab-api |
| Home Specialist | Expert specialist for home domain tasks. | You are a Home specialist. Help users manage and interact with Home functionality using the available tools. | home_general_tools | home | home |
| Jellyfin Itemrefresh Specialist | Expert specialist for itemrefresh domain tasks. | You are a Jellyfin Itemrefresh specialist. Help users manage and interact with Itemrefresh functionality using the available tools. | jellyfin-mcp_itemrefresh_toolset | itemrefresh | jellyfin-mcp |
| Jellyfin Collection Specialist | Expert specialist for collection domain tasks. | You are a Jellyfin Collection specialist. Help users manage and interact with Collection functionality using the available tools. | jellyfin-mcp_collection_toolset | collection | jellyfin-mcp |
| Jellyfin Tvshows Specialist | Expert specialist for tvshows domain tasks. | You are a Jellyfin Tvshows specialist. Help users manage and interact with Tvshows functionality using the available tools. | jellyfin-mcp_tvshows_toolset | tvshows | jellyfin-mcp |
| Jellyfin Scheduledtasks Specialist | Expert specialist for scheduledtasks domain tasks. | You are a Jellyfin Scheduledtasks specialist. Help users manage and interact with Scheduledtasks functionality using the available tools. | jellyfin-mcp_scheduledtasks_toolset | scheduledtasks | jellyfin-mcp |
| Jellyfin Tmdb Specialist | Expert specialist for tmdb domain tasks. | You are a Jellyfin Tmdb specialist. Help users manage and interact with Tmdb functionality using the available tools. | jellyfin-mcp_tmdb_toolset | tmdb | jellyfin-mcp |
| Jellyfin Dashboard Specialist | Expert specialist for dashboard domain tasks. | You are a Jellyfin Dashboard specialist. Help users manage and interact with Dashboard functionality using the available tools. | jellyfin-mcp_dashboard_toolset | dashboard | jellyfin-mcp |
| Jellyfin Clientlog Specialist | Expert specialist for clientlog domain tasks. | You are a Jellyfin Clientlog specialist. Help users manage and interact with Clientlog functionality using the available tools. | jellyfin-mcp_clientlog_toolset | clientlog | jellyfin-mcp |
| Jellyfin Search Specialist | Expert specialist for search domain tasks. | You are a Jellyfin Search specialist. Help users manage and interact with Search functionality using the available tools. | jellyfin-mcp_search_toolset, microsoft-agent_search_toolset, searxng-mcp_search_toolset, vector-mcp_search_toolset | search | jellyfin-mcp |
| Jellyfin Backup Specialist | Expert specialist for backup domain tasks. | You are a Jellyfin Backup specialist. Help users manage and interact with Backup functionality using the available tools. | jellyfin-mcp_backup_toolset | backup | jellyfin-mcp |
| Jellyfin Mediasegments Specialist | Expert specialist for mediasegments domain tasks. | You are a Jellyfin Mediasegments specialist. Help users manage and interact with Mediasegments functionality using the available tools. | jellyfin-mcp_mediasegments_toolset | mediasegments | jellyfin-mcp |
| Jellyfin Hlssegment Specialist | Expert specialist for hlssegment domain tasks. | You are a Jellyfin Hlssegment specialist. Help users manage and interact with Hlssegment functionality using the available tools. | jellyfin-mcp_hlssegment_toolset | hlssegment | jellyfin-mcp |
| Jellyfin Displaypreferences Specialist | Expert specialist for displaypreferences domain tasks. | You are a Jellyfin Displaypreferences specialist. Help users manage and interact with Displaypreferences functionality using the available tools. | jellyfin-mcp_displaypreferences_toolset | displaypreferences | jellyfin-mcp |
| Jellyfin Livetv Specialist | Expert specialist for livetv domain tasks. | You are a Jellyfin Livetv specialist. Help users manage and interact with Livetv functionality using the available tools. | jellyfin-mcp_livetv_toolset | livetv | jellyfin-mcp |
| Jellyfin Videoattachments Specialist | Expert specialist for videoattachments domain tasks. | You are a Jellyfin Videoattachments specialist. Help users manage and interact with Videoattachments functionality using the available tools. | jellyfin-mcp_videoattachments_toolset | videoattachments | jellyfin-mcp |
| Jellyfin Channels Specialist | Expert specialist for channels domain tasks. | You are a Jellyfin Channels specialist. Help users manage and interact with Channels functionality using the available tools. | jellyfin-mcp_channels_toolset | channels | jellyfin-mcp |
| Jellyfin Dynamichls Specialist | Expert specialist for dynamichls domain tasks. | You are a Jellyfin Dynamichls specialist. Help users manage and interact with Dynamichls functionality using the available tools. | jellyfin-mcp_dynamichls_toolset | dynamichls | jellyfin-mcp |
| Jellyfin Library Specialist | Expert specialist for library domain tasks. | You are a Jellyfin Library specialist. Help users manage and interact with Library functionality using the available tools. | jellyfin-mcp_library_toolset | library | jellyfin-mcp |
| Jellyfin Audio Specialist | Expert specialist for audio domain tasks. | You are a Jellyfin Audio specialist. Help users manage and interact with Audio functionality using the available tools. | jellyfin-mcp_audio_toolset | audio | jellyfin-mcp |
| Jellyfin Plugins Specialist | Expert specialist for plugins domain tasks. | You are a Jellyfin Plugins specialist. Help users manage and interact with Plugins functionality using the available tools. | jellyfin-mcp_plugins_toolset, servicenow-api_plugins_toolset | plugins | jellyfin-mcp |
| Jellyfin Session Specialist | Expert specialist for session domain tasks. | You are a Jellyfin Session specialist. Help users manage and interact with Session functionality using the available tools. | jellyfin-mcp_session_toolset | session | jellyfin-mcp |
| Jellyfin Studios Specialist | Expert specialist for studios domain tasks. | You are a Jellyfin Studios specialist. Help users manage and interact with Studios functionality using the available tools. | jellyfin-mcp_studios_toolset | studios | jellyfin-mcp |
| Jellyfin Environment Specialist | Expert specialist for environment domain tasks. | You are a Jellyfin Environment specialist. Help users manage and interact with Environment functionality using the available tools. | jellyfin-mcp_environment_toolset | environment | jellyfin-mcp |
| Jellyfin Persons Specialist | Expert specialist for persons domain tasks. | You are a Jellyfin Persons specialist. Help users manage and interact with Persons functionality using the available tools. | jellyfin-mcp_persons_toolset | persons | jellyfin-mcp |
| Jellyfin Trickplay Specialist | Expert specialist for trickplay domain tasks. | You are a Jellyfin Trickplay specialist. Help users manage and interact with Trickplay functionality using the available tools. | jellyfin-mcp_trickplay_toolset | trickplay | jellyfin-mcp |
| Jellyfin Instantmix Specialist | Expert specialist for instantmix domain tasks. | You are a Jellyfin Instantmix specialist. Help users manage and interact with Instantmix functionality using the available tools. | jellyfin-mcp_instantmix_toolset | instantmix | jellyfin-mcp |
| Jellyfin Movies Specialist | Expert specialist for movies domain tasks. | You are a Jellyfin Movies specialist. Help users manage and interact with Movies functionality using the available tools. | jellyfin-mcp_movies_toolset | movies | jellyfin-mcp |
| Jellyfin Syncplay Specialist | Expert specialist for syncplay domain tasks. | You are a Jellyfin Syncplay specialist. Help users manage and interact with Syncplay functionality using the available tools. | jellyfin-mcp_syncplay_toolset | syncplay | jellyfin-mcp |
| Jellyfin Startup Specialist | Expert specialist for startup domain tasks. | You are a Jellyfin Startup specialist. Help users manage and interact with Startup functionality using the available tools. | jellyfin-mcp_startup_toolset | startup | jellyfin-mcp |
| Jellyfin Universalaudio Specialist | Expert specialist for universalaudio domain tasks. | You are a Jellyfin Universalaudio specialist. Help users manage and interact with Universalaudio functionality using the available tools. | jellyfin-mcp_universalaudio_toolset | universalaudio | jellyfin-mcp |
| Jellyfin User Specialist | Expert specialist for user domain tasks. | You are a Jellyfin User specialist. Help users manage and interact with User functionality using the available tools. | jellyfin-mcp_user_toolset, microsoft-agent_user_toolset, nextcloud-agent_user_toolset, systems-manager_user_toolset | user | jellyfin-mcp |
| Jellyfin Musicgenres Specialist | Expert specialist for musicgenres domain tasks. | You are a Jellyfin Musicgenres specialist. Help users manage and interact with Musicgenres functionality using the available tools. | jellyfin-mcp_musicgenres_toolset | musicgenres | jellyfin-mcp |
| Jellyfin Suggestions Specialist | Expert specialist for suggestions domain tasks. | You are a Jellyfin Suggestions specialist. Help users manage and interact with Suggestions functionality using the available tools. | jellyfin-mcp_suggestions_toolset | suggestions | jellyfin-mcp |
| Jellyfin Timesync Specialist | Expert specialist for timesync domain tasks. | You are a Jellyfin Timesync specialist. Help users manage and interact with Timesync functionality using the available tools. | jellyfin-mcp_timesync_toolset | timesync | jellyfin-mcp |
| Jellyfin Artists Specialist | Expert specialist for artists domain tasks. | You are a Jellyfin Artists specialist. Help users manage and interact with Artists functionality using the available tools. | jellyfin-mcp_artists_toolset | artists | jellyfin-mcp |
| Jellyfin Localization Specialist | Expert specialist for localization domain tasks. | You are a Jellyfin Localization specialist. Help users manage and interact with Localization functionality using the available tools. | jellyfin-mcp_localization_toolset | localization | jellyfin-mcp |
| Jellyfin Itemupdate Specialist | Expert specialist for itemupdate domain tasks. | You are a Jellyfin Itemupdate specialist. Help users manage and interact with Itemupdate functionality using the available tools. | jellyfin-mcp_itemupdate_toolset | itemupdate | jellyfin-mcp |
| Jellyfin Librarystructure Specialist | Expert specialist for librarystructure domain tasks. | You are a Jellyfin Librarystructure specialist. Help users manage and interact with Librarystructure functionality using the available tools. | jellyfin-mcp_librarystructure_toolset | librarystructure | jellyfin-mcp |
| Jellyfin Mediainfo Specialist | Expert specialist for mediainfo domain tasks. | You are a Jellyfin Mediainfo specialist. Help users manage and interact with Mediainfo functionality using the available tools. | jellyfin-mcp_mediainfo_toolset | mediainfo | jellyfin-mcp |
| Jellyfin Quickconnect Specialist | Expert specialist for quickconnect domain tasks. | You are a Jellyfin Quickconnect specialist. Help users manage and interact with Quickconnect functionality using the available tools. | jellyfin-mcp_quickconnect_toolset | quickconnect | jellyfin-mcp |
| Jellyfin Videos Specialist | Expert specialist for videos domain tasks. | You are a Jellyfin Videos specialist. Help users manage and interact with Videos functionality using the available tools. | jellyfin-mcp_videos_toolset | videos | jellyfin-mcp |
| Jellyfin Remoteimage Specialist | Expert specialist for remoteimage domain tasks. | You are a Jellyfin Remoteimage specialist. Help users manage and interact with Remoteimage functionality using the available tools. | jellyfin-mcp_remoteimage_toolset | remoteimage | jellyfin-mcp |
| Jellyfin Playstate Specialist | Expert specialist for playstate domain tasks. | You are a Jellyfin Playstate specialist. Help users manage and interact with Playstate functionality using the available tools. | jellyfin-mcp_playstate_toolset | playstate | jellyfin-mcp |
| Jellyfin Apikey Specialist | Expert specialist for apikey domain tasks. | You are a Jellyfin Apikey specialist. Help users manage and interact with Apikey functionality using the available tools. | jellyfin-mcp_apikey_toolset | apikey | jellyfin-mcp |
| Jellyfin Devices Specialist | Expert specialist for devices domain tasks. | You are a Jellyfin Devices specialist. Help users manage and interact with Devices functionality using the available tools. | jellyfin-mcp_devices_toolset, microsoft-agent_devices_toolset | devices | jellyfin-mcp |
| Jellyfin Filter Specialist | Expert specialist for filter domain tasks. | You are a Jellyfin Filter specialist. Help users manage and interact with Filter functionality using the available tools. | jellyfin-mcp_filter_toolset | filter | jellyfin-mcp |
| Jellyfin Branding Specialist | Expert specialist for branding domain tasks. | You are a Jellyfin Branding specialist. Help users manage and interact with Branding functionality using the available tools. | jellyfin-mcp_branding_toolset | branding | jellyfin-mcp |
| Jellyfin Genres Specialist | Expert specialist for genres domain tasks. | You are a Jellyfin Genres specialist. Help users manage and interact with Genres functionality using the available tools. | jellyfin-mcp_genres_toolset | genres | jellyfin-mcp |
| Jellyfin Userviews Specialist | Expert specialist for userviews domain tasks. | You are a Jellyfin Userviews specialist. Help users manage and interact with Userviews functionality using the available tools. | jellyfin-mcp_userviews_toolset | userviews | jellyfin-mcp |
| Jellyfin Years Specialist | Expert specialist for years domain tasks. | You are a Jellyfin Years specialist. Help users manage and interact with Years functionality using the available tools. | jellyfin-mcp_years_toolset | years | jellyfin-mcp |
| Jellyfin Lyrics Specialist | Expert specialist for lyrics domain tasks. | You are a Jellyfin Lyrics specialist. Help users manage and interact with Lyrics functionality using the available tools. | jellyfin-mcp_lyrics_toolset | lyrics | jellyfin-mcp |
| Jellyfin Trailers Specialist | Expert specialist for trailers domain tasks. | You are a Jellyfin Trailers specialist. Help users manage and interact with Trailers functionality using the available tools. | jellyfin-mcp_trailers_toolset | trailers | jellyfin-mcp |
| Jellyfin Activitylog Specialist | Expert specialist for activitylog domain tasks. | You are a Jellyfin Activitylog specialist. Help users manage and interact with Activitylog functionality using the available tools. | jellyfin-mcp_activitylog_toolset | activitylog | jellyfin-mcp |
| Jellyfin Package Specialist | Expert specialist for package domain tasks. | You are a Jellyfin Package specialist. Help users manage and interact with Package functionality using the available tools. | jellyfin-mcp_package_toolset | package | jellyfin-mcp |
| Jellyfin Subtitle Specialist | Expert specialist for subtitle domain tasks. | You are a Jellyfin Subtitle specialist. Help users manage and interact with Subtitle functionality using the available tools. | jellyfin-mcp_subtitle_toolset | subtitle | jellyfin-mcp |
| Jellyfin Playlists Specialist | Expert specialist for playlists domain tasks. | You are a Jellyfin Playlists specialist. Help users manage and interact with Playlists functionality using the available tools. | jellyfin-mcp_playlists_toolset | playlists | jellyfin-mcp |
| Jellyfin Userlibrary Specialist | Expert specialist for userlibrary domain tasks. | You are a Jellyfin Userlibrary specialist. Help users manage and interact with Userlibrary functionality using the available tools. | jellyfin-mcp_userlibrary_toolset | userlibrary | jellyfin-mcp |
| Jellyfin Configuration Specialist | Expert specialist for configuration domain tasks. | You are a Jellyfin Configuration specialist. Help users manage and interact with Configuration functionality using the available tools. | jellyfin-mcp_configuration_toolset | configuration | jellyfin-mcp |
| Jellyfin Items Specialist | Expert specialist for items domain tasks. | You are a Jellyfin Items specialist. Help users manage and interact with Items functionality using the available tools. | jellyfin-mcp_items_toolset | items | jellyfin-mcp |
| Jellyfin Itemlookup Specialist | Expert specialist for itemlookup domain tasks. | You are a Jellyfin Itemlookup specialist. Help users manage and interact with Itemlookup functionality using the available tools. | jellyfin-mcp_itemlookup_toolset | itemlookup | jellyfin-mcp |
| Langfuse Annotation Queues  Specialist | Expert specialist for annotation_queues_ domain tasks. | You are a Langfuse Annotation Queues  specialist. Help users manage and interact with Annotation Queues  functionality using the available tools. | langfuse_annotation_queues__toolset | annotation_queues_ | langfuse |
| Langfuse Blob Storage Integrations  Specialist | Expert specialist for blob_storage_integrations_ domain tasks. | You are a Langfuse Blob Storage Integrations  specialist. Help users manage and interact with Blob Storage Integrations  functionality using the available tools. | langfuse_blob_storage_integrations__toolset | blob_storage_integrations_ | langfuse |
| Langfuse Comments  Specialist | Expert specialist for comments_ domain tasks. | You are a Langfuse Comments  specialist. Help users manage and interact with Comments  functionality using the available tools. | langfuse_comments__toolset | comments_ | langfuse |
| Langfuse Datasets  Specialist | Expert specialist for datasets_ domain tasks. | You are a Langfuse Datasets  specialist. Help users manage and interact with Datasets  functionality using the available tools. | langfuse_datasets__toolset | datasets_ | langfuse |
| Langfuse Dataset Items  Specialist | Expert specialist for dataset_items_ domain tasks. | You are a Langfuse Dataset Items  specialist. Help users manage and interact with Dataset Items  functionality using the available tools. | langfuse_dataset_items__toolset | dataset_items_ | langfuse |
| Langfuse Dataset Run Items  Specialist | Expert specialist for dataset_run_items_ domain tasks. | You are a Langfuse Dataset Run Items  specialist. Help users manage and interact with Dataset Run Items  functionality using the available tools. | langfuse_dataset_run_items__toolset | dataset_run_items_ | langfuse |
| Langfuse Health  Specialist | Expert specialist for health_ domain tasks. | You are a Langfuse Health  specialist. Help users manage and interact with Health  functionality using the available tools. | langfuse_health__toolset | health_ | langfuse |
| Langfuse Ingestion  Specialist | Expert specialist for ingestion_ domain tasks. | You are a Langfuse Ingestion  specialist. Help users manage and interact with Ingestion  functionality using the available tools. | langfuse_ingestion__toolset | ingestion_ | langfuse |
| Langfuse Legacy Metrics V1  Specialist | Expert specialist for legacy_metrics_v1_ domain tasks. | You are a Langfuse Legacy Metrics V1  specialist. Help users manage and interact with Legacy Metrics V1  functionality using the available tools. | langfuse_legacy_metrics_v1__toolset | legacy_metrics_v1_ | langfuse |
| Langfuse Legacy Observations V1  Specialist | Expert specialist for legacy_observations_v1_ domain tasks. | You are a Langfuse Legacy Observations V1  specialist. Help users manage and interact with Legacy Observations V1  functionality using the available tools. | langfuse_legacy_observations_v1__toolset | legacy_observations_v1_ | langfuse |
| Langfuse Legacy Score V1  Specialist | Expert specialist for legacy_score_v1_ domain tasks. | You are a Langfuse Legacy Score V1  specialist. Help users manage and interact with Legacy Score V1  functionality using the available tools. | langfuse_legacy_score_v1__toolset | legacy_score_v1_ | langfuse |
| Langfuse Llm Connections  Specialist | Expert specialist for llm_connections_ domain tasks. | You are a Langfuse Llm Connections  specialist. Help users manage and interact with Llm Connections  functionality using the available tools. | langfuse_llm_connections__toolset | llm_connections_ | langfuse |
| Langfuse Media  Specialist | Expert specialist for media_ domain tasks. | You are a Langfuse Media  specialist. Help users manage and interact with Media  functionality using the available tools. | langfuse_media__toolset | media_ | langfuse |
| Langfuse Metrics  Specialist | Expert specialist for metrics_ domain tasks. | You are a Langfuse Metrics  specialist. Help users manage and interact with Metrics  functionality using the available tools. | langfuse_metrics__toolset | metrics_ | langfuse |
| Langfuse Models  Specialist | Expert specialist for models_ domain tasks. | You are a Langfuse Models  specialist. Help users manage and interact with Models  functionality using the available tools. | langfuse_models__toolset | models_ | langfuse |
| Langfuse Observations  Specialist | Expert specialist for observations_ domain tasks. | You are a Langfuse Observations  specialist. Help users manage and interact with Observations  functionality using the available tools. | langfuse_observations__toolset | observations_ | langfuse |
| Langfuse Opentelemetry  Specialist | Expert specialist for opentelemetry_ domain tasks. | You are a Langfuse Opentelemetry  specialist. Help users manage and interact with Opentelemetry  functionality using the available tools. | langfuse_opentelemetry__toolset | opentelemetry_ | langfuse |
| Langfuse Organizations  Specialist | Expert specialist for organizations_ domain tasks. | You are a Langfuse Organizations  specialist. Help users manage and interact with Organizations  functionality using the available tools. | langfuse_organizations__toolset | organizations_ | langfuse |
| Langfuse Projects  Specialist | Expert specialist for projects_ domain tasks. | You are a Langfuse Projects  specialist. Help users manage and interact with Projects  functionality using the available tools. | langfuse_projects__toolset | projects_ | langfuse |
| Langfuse Prompts  Specialist | Expert specialist for prompts_ domain tasks. | You are a Langfuse Prompts  specialist. Help users manage and interact with Prompts  functionality using the available tools. | langfuse_prompts__toolset | prompts_ | langfuse |
| Langfuse Prompt Version  Specialist | Expert specialist for prompt_version_ domain tasks. | You are a Langfuse Prompt Version  specialist. Help users manage and interact with Prompt Version  functionality using the available tools. | langfuse_prompt_version__toolset | prompt_version_ | langfuse |
| Langfuse Scim  Specialist | Expert specialist for scim_ domain tasks. | You are a Langfuse Scim  specialist. Help users manage and interact with Scim  functionality using the available tools. | langfuse_scim__toolset | scim_ | langfuse |
| Langfuse Scores  Specialist | Expert specialist for scores_ domain tasks. | You are a Langfuse Scores  specialist. Help users manage and interact with Scores  functionality using the available tools. | langfuse_scores__toolset | scores_ | langfuse |
| Langfuse Score Configs  Specialist | Expert specialist for score_configs_ domain tasks. | You are a Langfuse Score Configs  specialist. Help users manage and interact with Score Configs  functionality using the available tools. | langfuse_score_configs__toolset | score_configs_ | langfuse |
| Langfuse Sessions  Specialist | Expert specialist for sessions_ domain tasks. | You are a Langfuse Sessions  specialist. Help users manage and interact with Sessions  functionality using the available tools. | langfuse_sessions__toolset | sessions_ | langfuse |
| Langfuse Trace  Specialist | Expert specialist for trace_ domain tasks. | You are a Langfuse Trace  specialist. Help users manage and interact with Trace  functionality using the available tools. | langfuse_trace__toolset | trace_ | langfuse |
| Leanix Poll Specialist | Expert specialist for leanix_poll domain tasks. | You are a Leanix Poll specialist. Help users manage and interact with Leanix Poll functionality using the available tools. | leanix-agent_leanix_poll_toolset | leanix_poll | leanix-agent |
| Leanix Discovery Linking V2 Specialist | Expert specialist for leanix_discovery_linking_v2 domain tasks. | You are a Leanix Discovery Linking V2 specialist. Help users manage and interact with Leanix Discovery Linking V2 functionality using the available tools. | leanix-agent_leanix_discovery_linking_v2_toolset | leanix_discovery_linking_v2 | leanix-agent |
| Leanix Reference Data Catalog Specialist | Expert specialist for leanix_reference_data_catalog domain tasks. | You are a Leanix Reference Data Catalog specialist. Help users manage and interact with Leanix Reference Data Catalog functionality using the available tools. | leanix-agent_leanix_reference_data_catalog_toolset | leanix_reference_data_catalog | leanix-agent |
| Leanix Metrics Specialist | Expert specialist for leanix_metrics domain tasks. | You are a Leanix Metrics specialist. Help users manage and interact with Leanix Metrics functionality using the available tools. | leanix-agent_leanix_metrics_toolset | leanix_metrics | leanix-agent |
| Leanix Discovery Saas Specialist | Expert specialist for leanix_discovery_saas domain tasks. | You are a Leanix Discovery Saas specialist. Help users manage and interact with Leanix Discovery Saas functionality using the available tools. | leanix-agent_leanix_discovery_saas_toolset | leanix_discovery_saas | leanix-agent |
| Leanix Mtm Specialist | Expert specialist for leanix_mtm domain tasks. | You are a Leanix Mtm specialist. Help users manage and interact with Leanix Mtm functionality using the available tools. | leanix-agent_leanix_mtm_toolset | leanix_mtm | leanix-agent |
| Leanix Webhooks Specialist | Expert specialist for leanix_webhooks domain tasks. | You are a Leanix Webhooks specialist. Help users manage and interact with Leanix Webhooks functionality using the available tools. | leanix-agent_leanix_webhooks_toolset | leanix_webhooks | leanix-agent |
| Leanix Storage Specialist | Expert specialist for leanix_storage domain tasks. | You are a Leanix Storage specialist. Help users manage and interact with Leanix Storage functionality using the available tools. | leanix-agent_leanix_storage_toolset | leanix_storage | leanix-agent |
| Leanix Transformations Specialist | Expert specialist for leanix_transformations domain tasks. | You are a Leanix Transformations specialist. Help users manage and interact with Leanix Transformations functionality using the available tools. | leanix-agent_leanix_transformations_toolset | leanix_transformations | leanix-agent |
| Leanix Integration Collibra Specialist | Expert specialist for leanix_integration_collibra domain tasks. | You are a Leanix Integration Collibra specialist. Help users manage and interact with Leanix Integration Collibra functionality using the available tools. | leanix-agent_leanix_integration_collibra_toolset | leanix_integration_collibra | leanix-agent |
| Leanix Discovery Sap Extension Specialist | Expert specialist for leanix_discovery_sap_extension domain tasks. | You are a Leanix Discovery Sap Extension specialist. Help users manage and interact with Leanix Discovery Sap Extension functionality using the available tools. | leanix-agent_leanix_discovery_sap_extension_toolset | leanix_discovery_sap_extension | leanix-agent |
| Leanix Impacts Specialist | Expert specialist for leanix_impacts domain tasks. | You are a Leanix Impacts specialist. Help users manage and interact with Leanix Impacts functionality using the available tools. | leanix-agent_leanix_impacts_toolset | leanix_impacts | leanix-agent |
| Leanix Technology Discovery Specialist | Expert specialist for leanix_technology_discovery domain tasks. | You are a Leanix Technology Discovery specialist. Help users manage and interact with Leanix Technology Discovery functionality using the available tools. | leanix-agent_leanix_technology_discovery_toolset | leanix_technology_discovery | leanix-agent |
| Leanix Ai Inventory Builder Specialist | Expert specialist for leanix_ai_inventory_builder domain tasks. | You are a Leanix Ai Inventory Builder specialist. Help users manage and interact with Leanix Ai Inventory Builder functionality using the available tools. | leanix-agent_leanix_ai_inventory_builder_toolset | leanix_ai_inventory_builder | leanix-agent |
| Leanix Managed Code Execution Specialist | Expert specialist for leanix_managed_code_execution domain tasks. | You are a Leanix Managed Code Execution specialist. Help users manage and interact with Leanix Managed Code Execution functionality using the available tools. | leanix-agent_leanix_managed_code_execution_toolset | leanix_managed_code_execution | leanix-agent |
| Leanix Graphql Specialist | Expert specialist for graphql domain tasks. | You are a Leanix Graphql specialist. Help users manage and interact with Graphql functionality using the available tools. | leanix-agent_graphql_toolset | graphql | leanix-agent |
| Leanix Reference Data Specialist | Expert specialist for leanix_reference_data domain tasks. | You are a Leanix Reference Data specialist. Help users manage and interact with Leanix Reference Data functionality using the available tools. | leanix-agent_leanix_reference_data_toolset | leanix_reference_data | leanix-agent |
| Leanix Survey Specialist | Expert specialist for leanix_survey domain tasks. | You are a Leanix Survey specialist. Help users manage and interact with Leanix Survey functionality using the available tools. | leanix-agent_leanix_survey_toolset | leanix_survey | leanix-agent |
| Leanix Navigation Specialist | Expert specialist for leanix_navigation domain tasks. | You are a Leanix Navigation specialist. Help users manage and interact with Leanix Navigation functionality using the available tools. | leanix-agent_leanix_navigation_toolset | leanix_navigation | leanix-agent |
| Leanix Integration Signavio Specialist | Expert specialist for leanix_integration_signavio domain tasks. | You are a Leanix Integration Signavio specialist. Help users manage and interact with Leanix Integration Signavio functionality using the available tools. | leanix-agent_leanix_integration_signavio_toolset | leanix_integration_signavio | leanix-agent |
| Leanix Pathfinder Specialist | Expert specialist for leanix_pathfinder domain tasks. | You are a Leanix Pathfinder specialist. Help users manage and interact with Leanix Pathfinder functionality using the available tools. | leanix-agent_leanix_pathfinder_toolset | leanix_pathfinder | leanix-agent |
| Leanix Todo Specialist | Expert specialist for leanix_todo domain tasks. | You are a Leanix Todo specialist. Help users manage and interact with Leanix Todo functionality using the available tools. | leanix-agent_leanix_todo_toolset | leanix_todo | leanix-agent |
| Leanix Discovery Ai Agents Specialist | Expert specialist for leanix_discovery_ai_agents domain tasks. | You are a Leanix Discovery Ai Agents specialist. Help users manage and interact with Leanix Discovery Ai Agents functionality using the available tools. | leanix-agent_leanix_discovery_ai_agents_toolset | leanix_discovery_ai_agents | leanix-agent |
| Leanix Integration Servicenow Specialist | Expert specialist for leanix_integration_servicenow domain tasks. | You are a Leanix Integration Servicenow specialist. Help users manage and interact with Leanix Integration Servicenow functionality using the available tools. | leanix-agent_leanix_integration_servicenow_toolset | leanix_integration_servicenow | leanix-agent |
| Leanix Automations Specialist | Expert specialist for leanix_automations domain tasks. | You are a Leanix Automations specialist. Help users manage and interact with Leanix Automations functionality using the available tools. | leanix-agent_leanix_automations_toolset | leanix_automations | leanix-agent |
| Leanix Discovery Linking V1 Specialist | Expert specialist for leanix_discovery_linking_v1 domain tasks. | You are a Leanix Discovery Linking V1 specialist. Help users manage and interact with Leanix Discovery Linking V1 functionality using the available tools. | leanix-agent_leanix_discovery_linking_v1_toolset | leanix_discovery_linking_v1 | leanix-agent |
| Leanix Discovery Sap Specialist | Expert specialist for leanix_discovery_sap domain tasks. | You are a Leanix Discovery Sap specialist. Help users manage and interact with Leanix Discovery Sap functionality using the available tools. | leanix-agent_leanix_discovery_sap_toolset | leanix_discovery_sap | leanix-agent |
| Leanix Synclog Specialist | Expert specialist for leanix_synclog domain tasks. | You are a Leanix Synclog specialist. Help users manage and interact with Leanix Synclog functionality using the available tools. | leanix-agent_leanix_synclog_toolset | leanix_synclog | leanix-agent |
| Leanix Integration Api Specialist | Expert specialist for leanix_integration_api domain tasks. | You are a Leanix Integration Api specialist. Help users manage and interact with Leanix Integration Api functionality using the available tools. | leanix-agent_leanix_integration_api_toolset | leanix_integration_api | leanix-agent |
| Leanix Inventory Data Quality Specialist | Expert specialist for leanix_inventory_data_quality domain tasks. | You are a Leanix Inventory Data Quality specialist. Help users manage and interact with Leanix Inventory Data Quality functionality using the available tools. | leanix-agent_leanix_inventory_data_quality_toolset | leanix_inventory_data_quality | leanix-agent |
| Leanix Documents Specialist | Expert specialist for leanix_documents domain tasks. | You are a Leanix Documents specialist. Help users manage and interact with Leanix Documents functionality using the available tools. | leanix-agent_leanix_documents_toolset | leanix_documents | leanix-agent |
| Leanix Apptio Connector Specialist | Expert specialist for leanix_apptio_connector domain tasks. | You are a Leanix Apptio Connector specialist. Help users manage and interact with Leanix Apptio Connector functionality using the available tools. | leanix-agent_leanix_apptio_connector_toolset | leanix_apptio_connector | leanix-agent |
| Mealie App Specialist | Expert specialist for app domain tasks. | You are a Mealie App specialist. Help users manage and interact with App functionality using the available tools. | get_startup_info, get_app_theme | app | mealie-mcp |
| Mealie Households Specialist | Expert specialist for households domain tasks. | You are a Mealie Households specialist. Help users manage and interact with Households functionality using the available tools. | get_households_cookbooks, post_households_cookbooks, put_households_cookbooks, get_households_cookbooks_item_id, put_households_cookbooks_item_id, delete_households_cookbooks_item_id, get_households_events_notifications, post_households_events_notifications, get_households_events_notifications_item_id, put_households_events_notifications_item_id, delete_households_events_notifications_item_id, test_notification, get_households_recipe_actions, post_households_recipe_actions, get_households_recipe_actions_item_id, put_households_recipe_actions_item_id, delete_households_recipe_actions_item_id, trigger_action, get_logged_in_user_household, get_household_recipe, get_household_members, get_household_preferences, update_household_preferences, set_member_permissions, get_statistics, get_invite_tokens, create_invite_token, email_invitation, get_households_shopping_lists, post_households_shopping_lists, get_households_shopping_lists_item_id, put_households_shopping_lists_item_id, delete_households_shopping_lists_item_id, update_label_settings, add_recipe_ingredients_to_list, add_single_recipe_ingredients_to_list, remove_recipe_ingredients_from_list, get_households_shopping_items, post_households_shopping_items, put_households_shopping_items, delete_households_shopping_items, post_households_shopping_items_create_bulk, get_households_shopping_items_item_id, put_households_shopping_items_item_id, delete_households_shopping_items_item_id, get_households_webhooks, post_households_webhooks, rerun_webhooks, get_households_webhooks_item_id, put_households_webhooks_item_id, delete_households_webhooks_item_id, test_one, get_households_mealplans_rules, post_households_mealplans_rules, get_households_mealplans_rules_item_id, put_households_mealplans_rules_item_id, delete_households_mealplans_rules_item_id, get_households_mealplans, post_households_mealplans, get_todays_meals, create_random_meal, get_households_mealplans_item_id, put_households_mealplans_item_id, delete_households_mealplans_item_id | households | mealie-mcp |
| Mealie Recipes Specialist | Expert specialist for recipes domain tasks. | You are a Mealie Recipes specialist. Help users manage and interact with Recipes functionality using the available tools. | get_recipe_formats_and_templates, get_recipe_as_format, test_parse_recipe_url, create_recipe_from_html_or_json, parse_recipe_url, parse_recipe_url_bulk, create_recipe_from_zip, create_recipe_from_image, get_recipes, post_recipes, put_recipes, patch_many, get_recipes_suggestions, get_recipes_slug, put_recipes_slug, patch_one, delete_recipes_slug, duplicate_one, update_last_made, scrape_image_url, update_recipe_image, delete_recipe_image, upload_recipe_asset, get_recipe_comments, bulk_tag_recipes, bulk_settings_recipes, bulk_categorize_recipes, bulk_delete_recipes, bulk_export_recipes, get_exported_data, get_exported_data_token, purge_export_data, get_shared_recipe, get_shared_recipe_as_zip, get_recipes_timeline_events, post_recipes_timeline_events, get_recipes_timeline_events_item_id, put_recipes_timeline_events_item_id, delete_recipes_timeline_events_item_id, update_event_image, get_comments, post_comments, get_comments_item_id, put_comments_item_id, post_parser_ingredient, parse_ingredient, parse_ingredients, get_foods, post_foods, put_foods_merge, get_foods_item_id, put_foods_item_id, delete_foods_item_id, get_units, post_units, put_units_merge, get_units_item_id, put_units_item_id, delete_units_item_id, get_recipe_img, get_recipe_timeline_event_img, get_recipe_asset, get_user_image, get_validation_text | recipes | mealie-mcp |
| Mealie Organizer Specialist | Expert specialist for organizer domain tasks. | You are a Mealie Organizer specialist. Help users manage and interact with Organizer functionality using the available tools. | get_organizers_categories, post_organizers_categories, get_all_empty, get_organizers_categories_item_id, put_organizers_categories_item_id, delete_organizers_categories_item_id, get_organizers_categories_slug_category_slug, get_organizers_tags, post_organizers_tags, get_empty_tags, get_organizers_tags_item_id, put_organizers_tags_item_id, delete_recipe_tag, get_organizers_tags_slug_tag_slug, get_organizers_tools, post_organizers_tools, get_organizers_tools_item_id, put_organizers_tools_item_id, delete_organizers_tools_item_id, get_organizers_tools_slug_tool_slug | organizer | mealie-mcp |
| Mealie Shared Specialist | Expert specialist for shared domain tasks. | You are a Mealie Shared specialist. Help users manage and interact with Shared functionality using the available tools. | get_shared_recipes, post_shared_recipes, get_shared_recipes_item_id, delete_shared_recipes_item_id | shared | mealie-mcp |
| Mealie Admin Specialist | Expert specialist for admin domain tasks. | You are a Mealie Admin specialist. Help users manage and interact with Admin functionality using the available tools. | get_app_info, get_app_statistics, check_app_config, get_admin_users, post_admin_users, unlock_users, get_admin_users_item_id, put_admin_users_item_id, delete_admin_users_item_id, generate_token, get_admin_households, post_admin_households, get_admin_households_item_id, put_admin_households_item_id, delete_admin_households_item_id, get_admin_groups, post_admin_groups, get_admin_groups_item_id, put_admin_groups_item_id, delete_admin_groups_item_id, check_email_config, send_test_email, get_admin_backups, post_admin_backups, get_admin_backups_file_name, delete_admin_backups_file_name, upload_one, import_one, get_maintenance_summary, get_storage_details, clean_images, clean_temp, clean_recipe_folders, debug_openai, microsoft-agent_admin_toolset | admin | mealie-mcp |
| Mealie Explore Specialist | Expert specialist for explore domain tasks. | You are a Mealie Explore specialist. Help users manage and interact with Explore functionality using the available tools. | get_explore_groups_group_slug_foods, get_explore_groups_group_slug_foods_item_id, get_explore_groups_group_slug_households, get_household, get_explore_groups_group_slug_organizers_categories, get_explore_groups_group_slug_organizers_categories_item_id, get_explore_groups_group_slug_organizers_tags, get_explore_groups_group_slug_organizers_tags_item_id, get_explore_groups_group_slug_organizers_tools, get_explore_groups_group_slug_organizers_tools_item_id, get_explore_groups_group_slug_cookbooks, get_explore_groups_group_slug_cookbooks_item_id, get_explore_groups_group_slug_recipes, get_explore_groups_group_slug_recipes_suggestions, get_recipe | explore | mealie-mcp |
| Mealie Utils Specialist | Expert specialist for utils domain tasks. | You are a Mealie Utils specialist. Help users manage and interact with Utils functionality using the available tools. | download_file | utils | mealie-mcp |
| Media-Downloader Text Editor Specialist | Expert specialist for text_editor domain tasks. | You are a Media-Downloader Text Editor specialist. Help users manage and interact with Text Editor functionality using the available tools. | media-downloader-mcp_text_editor_toolset, systems-manager_text_editor_toolset | text_editor | media-downloader-mcp |
| Media-Downloader Collection Management Specialist | Expert specialist for collection_management domain tasks. | You are a Media-Downloader Collection Management specialist. Help users manage and interact with Collection Management functionality using the available tools. | media-downloader-mcp_collection_management_toolset, vector-mcp_collection_management_toolset | collection_management | media-downloader-mcp |
| Microsoft Auth Specialist | Expert specialist for auth domain tasks. | You are a Microsoft Auth specialist. Help users manage and interact with Auth functionality using the available tools. | microsoft-agent_auth_toolset, servicenow-api_auth_toolset | auth | microsoft-agent |
| Microsoft Agreements Specialist | Expert specialist for agreements domain tasks. | You are a Microsoft Agreements specialist. Help users manage and interact with Agreements functionality using the available tools. | microsoft-agent_agreements_toolset | agreements | microsoft-agent |
| Microsoft Files Specialist | Expert specialist for files domain tasks. | You are a Microsoft Files specialist. Help users manage and interact with Files functionality using the available tools. | microsoft-agent_files_toolset, nextcloud-agent_files_toolset | files | microsoft-agent |
| Microsoft Notes Specialist | Expert specialist for notes domain tasks. | You are a Microsoft Notes specialist. Help users manage and interact with Notes functionality using the available tools. | microsoft-agent_notes_toolset | notes | microsoft-agent |
| Microsoft Organization Specialist | Expert specialist for organization domain tasks. | You are a Microsoft Organization specialist. Help users manage and interact with Organization functionality using the available tools. | microsoft-agent_organization_toolset | organization | microsoft-agent |
| Microsoft Audit Specialist | Expert specialist for audit domain tasks. | You are a Microsoft Audit specialist. Help users manage and interact with Audit functionality using the available tools. | microsoft-agent_audit_toolset | audit | microsoft-agent |
| Microsoft Places Specialist | Expert specialist for places domain tasks. | You are a Microsoft Places specialist. Help users manage and interact with Places functionality using the available tools. | microsoft-agent_places_toolset | places | microsoft-agent |
| Microsoft Print Specialist | Expert specialist for print domain tasks. | You are a Microsoft Print specialist. Help users manage and interact with Print functionality using the available tools. | microsoft-agent_print_toolset | print | microsoft-agent |
| Microsoft Tasks Specialist | Expert specialist for tasks domain tasks. | You are a Microsoft Tasks specialist. Help users manage and interact with Tasks functionality using the available tools. | microsoft-agent_tasks_toolset | tasks | microsoft-agent |
| Microsoft Employee Experience Specialist | Expert specialist for employee_experience domain tasks. | You are a Microsoft Employee Experience specialist. Help users manage and interact with Employee Experience functionality using the available tools. | microsoft-agent_employee_experience_toolset | employee_experience | microsoft-agent |
| Microsoft Meta Specialist | Expert specialist for meta domain tasks. | You are a Microsoft Meta specialist. Help users manage and interact with Meta functionality using the available tools. | microsoft-agent_meta_toolset | meta | microsoft-agent |
| Microsoft Chat Specialist | Expert specialist for chat domain tasks. | You are a Microsoft Chat specialist. Help users manage and interact with Chat functionality using the available tools. | microsoft-agent_chat_toolset, owncast-chat-get-user-details | chat | microsoft-agent |
| Microsoft Sites Specialist | Expert specialist for sites domain tasks. | You are a Microsoft Sites specialist. Help users manage and interact with Sites functionality using the available tools. | microsoft-agent_sites_toolset | sites | microsoft-agent |
| Microsoft Directory Specialist | Expert specialist for directory domain tasks. | You are a Microsoft Directory specialist. Help users manage and interact with Directory functionality using the available tools. | microsoft-agent_directory_toolset | directory | microsoft-agent |
| Microsoft Policies Specialist | Expert specialist for policies domain tasks. | You are a Microsoft Policies specialist. Help users manage and interact with Policies functionality using the available tools. | microsoft-agent_policies_toolset | policies | microsoft-agent |
| Microsoft Teams Specialist | Expert specialist for teams domain tasks. | You are a Microsoft Teams specialist. Help users manage and interact with Teams functionality using the available tools. | microsoft-agent_teams_toolset | teams | microsoft-agent |
| Microsoft Applications Specialist | Expert specialist for applications domain tasks. | You are a Microsoft Applications specialist. Help users manage and interact with Applications functionality using the available tools. | microsoft-agent_applications_toolset | applications | microsoft-agent |
| Microsoft Calendar Specialist | Expert specialist for calendar domain tasks. | You are a Microsoft Calendar specialist. Help users manage and interact with Calendar functionality using the available tools. | microsoft-agent_calendar_toolset, nextcloud-agent_calendar_toolset | calendar | microsoft-agent |
| Microsoft Reports Specialist | Expert specialist for reports domain tasks. | You are a Microsoft Reports specialist. Help users manage and interact with Reports functionality using the available tools. | microsoft-agent_reports_toolset | reports | microsoft-agent |
| Microsoft Privacy Specialist | Expert specialist for privacy domain tasks. | You are a Microsoft Privacy specialist. Help users manage and interact with Privacy functionality using the available tools. | microsoft-agent_privacy_toolset | privacy | microsoft-agent |
| Microsoft Solutions Specialist | Expert specialist for solutions domain tasks. | You are a Microsoft Solutions specialist. Help users manage and interact with Solutions functionality using the available tools. | microsoft-agent_solutions_toolset | solutions | microsoft-agent |
| Microsoft Subscriptions Specialist | Expert specialist for subscriptions domain tasks. | You are a Microsoft Subscriptions specialist. Help users manage and interact with Subscriptions functionality using the available tools. | microsoft-agent_subscriptions_toolset | subscriptions | microsoft-agent |
| Microsoft Domains Specialist | Expert specialist for domains domain tasks. | You are a Microsoft Domains specialist. Help users manage and interact with Domains functionality using the available tools. | microsoft-agent_domains_toolset | domains | microsoft-agent |
| Microsoft Connections Specialist | Expert specialist for connections domain tasks. | You are a Microsoft Connections specialist. Help users manage and interact with Connections functionality using the available tools. | microsoft-agent_connections_toolset | connections | microsoft-agent |
| Microsoft Storage Specialist | Expert specialist for storage domain tasks. | You are a Microsoft Storage specialist. Help users manage and interact with Storage functionality using the available tools. | microsoft-agent_storage_toolset | storage | microsoft-agent |
| Microsoft Security Specialist | Expert specialist for security domain tasks. | You are a Microsoft Security specialist. Help users manage and interact with Security functionality using the available tools. | microsoft-agent_security_toolset | security | microsoft-agent |
| Microsoft Contacts Specialist | Expert specialist for contacts domain tasks. | You are a Microsoft Contacts specialist. Help users manage and interact with Contacts functionality using the available tools. | microsoft-agent_contacts_toolset, nextcloud-agent_contacts_toolset | contacts | microsoft-agent |
| Microsoft Education Specialist | Expert specialist for education domain tasks. | You are a Microsoft Education specialist. Help users manage and interact with Education functionality using the available tools. | microsoft-agent_education_toolset | education | microsoft-agent |
| Microsoft Identity Specialist | Expert specialist for identity domain tasks. | You are a Microsoft Identity specialist. Help users manage and interact with Identity functionality using the available tools. | microsoft-agent_identity_toolset | identity | microsoft-agent |
| Microsoft Communications Specialist | Expert specialist for communications domain tasks. | You are a Microsoft Communications specialist. Help users manage and interact with Communications functionality using the available tools. | microsoft-agent_communications_toolset | communications | microsoft-agent |
| Microsoft Mail Specialist | Expert specialist for mail domain tasks. | You are a Microsoft Mail specialist. Help users manage and interact with Mail functionality using the available tools. | microsoft-agent_mail_toolset | mail | microsoft-agent |
| Nextcloud Sharing Specialist | Expert specialist for sharing domain tasks. | You are a Nextcloud Sharing specialist. Help users manage and interact with Sharing functionality using the available tools. | nextcloud-agent_sharing_toolset | sharing | nextcloud-agent |
| Owncast External Specialist | Expert specialist for external domain tasks. | You are a Owncast External specialist. Help users manage and interact with External functionality using the available tools. | owncast-external-send-system-message, owncast-external-send-system-message-to-connected-client, owncast-external-send-user-message, owncast-external-send-integration-chat-message, owncast-external-send-chat-action, owncast-external-update-message-visibility, owncast-external-get-status, owncast-external-set-stream-title, owncast-external-get-chat-messages, owncast-external-get-connected-chat-clients, owncast-external-get-user-details | external | owncast |
| Owncast Internal Specialist | Expert specialist for internal domain tasks. | You are a Owncast Internal specialist. Help users manage and interact with Internal functionality using the available tools. | owncast-internal-get-status, owncast-internal-get-custom-emoji-list, owncast-internal-get-chat-messages, owncast-internal-register-anonymous-chat-user, owncast-internal-update-message-visibility, owncast-internal-update-user-enabled, owncast-internal-get-web-config, owncast-internal-get-ypresponse, owncast-internal-get-all-social-platforms, owncast-internal-get-video-stream-output-variants, owncast-internal-ping, owncast-internal-remote-follow, owncast-internal-get-followers, owncast-internal-report-playback-metrics, owncast-internal-register-for-live-notifications, owncast-internal-status-admin, owncast-internal-disconnect-inbound-connection, owncast-internal-get-server-config, owncast-internal-get-viewers-over-time, owncast-internal-get-active-viewers, owncast-internal-get-hardware-stats, owncast-internal-get-connected-chat-clients, owncast-internal-get-chat-messages-admin, owncast-internal-update-message-visibility-admin, owncast-internal-update-user-enabled-admin, owncast-internal-get-disabled-users, owncast-internal-ban-ipaddress, owncast-internal-unban-ipaddress, owncast-internal-get-ipaddress-bans, owncast-internal-update-user-moderator, owncast-internal-get-moderators, owncast-internal-get-logs, owncast-internal-get-warnings, owncast-internal-get-followers-admin, owncast-internal-get-pending-follow-requests, owncast-internal-get-blocked-and-rejected-followers, owncast-internal-approve-follower, owncast-internal-upload-custom-emoji, owncast-internal-delete-custom-emoji, owncast-internal-set-admin-password, owncast-internal-set-stream-keys, owncast-internal-set-extra-page-content, owncast-internal-set-stream-title, owncast-internal-set-server-welcome-message, owncast-internal-set-chat-disabled, owncast-internal-set-chat-join-messages-enabled, owncast-internal-set-enable-established-chat-user-mode, owncast-internal-set-forbidden-username-list, owncast-internal-set-suggested-username-list, owncast-internal-set-chat-spam-protection-enabled, owncast-internal-set-chat-slur-filter-enabled, owncast-internal-set-chat-require-authentication, owncast-internal-set-video-codec, owncast-internal-set-stream-latency-level, owncast-internal-set-stream-output-variants, owncast-internal-set-custom-color-variable-values, owncast-internal-set-logo, owncast-internal-set-favicon, owncast-internal-reset-favicon, owncast-internal-set-tags, owncast-internal-set-ffmpeg-path, owncast-internal-set-web-server-port, owncast-internal-set-web-server-ip, owncast-internal-set-rtmpserver-port, owncast-internal-set-socket-host-override, owncast-internal-set-video-serving-endpoint, owncast-internal-set-nsfw, owncast-internal-set-directory-enabled, owncast-internal-set-social-handles, owncast-internal-set-s3-configuration, owncast-internal-set-server-url, owncast-internal-set-external-actions, owncast-internal-set-custom-styles, owncast-internal-set-custom-javascript, owncast-internal-set-hide-viewer-count, owncast-internal-set-disable-search-indexing, owncast-internal-set-federation-enabled, owncast-internal-set-federation-activity-private, owncast-internal-set-federation-show-engagement, owncast-internal-set-federation-username, owncast-internal-set-federation-go-live-message, owncast-internal-set-federation-block-domains, owncast-internal-set-discord-notification-configuration, owncast-internal-set-browser-notification-configuration, owncast-internal-get-webhooks, owncast-internal-delete-webhook, owncast-internal-create-webhook, owncast-internal-get-external-apiusers, owncast-internal-delete-external-apiuser, owncast-internal-create-external-apiuser, owncast-internal-auto-update-options, owncast-internal-auto-update-start, owncast-internal-auto-update-force-quit, owncast-internal-reset-ypregistration, owncast-internal-get-video-playback-metrics, owncast-internal-get-prometheus-api, owncast-internal-post-prometheus-api, owncast-internal-put-prometheus-api, owncast-internal-delete-prometheus-api, owncast-internal-send-federated-message, owncast-internal-get-federated-actions, owncast-internal-start-indie-auth-flow, owncast-internal-handle-indie-auth-redirect, owncast-internal-handle-indie-auth-endpoint-get, owncast-internal-handle-indie-auth-endpoint-post, owncast-internal-register-fediverse-otprequest, owncast-internal-verify-fediverse-otprequest | internal | owncast |
| Owncast Objects Specialist | Expert specialist for objects domain tasks. | You are a Owncast Objects specialist. Help users manage and interact with Objects functionality using the available tools. | owncast-objects-set-server-name, owncast-objects-set-server-summary, owncast-objects-set-custom-offline-message | objects | owncast |
| Plane Work Items Specialist | Expert specialist for work_items domain tasks. | You are a Plane Work Items specialist. Help users manage and interact with Work Items functionality using the available tools. | list_work_items, create_work_item, update_work_item, delete_work_item, search_work_items, retrieve_work_item_by_identifier, retrieve_work_item, list_work_item_activities, list_work_item_comments, create_work_item_comment, list_work_item_links, create_work_item_link, list_work_item_relations, list_work_item_types, list_work_logs, create_work_log | work_items | plane |
| Plane Cycles Specialist | Expert specialist for cycles domain tasks. | You are a Plane Cycles specialist. Help users manage and interact with Cycles functionality using the available tools. | list_cycles, create_cycle, retrieve_cycle, update_cycle, delete_cycle, list_cycle_work_items, add_work_items_to_cycle | cycles | plane |
| Plane Epics Specialist | Expert specialist for epics domain tasks. | You are a Plane Epics specialist. Help users manage and interact with Epics functionality using the available tools. | list_epics, create_epic, retrieve_epic, update_epic, delete_epic | epics | plane |
| Plane Initiatives Specialist | Expert specialist for initiatives domain tasks. | You are a Plane Initiatives specialist. Help users manage and interact with Initiatives functionality using the available tools. | list_initiatives, create_initiative | initiatives | plane |
| Plane Intake Specialist | Expert specialist for intake domain tasks. | You are a Plane Intake specialist. Help users manage and interact with Intake functionality using the available tools. | list_intake_work_items, create_intake_work_item | intake | plane |
| Plane Labels Specialist | Expert specialist for labels domain tasks. | You are a Plane Labels specialist. Help users manage and interact with Labels functionality using the available tools. | list_labels, create_label | labels | plane |
| Plane Pages Specialist | Expert specialist for pages domain tasks. | You are a Plane Pages specialist. Help users manage and interact with Pages functionality using the available tools. | retrieve_project_page, create_project_page | pages | plane |
| Plane Milestones Specialist | Expert specialist for milestones domain tasks. | You are a Plane Milestones specialist. Help users manage and interact with Milestones functionality using the available tools. | list_milestones, create_milestone, retrieve_milestone, update_milestone, delete_milestone | milestones | plane |
| Plane Modules Specialist | Expert specialist for modules domain tasks. | You are a Plane Modules specialist. Help users manage and interact with Modules functionality using the available tools. | list_modules, create_module, retrieve_module, update_module, delete_module | modules | plane |
| Plane States Specialist | Expert specialist for states domain tasks. | You are a Plane States specialist. Help users manage and interact with States functionality using the available tools. | list_states, create_state | states | plane |
| Plane Workspaces Specialist | Expert specialist for workspaces domain tasks. | You are a Plane Workspaces specialist. Help users manage and interact with Workspaces functionality using the available tools. | get_workspace, get_workspace_members, get_workspace_features, update_workspace_features | workspaces | plane |
| Portainer Auth Specialist | Expert specialist for Auth domain tasks. | You are a Portainer Auth specialist. Help users manage and interact with Auth functionality using the available tools. | authenticate, logout, validate_oauth | Auth | portainer-agent |
| Portainer Environment Specialist | Expert specialist for Environment domain tasks. | You are a Portainer Environment specialist. Help users manage and interact with Environment functionality using the available tools. | get_endpoints, get_endpoint, create_endpoint, update_endpoint, delete_endpoint, snapshot_endpoint, snapshot_all_endpoints, get_endpoint_groups, create_endpoint_group, delete_endpoint_group | Environment | portainer-agent |
| Portainer Docker Specialist | Expert specialist for docker domain tasks. | You are a Portainer Docker specialist. Help users manage and interact with Docker functionality using the available tools. | get_docker_dashboard, get_container_gpus, docker_list_containers, docker_inspect_container, docker_get_container_logs, docker_get_container_stats, docker_start_container, docker_stop_container, docker_restart_container, docker_remove_container, docker_list_services, docker_inspect_service, docker_get_service_logs, docker_list_images, docker_inspect_image, docker_list_networks, docker_inspect_network, docker_list_volumes, docker_inspect_volume, docker_get_info, docker_get_version, docker_get_system_df, docker_create_container, docker_create_network, docker_create_volume, docker_create_exec, docker_start_exec, docker_inspect_exec, docker_get_stack_logs | Docker | portainer-agent |
| Portainer Stack Specialist | Expert specialist for stack domain tasks. | You are a Portainer Stack specialist. Help users manage and interact with Stack functionality using the available tools. | get_stacks, get_stack, get_stack_file, create_standalone_stack, create_standalone_stack_from_repo, update_stack, delete_stack, start_stack, stop_stack, redeploy_stack_git | Stack | portainer-agent |
| Portainer Kubernetes Specialist | Expert specialist for kubernetes domain tasks. | You are a Portainer Kubernetes specialist. Help users manage and interact with Kubernetes functionality using the available tools. | get_kubernetes_dashboard, get_kubernetes_namespaces, get_kubernetes_applications, get_kubernetes_services, get_kubernetes_ingresses, get_kubernetes_configmaps, get_kubernetes_secrets, get_kubernetes_volumes, get_kubernetes_events, get_kubernetes_nodes_limits, get_kubernetes_metrics_nodes, get_helm_releases, install_helm_chart, delete_helm_release | Kubernetes | portainer-agent |
| Portainer Edge Specialist | Expert specialist for edge domain tasks. | You are a Portainer Edge specialist. Help users manage and interact with Edge functionality using the available tools. | get_edge_groups, create_edge_group, delete_edge_group, get_edge_stacks, get_edge_stack, create_edge_stack, delete_edge_stack, get_edge_jobs, get_edge_job, create_edge_job, delete_edge_job | Edge | portainer-agent |
| Portainer Template Specialist | Expert specialist for template domain tasks. | You are a Portainer Template specialist. Help users manage and interact with Template functionality using the available tools. | get_templates, get_custom_templates, get_custom_template, create_custom_template, delete_custom_template, get_custom_template_file, get_helm_templates | Template | portainer-agent |
| Portainer User Specialist | Expert specialist for User domain tasks. | You are a Portainer User specialist. Help users manage and interact with User functionality using the available tools. | get_users, get_user, get_current_user, create_user, delete_user, get_teams, create_team, delete_team, get_roles, get_user_tokens, get_user_profile, get_user_statistics, get_user_trophies, get_languages, get_repetition_units, get_weight_unit_settings | User | portainer-agent |
| Portainer Registry Specialist | Expert specialist for registry domain tasks. | You are a Portainer Registry specialist. Help users manage and interact with Registry functionality using the available tools. | get_registries, get_registry, create_registry, delete_registry | Registry | portainer-agent |
| Portainer System Specialist | Expert specialist for System domain tasks. | You are a Portainer System specialist. Help users manage and interact with System functionality using the available tools. | get_status, get_system_info, get_system_version, get_settings, update_settings, get_tags, create_tag, delete_tag, get_motd, backup_portainer | System | portainer-agent |
| Postiz Analytics Specialist | Expert specialist for analytics domain tasks. | You are a Postiz Analytics specialist. Help users manage and interact with Analytics functionality using the available tools. | postiz_analytics_toolset | analytics | postiz |
| Postiz Integrations Specialist | Expert specialist for integrations domain tasks. | You are a Postiz Integrations specialist. Help users manage and interact with Integrations functionality using the available tools. | postiz_integrations_toolset | integrations | postiz |
| Postiz Notifications Specialist | Expert specialist for notifications domain tasks. | You are a Postiz Notifications specialist. Help users manage and interact with Notifications functionality using the available tools. | postiz_notifications_toolset | notifications | postiz |
| Postiz Posts Specialist | Expert specialist for posts domain tasks. | You are a Postiz Posts specialist. Help users manage and interact with Posts functionality using the available tools. | postiz_posts_toolset | posts | postiz |
| Postiz Uploads Specialist | Expert specialist for uploads domain tasks. | You are a Postiz Uploads specialist. Help users manage and interact with Uploads functionality using the available tools. | postiz_uploads_toolset | uploads | postiz |
| Postiz Video Specialist | Expert specialist for video domain tasks. | You are a Postiz Video specialist. Help users manage and interact with Video functionality using the available tools. | postiz_video_toolset | video | postiz |
| Qbittorrent Specialist | Expert specialist for qbittorrent domain tasks. | You are a Qbittorrent specialist. Help users manage and interact with Qbittorrent functionality using the available tools. | qbittorrent_general_tools | qbittorrent | qbittorrent |
| Repository-Manager File Operations Specialist | Expert specialist for file_operations domain tasks. | You are a Repository-Manager File Operations specialist. Help users manage and interact with File Operations functionality using the available tools. | repository-manager_file_operations_toolset | file_operations | repository-manager |
| Repository-Manager Git Operations Specialist | Expert specialist for git_operations domain tasks. | You are a Repository-Manager Git Operations specialist. Help users manage and interact with Git Operations functionality using the available tools. | repository-manager_git_operations_toolset | git_operations | repository-manager |
| Repository-Manager Graph Intelligence Specialist | Expert specialist for graph_intelligence domain tasks. | You are a Repository-Manager Graph Intelligence specialist. Help users manage and interact with Graph Intelligence functionality using the available tools. | repository-manager_graph_intelligence_toolset | graph_intelligence | repository-manager |
| Repository-Manager Visualization Specialist | Expert specialist for visualization domain tasks. | You are a Repository-Manager Visualization specialist. Help users manage and interact with Visualization functionality using the available tools. | repository-manager_visualization_toolset | visualization | repository-manager |
| Repository-Manager Workspace Management Specialist | Expert specialist for workspace_management domain tasks. | You are a Repository-Manager Workspace Management specialist. Help users manage and interact with Workspace Management functionality using the available tools. | repository-manager_workspace_management_toolset | workspace_management | repository-manager |
| Servicenow-Api Account Specialist | Expert specialist for account domain tasks. | You are a Servicenow-Api Account specialist. Help users manage and interact with Account functionality using the available tools. | servicenow-api_account_toolset | account | servicenow-api |
| Servicenow-Api Activity Subscriptions Specialist | Expert specialist for activity_subscriptions domain tasks. | You are a Servicenow-Api Activity Subscriptions specialist. Help users manage and interact with Activity Subscriptions functionality using the available tools. | servicenow-api_activity_subscriptions_toolset | activity_subscriptions | servicenow-api |
| Servicenow-Api Aggregate Specialist | Expert specialist for aggregate domain tasks. | You are a Servicenow-Api Aggregate specialist. Help users manage and interact with Aggregate functionality using the available tools. | servicenow-api_aggregate_toolset | aggregate | servicenow-api |
| Servicenow-Api Application Specialist | Expert specialist for application domain tasks. | You are a Servicenow-Api Application specialist. Help users manage and interact with Application functionality using the available tools. | servicenow-api_application_toolset | application | servicenow-api |
| Servicenow-Api Attachment Specialist | Expert specialist for attachment domain tasks. | You are a Servicenow-Api Attachment specialist. Help users manage and interact with Attachment functionality using the available tools. | servicenow-api_attachment_toolset | attachment | servicenow-api |
| Servicenow-Api Batch Specialist | Expert specialist for batch domain tasks. | You are a Servicenow-Api Batch specialist. Help users manage and interact with Batch functionality using the available tools. | servicenow-api_batch_toolset | batch | servicenow-api |
| Servicenow-Api Change Management Specialist | Expert specialist for change_management domain tasks. | You are a Servicenow-Api Change Management specialist. Help users manage and interact with Change Management functionality using the available tools. | servicenow-api_change_management_toolset | change_management | servicenow-api |
| Servicenow-Api Cicd Specialist | Expert specialist for cicd domain tasks. | You are a Servicenow-Api Cicd specialist. Help users manage and interact with Cicd functionality using the available tools. | servicenow-api_cicd_toolset | cicd | servicenow-api |
| Servicenow-Api Cilifecycle Specialist | Expert specialist for cilifecycle domain tasks. | You are a Servicenow-Api Cilifecycle specialist. Help users manage and interact with Cilifecycle functionality using the available tools. | servicenow-api_cilifecycle_toolset | cilifecycle | servicenow-api |
| Servicenow-Api Cmdb Specialist | Expert specialist for cmdb domain tasks. | You are a Servicenow-Api Cmdb specialist. Help users manage and interact with Cmdb functionality using the available tools. | servicenow-api_cmdb_toolset | cmdb | servicenow-api |
| Servicenow-Api Data Classification Specialist | Expert specialist for data_classification domain tasks. | You are a Servicenow-Api Data Classification specialist. Help users manage and interact with Data Classification functionality using the available tools. | servicenow-api_data_classification_toolset | data_classification | servicenow-api |
| Servicenow-Api Devops Specialist | Expert specialist for devops domain tasks. | You are a Servicenow-Api Devops specialist. Help users manage and interact with Devops functionality using the available tools. | servicenow-api_devops_toolset | devops | servicenow-api |
| Servicenow-Api Email Specialist | Expert specialist for email domain tasks. | You are a Servicenow-Api Email specialist. Help users manage and interact with Email functionality using the available tools. | servicenow-api_email_toolset | email | servicenow-api |
| Servicenow-Api Flows Specialist | Expert specialist for flows domain tasks. | You are a Servicenow-Api Flows specialist. Help users manage and interact with Flows functionality using the available tools. | servicenow-api_flows_toolset | flows | servicenow-api |
| Servicenow-Api Hr Specialist | Expert specialist for hr domain tasks. | You are a Servicenow-Api Hr specialist. Help users manage and interact with Hr functionality using the available tools. | servicenow-api_hr_toolset | hr | servicenow-api |
| Servicenow-Api Import Sets Specialist | Expert specialist for import_sets domain tasks. | You are a Servicenow-Api Import Sets specialist. Help users manage and interact with Import Sets functionality using the available tools. | servicenow-api_import_sets_toolset | import_sets | servicenow-api |
| Servicenow-Api Incidents Specialist | Expert specialist for incidents domain tasks. | You are a Servicenow-Api Incidents specialist. Help users manage and interact with Incidents functionality using the available tools. | servicenow-api_incidents_toolset | incidents | servicenow-api |
| Servicenow-Api Knowledge Management Specialist | Expert specialist for knowledge_management domain tasks. | You are a Servicenow-Api Knowledge Management specialist. Help users manage and interact with Knowledge Management functionality using the available tools. | servicenow-api_knowledge_management_toolset | knowledge_management | servicenow-api |
| Servicenow-Api Metricbase Specialist | Expert specialist for metricbase domain tasks. | You are a Servicenow-Api Metricbase specialist. Help users manage and interact with Metricbase functionality using the available tools. | servicenow-api_metricbase_toolset | metricbase | servicenow-api |
| Servicenow-Api Ppm Specialist | Expert specialist for ppm domain tasks. | You are a Servicenow-Api Ppm specialist. Help users manage and interact with Ppm functionality using the available tools. | servicenow-api_ppm_toolset | ppm | servicenow-api |
| Servicenow-Api Product Inventory Specialist | Expert specialist for product_inventory domain tasks. | You are a Servicenow-Api Product Inventory specialist. Help users manage and interact with Product Inventory functionality using the available tools. | servicenow-api_product_inventory_toolset | product_inventory | servicenow-api |
| Servicenow-Api Service Qualification Specialist | Expert specialist for service_qualification domain tasks. | You are a Servicenow-Api Service Qualification specialist. Help users manage and interact with Service Qualification functionality using the available tools. | servicenow-api_service_qualification_toolset | service_qualification | servicenow-api |
| Servicenow-Api Source Control Specialist | Expert specialist for source_control domain tasks. | You are a Servicenow-Api Source Control specialist. Help users manage and interact with Source Control functionality using the available tools. | servicenow-api_source_control_toolset | source_control | servicenow-api |
| Servicenow-Api Table Api Specialist | Expert specialist for table_api domain tasks. | You are a Servicenow-Api Table Api specialist. Help users manage and interact with Table Api functionality using the available tools. | servicenow-api_table_api_toolset | table_api | servicenow-api |
| Servicenow-Api Testing Specialist | Expert specialist for testing domain tasks. | You are a Servicenow-Api Testing specialist. Help users manage and interact with Testing functionality using the available tools. | servicenow-api_testing_toolset | testing | servicenow-api |
| Servicenow-Api Update Sets Specialist | Expert specialist for update_sets domain tasks. | You are a Servicenow-Api Update Sets specialist. Help users manage and interact with Update Sets functionality using the available tools. | servicenow-api_update_sets_toolset | update_sets | servicenow-api |
| Stirlingpdf Pdf Specialist | Expert specialist for pdf domain tasks. | You are a Stirlingpdf Pdf specialist. Help users manage and interact with Pdf functionality using the available tools. | add_watermark | PDF | stirlingpdf-agent |
| Systems-Manager Filesystem Specialist | Expert specialist for filesystem domain tasks. | You are a Systems-Manager Filesystem specialist. Help users manage and interact with Filesystem functionality using the available tools. | systems-manager_filesystem_toolset | filesystem | systems-manager |
| Systems-Manager Process Specialist | Expert specialist for process domain tasks. | You are a Systems-Manager Process specialist. Help users manage and interact with Process functionality using the available tools. | systems-manager_process_toolset | process | systems-manager |
| Systems-Manager Ssh Management Specialist | Expert specialist for ssh_management domain tasks. | You are a Systems-Manager Ssh Management specialist. Help users manage and interact with Ssh Management functionality using the available tools. | systems-manager_ssh_management_toolset | ssh_management | systems-manager |
| Systems-Manager Shell Specialist | Expert specialist for shell domain tasks. | You are a Systems-Manager Shell specialist. Help users manage and interact with Shell functionality using the available tools. | systems-manager_shell_toolset | shell | systems-manager |
| Systems-Manager Cron Specialist | Expert specialist for cron domain tasks. | You are a Systems-Manager Cron specialist. Help users manage and interact with Cron functionality using the available tools. | systems-manager_cron_toolset | cron | systems-manager |
| Systems-Manager Nodejs Specialist | Expert specialist for nodejs domain tasks. | You are a Systems-Manager Nodejs specialist. Help users manage and interact with Nodejs functionality using the available tools. | systems-manager_nodejs_toolset | nodejs | systems-manager |
| Systems-Manager Service Specialist | Expert specialist for service domain tasks. | You are a Systems-Manager Service specialist. Help users manage and interact with Service functionality using the available tools. | systems-manager_service_toolset | service | systems-manager |
| Systems-Manager System Management Specialist | Expert specialist for system_management domain tasks. | You are a Systems-Manager System Management specialist. Help users manage and interact with System Management functionality using the available tools. | systems-manager_system_management_toolset | system_management | systems-manager |
| Systems-Manager Firewall Management Specialist | Expert specialist for firewall_management domain tasks. | You are a Systems-Manager Firewall Management specialist. Help users manage and interact with Firewall Management functionality using the available tools. | systems-manager_firewall_management_toolset | firewall_management | systems-manager |
| Systems-Manager Python Specialist | Expert specialist for python domain tasks. | You are a Systems-Manager Python specialist. Help users manage and interact with Python functionality using the available tools. | systems-manager_python_toolset | python | systems-manager |
| Systems-Manager Disk Specialist | Expert specialist for disk domain tasks. | You are a Systems-Manager Disk specialist. Help users manage and interact with Disk functionality using the available tools. | systems-manager_disk_toolset | disk | systems-manager |
| Tunnel-Manager Host Management Specialist | Expert specialist for host_management domain tasks. | You are a Tunnel-Manager Host Management specialist. Help users manage and interact with Host Management functionality using the available tools. | list_hosts, add_host, remove_host | host_management | tunnel-manager-mcp |
| Tunnel-Manager Remote Access Specialist | Expert specialist for remote_access domain tasks. | You are a Tunnel-Manager Remote Access specialist. Help users manage and interact with Remote Access functionality using the available tools. | run_command_on_remote_host, send_file_to_remote_host, receive_file_from_remote_host, check_ssh_server, test_key_auth, setup_passwordless_ssh, copy_ssh_config, rotate_ssh_key, remove_host_key, configure_key_auth_on_inventory, run_command_on_inventory, copy_ssh_config_on_inventory, rotate_ssh_key_on_inventory, send_file_to_inventory, receive_file_from_inventory | remote_access | tunnel-manager-mcp |
| Uptime Specialist | Expert specialist for uptime domain tasks. | You are a Uptime specialist. Help users manage and interact with Uptime functionality using the available tools. | uptime-kuma-get-monitors, uptime-kuma-get-monitor, uptime-kuma-add-monitor, uptime-kuma-edit-monitor, uptime-kuma-delete-monitor, uptime-kuma-pause-monitor, uptime-kuma-resume-monitor, uptime-kuma-get-status, uptime-kuma-get-uptime | uptime | uptime |
| Wger Routine Specialist | Expert specialist for Routine domain tasks. | You are a Wger Routine specialist. Help users manage and interact with Routine functionality using the available tools. | get_routines, get_routine, create_routine, delete_routine, get_days, create_day, delete_day, get_slots, create_slot, create_slot_entry, get_templates, get_public_templates | Routine | wger-agent |
| Wger Routineconfig Specialist | Expert specialist for RoutineConfig domain tasks. | You are a Wger Routineconfig specialist. Help users manage and interact with Routineconfig functionality using the available tools. | create_weight_config, get_weight_configs, create_repetitions_config, get_repetitions_configs, create_sets_config, create_rest_config, create_rir_config | RoutineConfig | wger-agent |
| Wger Exercise Specialist | Expert specialist for Exercise domain tasks. | You are a Wger Exercise specialist. Help users manage and interact with Exercise functionality using the available tools. | get_exercises, get_exercise_info, search_exercises, get_exercise_categories, get_equipment, get_muscles, get_exercise_images, get_variations | Exercise | wger-agent |
| Wger Workout Specialist | Expert specialist for Workout domain tasks. | You are a Wger Workout specialist. Help users manage and interact with Workout functionality using the available tools. | get_workout_sessions, get_workout_session, create_workout_session, delete_workout_session, get_workout_logs, create_workout_log, delete_workout_log | Workout | wger-agent |
| Wger Nutrition Specialist | Expert specialist for Nutrition domain tasks. | You are a Wger Nutrition specialist. Help users manage and interact with Nutrition functionality using the available tools. | get_nutrition_plans, get_nutrition_plan_info, create_nutrition_plan, delete_nutrition_plan, create_meal, create_meal_item, get_ingredients, get_ingredient_info, get_nutrition_diary, log_nutrition | Nutrition | wger-agent |
| Wger Body Specialist | Expert specialist for Body domain tasks. | You are a Wger Body specialist. Help users manage and interact with Body functionality using the available tools. | get_weight_entries, log_body_weight, delete_weight_entry, get_measurements, log_measurement, get_measurement_categories, create_measurement_category, get_gallery | Body | wger-agent |

## Tool Inventory Table

| Tool Name | Description | Tag | Source |
|-----------|-------------|-----|--------|
| adguard-home-agent_dhcp_toolset | Static hint toolset for dhcp based on config env. | dhcp | adguard-home-agent |
| adguard-home-agent_blocked_services_toolset | Static hint toolset for blocked_services based on config env. | blocked_services | adguard-home-agent |
| adguard-home-agent_access_toolset | Static hint toolset for access based on config env. | access | adguard-home-agent |
| adguard-home-agent_system_toolset | Static hint toolset for system based on config env. | system | adguard-home-agent |
| adguard-home-agent_settings_toolset | Static hint toolset for settings based on config env. | settings | adguard-home-agent |
| adguard-home-agent_rewrites_toolset | Static hint toolset for rewrites based on config env. | rewrites | adguard-home-agent |
| adguard-home-agent_filtering_toolset | Static hint toolset for filtering based on config env. | filtering | adguard-home-agent |
| adguard-home-agent_tls_toolset | Static hint toolset for tls based on config env. | tls | adguard-home-agent |
| adguard-home-agent_mobile_toolset | Static hint toolset for mobile based on config env. | mobile | adguard-home-agent |
| adguard-home-agent_stats_toolset | Static hint toolset for stats based on config env. | stats | adguard-home-agent |
| adguard-home-agent_clients_toolset | Static hint toolset for clients based on config env. | clients | adguard-home-agent |
| adguard-home-agent_dns_toolset | Static hint toolset for dns based on config env. | dns | adguard-home-agent |
| adguard-home-agent_profile_toolset | Static hint toolset for profile based on config env. | profile | adguard-home-agent |
| adguard-home-agent_query_log_toolset | Static hint toolset for query_log based on config env. | query_log | adguard-home-agent |
| adguard-home-agent_misc_toolset | Static hint toolset for misc based on config env. | misc | adguard-home-agent |
| ansible-tower-mcp_general_tools | General tools for ansible-tower-mcp (offline extraction). | ansible-tower | ansible-tower-mcp |
| archivebox-mcp_authentication_toolset | Static hint toolset for authentication based on config env. | authentication | archivebox-mcp |
| archivebox-mcp_cli_toolset | Static hint toolset for cli based on config env. | cli | archivebox-mcp |
| archivebox-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | archivebox-mcp |
| archivebox-mcp_core_toolset | Static hint toolset for core based on config env. | core | archivebox-mcp |
| arr-mcp_sonarr_downloads_toolset | Static hint toolset for sonarr_downloads based on config env. | sonarr_downloads | arr-mcp |
| arr-mcp_prowlarr_system_toolset | Static hint toolset for prowlarr_system based on config env. | prowlarr_system | arr-mcp |
| arr-mcp_prowlarr_history_toolset | Static hint toolset for prowlarr_history based on config env. | prowlarr_history | arr-mcp |
| arr-mcp_chaptarr_queue_toolset | Static hint toolset for chaptarr_queue based on config env. | chaptarr_queue | arr-mcp |
| arr-mcp_prowlarr_search_toolset | Static hint toolset for prowlarr_search based on config env. | prowlarr_search | arr-mcp |
| arr-mcp_lidarr_config_toolset | Static hint toolset for lidarr_config based on config env. | lidarr_config | arr-mcp |
| arr-mcp_sonarr_system_toolset | Static hint toolset for sonarr_system based on config env. | sonarr_system | arr-mcp |
| arr-mcp_sonarr_profiles_toolset | Static hint toolset for sonarr_profiles based on config env. | sonarr_profiles | arr-mcp |
| arr-mcp_lidarr_history_toolset | Static hint toolset for lidarr_history based on config env. | lidarr_history | arr-mcp |
| arr-mcp_lidarr_catalog_toolset | Static hint toolset for lidarr_catalog based on config env. | lidarr_catalog | arr-mcp |
| arr-mcp_bazarr_catalog_toolset | Static hint toolset for bazarr_catalog based on config env. | bazarr_catalog | arr-mcp |
| arr-mcp_bazarr_history_toolset | Static hint toolset for bazarr_history based on config env. | bazarr_history | arr-mcp |
| arr-mcp_sonarr_history_toolset | Static hint toolset for sonarr_history based on config env. | sonarr_history | arr-mcp |
| arr-mcp_sonarr_queue_toolset | Static hint toolset for sonarr_queue based on config env. | sonarr_queue | arr-mcp |
| arr-mcp_radarr_downloads_toolset | Static hint toolset for radarr_downloads based on config env. | radarr_downloads | arr-mcp |
| arr-mcp_chaptarr_downloads_toolset | Static hint toolset for chaptarr_downloads based on config env. | chaptarr_downloads | arr-mcp |
| arr-mcp_chaptarr_history_toolset | Static hint toolset for chaptarr_history based on config env. | chaptarr_history | arr-mcp |
| arr-mcp_lidarr_downloads_toolset | Static hint toolset for lidarr_downloads based on config env. | lidarr_downloads | arr-mcp |
| arr-mcp_lidarr_profiles_toolset | Static hint toolset for lidarr_profiles based on config env. | lidarr_profiles | arr-mcp |
| arr-mcp_chaptarr_config_toolset | Static hint toolset for chaptarr_config based on config env. | chaptarr_config | arr-mcp |
| arr-mcp_radarr_indexer_toolset | Static hint toolset for radarr_indexer based on config env. | radarr_indexer | arr-mcp |
| arr-mcp_chaptarr_indexer_toolset | Static hint toolset for chaptarr_indexer based on config env. | chaptarr_indexer | arr-mcp |
| arr-mcp_radarr_catalog_toolset | Static hint toolset for radarr_catalog based on config env. | radarr_catalog | arr-mcp |
| arr-mcp_radarr_profiles_toolset | Static hint toolset for radarr_profiles based on config env. | radarr_profiles | arr-mcp |
| arr-mcp_bazarr_system_toolset | Static hint toolset for bazarr_system based on config env. | bazarr_system | arr-mcp |
| arr-mcp_chaptarr_profiles_toolset | Static hint toolset for chaptarr_profiles based on config env. | chaptarr_profiles | arr-mcp |
| arr-mcp_lidarr_indexer_toolset | Static hint toolset for lidarr_indexer based on config env. | lidarr_indexer | arr-mcp |
| arr-mcp_seerr_system_toolset | Static hint toolset for seerr_system based on config env. | seerr_system | arr-mcp |
| arr-mcp_chaptarr_search_toolset | Static hint toolset for chaptarr_search based on config env. | chaptarr_search | arr-mcp |
| arr-mcp_radarr_history_toolset | Static hint toolset for radarr_history based on config env. | radarr_history | arr-mcp |
| arr-mcp_prowlarr_config_toolset | Static hint toolset for prowlarr_config based on config env. | prowlarr_config | arr-mcp |
| arr-mcp_sonarr_config_toolset | Static hint toolset for sonarr_config based on config env. | sonarr_config | arr-mcp |
| arr-mcp_chaptarr_operations_toolset | Static hint toolset for chaptarr_operations based on config env. | chaptarr_operations | arr-mcp |
| arr-mcp_seerr_catalog_toolset | Static hint toolset for seerr_catalog based on config env. | seerr_catalog | arr-mcp |
| arr-mcp_prowlarr_indexer_toolset | Static hint toolset for prowlarr_indexer based on config env. | prowlarr_indexer | arr-mcp |
| arr-mcp_prowlarr_operations_toolset | Static hint toolset for prowlarr_operations based on config env. | prowlarr_operations | arr-mcp |
| arr-mcp_prowlarr_downloads_toolset | Static hint toolset for prowlarr_downloads based on config env. | prowlarr_downloads | arr-mcp |
| arr-mcp_radarr_config_toolset | Static hint toolset for radarr_config based on config env. | radarr_config | arr-mcp |
| arr-mcp_prowlarr_profiles_toolset | Static hint toolset for prowlarr_profiles based on config env. | prowlarr_profiles | arr-mcp |
| arr-mcp_sonarr_catalog_toolset | Static hint toolset for sonarr_catalog based on config env. | sonarr_catalog | arr-mcp |
| arr-mcp_sonarr_indexer_toolset | Static hint toolset for sonarr_indexer based on config env. | sonarr_indexer | arr-mcp |
| arr-mcp_sonarr_operations_toolset | Static hint toolset for sonarr_operations based on config env. | sonarr_operations | arr-mcp |
| arr-mcp_lidarr_system_toolset | Static hint toolset for lidarr_system based on config env. | lidarr_system | arr-mcp |
| arr-mcp_radarr_system_toolset | Static hint toolset for radarr_system based on config env. | radarr_system | arr-mcp |
| arr-mcp_radarr_queue_toolset | Static hint toolset for radarr_queue based on config env. | radarr_queue | arr-mcp |
| arr-mcp_lidarr_queue_toolset | Static hint toolset for lidarr_queue based on config env. | lidarr_queue | arr-mcp |
| arr-mcp_seerr_search_toolset | Static hint toolset for seerr_search based on config env. | seerr_search | arr-mcp |
| arr-mcp_chaptarr_system_toolset | Static hint toolset for chaptarr_system based on config env. | chaptarr_system | arr-mcp |
| arr-mcp_radarr_operations_toolset | Static hint toolset for radarr_operations based on config env. | radarr_operations | arr-mcp |
| arr-mcp_lidarr_operations_toolset | Static hint toolset for lidarr_operations based on config env. | lidarr_operations | arr-mcp |
| arr-mcp_lidarr_search_toolset | Static hint toolset for lidarr_search based on config env. | lidarr_search | arr-mcp |
| atlassian_general_tools | General tools for atlassian (offline extraction). | atlassian | atlassian |
| audio-transcriber-mcp_audio_processing_toolset | Static hint toolset for audio_processing based on config env. | audio_processing | audio-transcriber-mcp |
| audio-transcriber-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | audio-transcriber-mcp |
| container-manager-mcp_log_toolset | Static hint toolset for log based on config env. | log | container-manager-mcp |
| container-manager-mcp_system_toolset | Static hint toolset for system based on config env. | system | container-manager-mcp |
| container-manager-mcp_info_toolset | Static hint toolset for info based on config env. | info | container-manager-mcp |
| container-manager-mcp_image_toolset | Static hint toolset for image based on config env. | image | container-manager-mcp |
| container-manager-mcp_network_toolset | Static hint toolset for network based on config env. | network | container-manager-mcp |
| container-manager-mcp_swarm_toolset | Static hint toolset for swarm based on config env. | swarm | container-manager-mcp |
| container-manager-mcp_container_toolset | Static hint toolset for container based on config env. | container | container-manager-mcp |
| container-manager-mcp_compose_toolset | Static hint toolset for compose based on config env. | compose | container-manager-mcp |
| container-manager-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | container-manager-mcp |
| container-manager-mcp_volume_toolset | Static hint toolset for volume based on config env. | volume | container-manager-mcp |
| documentdb-mcp_analysis_toolset | Static hint toolset for analysis based on config env. | analysis | documentdb-mcp |
| documentdb-mcp_users_toolset | Static hint toolset for users based on config env. | users | documentdb-mcp |
| documentdb-mcp_system_toolset | Static hint toolset for system based on config env. | system | documentdb-mcp |
| documentdb-mcp_collections_toolset | Static hint toolset for collections based on config env. | collections | documentdb-mcp |
| documentdb-mcp_crud_toolset | Static hint toolset for crud based on config env. | crud | documentdb-mcp |
| documentdb-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | documentdb-mcp |
| github_list_repos | List repositories for the authenticated user. | repos | github-mcp |
| github_get_repo | Get details for a specific repository. | repos | github-mcp |
| github_list_issues | List issues for a repository. | issues | github-mcp |
| github_list_pull_requests | List pull requests for a repository. | pulls | github-mcp |
| github_get_contents | Get contents of a file or directory. | contents | github-mcp |
| gitlab-api_groups_toolset | Static hint toolset for groups based on config env. | groups | gitlab-api |
| gitlab-api_protected_branches_toolset | Static hint toolset for protected_branches based on config env. | protected_branches | gitlab-api |
| gitlab-api_pipelines_toolset | Static hint toolset for pipelines based on config env. | pipelines | gitlab-api |
| gitlab-api_merge_requests_toolset | Static hint toolset for merge_requests based on config env. | merge_requests | gitlab-api |
| gitlab-api_misc_toolset | Static hint toolset for misc based on config env. | misc | gitlab-api |
| gitlab-api_packages_toolset | Static hint toolset for packages based on config env. | packages | gitlab-api |
| gitlab-api_deploy_tokens_toolset | Static hint toolset for deploy_tokens based on config env. | deploy_tokens | gitlab-api |
| gitlab-api_custom_api_toolset | Static hint toolset for custom_api based on config env. | custom_api | gitlab-api |
| gitlab-api_pipeline_schedules_toolset | Static hint toolset for pipeline_schedules based on config env. | pipeline_schedules | gitlab-api |
| gitlab-api_merge_rules_toolset | Static hint toolset for merge_rules based on config env. | merge_rules | gitlab-api |
| gitlab-api_commits_toolset | Static hint toolset for commits based on config env. | commits | gitlab-api |
| gitlab-api_branches_toolset | Static hint toolset for branches based on config env. | branches | gitlab-api |
| gitlab-api_jobs_toolset | Static hint toolset for jobs based on config env. | jobs | gitlab-api |
| gitlab-api_tags_toolset | Static hint toolset for tags based on config env. | tags | gitlab-api |
| gitlab-api_members_toolset | Static hint toolset for members based on config env. | members | gitlab-api |
| gitlab-api_environments_toolset | Static hint toolset for environments based on config env. | environments | gitlab-api |
| gitlab-api_projects_toolset | Static hint toolset for projects based on config env. | projects | gitlab-api |
| gitlab-api_releases_toolset | Static hint toolset for releases based on config env. | releases | gitlab-api |
| gitlab-api_runners_toolset | Static hint toolset for runners based on config env. | runners | gitlab-api |
| home_general_tools | General tools for home (offline extraction). | home | home |
| jellyfin-mcp_itemrefresh_toolset | Static hint toolset for itemrefresh based on config env. | itemrefresh | jellyfin-mcp |
| jellyfin-mcp_collection_toolset | Static hint toolset for collection based on config env. | collection | jellyfin-mcp |
| jellyfin-mcp_tvshows_toolset | Static hint toolset for tvshows based on config env. | tvshows | jellyfin-mcp |
| jellyfin-mcp_scheduledtasks_toolset | Static hint toolset for scheduledtasks based on config env. | scheduledtasks | jellyfin-mcp |
| jellyfin-mcp_tmdb_toolset | Static hint toolset for tmdb based on config env. | tmdb | jellyfin-mcp |
| jellyfin-mcp_dashboard_toolset | Static hint toolset for dashboard based on config env. | dashboard | jellyfin-mcp |
| jellyfin-mcp_clientlog_toolset | Static hint toolset for clientlog based on config env. | clientlog | jellyfin-mcp |
| jellyfin-mcp_search_toolset | Static hint toolset for search based on config env. | search | jellyfin-mcp |
| jellyfin-mcp_backup_toolset | Static hint toolset for backup based on config env. | backup | jellyfin-mcp |
| jellyfin-mcp_mediasegments_toolset | Static hint toolset for mediasegments based on config env. | mediasegments | jellyfin-mcp |
| jellyfin-mcp_hlssegment_toolset | Static hint toolset for hlssegment based on config env. | hlssegment | jellyfin-mcp |
| jellyfin-mcp_displaypreferences_toolset | Static hint toolset for displaypreferences based on config env. | displaypreferences | jellyfin-mcp |
| jellyfin-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | jellyfin-mcp |
| jellyfin-mcp_livetv_toolset | Static hint toolset for livetv based on config env. | livetv | jellyfin-mcp |
| jellyfin-mcp_videoattachments_toolset | Static hint toolset for videoattachments based on config env. | videoattachments | jellyfin-mcp |
| jellyfin-mcp_channels_toolset | Static hint toolset for channels based on config env. | channels | jellyfin-mcp |
| jellyfin-mcp_dynamichls_toolset | Static hint toolset for dynamichls based on config env. | dynamichls | jellyfin-mcp |
| jellyfin-mcp_library_toolset | Static hint toolset for library based on config env. | library | jellyfin-mcp |
| jellyfin-mcp_audio_toolset | Static hint toolset for audio based on config env. | audio | jellyfin-mcp |
| jellyfin-mcp_plugins_toolset | Static hint toolset for plugins based on config env. | plugins | jellyfin-mcp |
| jellyfin-mcp_session_toolset | Static hint toolset for session based on config env. | session | jellyfin-mcp |
| jellyfin-mcp_image_toolset | Static hint toolset for image based on config env. | image | jellyfin-mcp |
| jellyfin-mcp_studios_toolset | Static hint toolset for studios based on config env. | studios | jellyfin-mcp |
| jellyfin-mcp_environment_toolset | Static hint toolset for environment based on config env. | environment | jellyfin-mcp |
| jellyfin-mcp_persons_toolset | Static hint toolset for persons based on config env. | persons | jellyfin-mcp |
| jellyfin-mcp_trickplay_toolset | Static hint toolset for trickplay based on config env. | trickplay | jellyfin-mcp |
| jellyfin-mcp_instantmix_toolset | Static hint toolset for instantmix based on config env. | instantmix | jellyfin-mcp |
| jellyfin-mcp_movies_toolset | Static hint toolset for movies based on config env. | movies | jellyfin-mcp |
| jellyfin-mcp_syncplay_toolset | Static hint toolset for syncplay based on config env. | syncplay | jellyfin-mcp |
| jellyfin-mcp_startup_toolset | Static hint toolset for startup based on config env. | startup | jellyfin-mcp |
| jellyfin-mcp_universalaudio_toolset | Static hint toolset for universalaudio based on config env. | universalaudio | jellyfin-mcp |
| jellyfin-mcp_user_toolset | Static hint toolset for user based on config env. | user | jellyfin-mcp |
| jellyfin-mcp_musicgenres_toolset | Static hint toolset for musicgenres based on config env. | musicgenres | jellyfin-mcp |
| jellyfin-mcp_suggestions_toolset | Static hint toolset for suggestions based on config env. | suggestions | jellyfin-mcp |
| jellyfin-mcp_timesync_toolset | Static hint toolset for timesync based on config env. | timesync | jellyfin-mcp |
| jellyfin-mcp_artists_toolset | Static hint toolset for artists based on config env. | artists | jellyfin-mcp |
| jellyfin-mcp_system_toolset | Static hint toolset for system based on config env. | system | jellyfin-mcp |
| jellyfin-mcp_localization_toolset | Static hint toolset for localization based on config env. | localization | jellyfin-mcp |
| jellyfin-mcp_itemupdate_toolset | Static hint toolset for itemupdate based on config env. | itemupdate | jellyfin-mcp |
| jellyfin-mcp_librarystructure_toolset | Static hint toolset for librarystructure based on config env. | librarystructure | jellyfin-mcp |
| jellyfin-mcp_mediainfo_toolset | Static hint toolset for mediainfo based on config env. | mediainfo | jellyfin-mcp |
| jellyfin-mcp_quickconnect_toolset | Static hint toolset for quickconnect based on config env. | quickconnect | jellyfin-mcp |
| jellyfin-mcp_videos_toolset | Static hint toolset for videos based on config env. | videos | jellyfin-mcp |
| jellyfin-mcp_remoteimage_toolset | Static hint toolset for remoteimage based on config env. | remoteimage | jellyfin-mcp |
| jellyfin-mcp_playstate_toolset | Static hint toolset for playstate based on config env. | playstate | jellyfin-mcp |
| jellyfin-mcp_apikey_toolset | Static hint toolset for apikey based on config env. | apikey | jellyfin-mcp |
| jellyfin-mcp_devices_toolset | Static hint toolset for devices based on config env. | devices | jellyfin-mcp |
| jellyfin-mcp_filter_toolset | Static hint toolset for filter based on config env. | filter | jellyfin-mcp |
| jellyfin-mcp_branding_toolset | Static hint toolset for branding based on config env. | branding | jellyfin-mcp |
| jellyfin-mcp_genres_toolset | Static hint toolset for genres based on config env. | genres | jellyfin-mcp |
| jellyfin-mcp_userviews_toolset | Static hint toolset for userviews based on config env. | userviews | jellyfin-mcp |
| jellyfin-mcp_years_toolset | Static hint toolset for years based on config env. | years | jellyfin-mcp |
| jellyfin-mcp_lyrics_toolset | Static hint toolset for lyrics based on config env. | lyrics | jellyfin-mcp |
| jellyfin-mcp_trailers_toolset | Static hint toolset for trailers based on config env. | trailers | jellyfin-mcp |
| jellyfin-mcp_activitylog_toolset | Static hint toolset for activitylog based on config env. | activitylog | jellyfin-mcp |
| jellyfin-mcp_package_toolset | Static hint toolset for package based on config env. | package | jellyfin-mcp |
| jellyfin-mcp_subtitle_toolset | Static hint toolset for subtitle based on config env. | subtitle | jellyfin-mcp |
| jellyfin-mcp_playlists_toolset | Static hint toolset for playlists based on config env. | playlists | jellyfin-mcp |
| jellyfin-mcp_userlibrary_toolset | Static hint toolset for userlibrary based on config env. | userlibrary | jellyfin-mcp |
| jellyfin-mcp_configuration_toolset | Static hint toolset for configuration based on config env. | configuration | jellyfin-mcp |
| jellyfin-mcp_items_toolset | Static hint toolset for items based on config env. | items | jellyfin-mcp |
| jellyfin-mcp_itemlookup_toolset | Static hint toolset for itemlookup based on config env. | itemlookup | jellyfin-mcp |
| langfuse_annotation_queues__toolset | Static hint toolset for annotation_queues_ based on config env. | annotation_queues_ | langfuse |
| langfuse_blob_storage_integrations__toolset | Static hint toolset for blob_storage_integrations_ based on config env. | blob_storage_integrations_ | langfuse |
| langfuse_comments__toolset | Static hint toolset for comments_ based on config env. | comments_ | langfuse |
| langfuse_datasets__toolset | Static hint toolset for datasets_ based on config env. | datasets_ | langfuse |
| langfuse_dataset_items__toolset | Static hint toolset for dataset_items_ based on config env. | dataset_items_ | langfuse |
| langfuse_dataset_run_items__toolset | Static hint toolset for dataset_run_items_ based on config env. | dataset_run_items_ | langfuse |
| langfuse_health__toolset | Static hint toolset for health_ based on config env. | health_ | langfuse |
| langfuse_ingestion__toolset | Static hint toolset for ingestion_ based on config env. | ingestion_ | langfuse |
| langfuse_legacy_metrics_v1__toolset | Static hint toolset for legacy_metrics_v1_ based on config env. | legacy_metrics_v1_ | langfuse |
| langfuse_legacy_observations_v1__toolset | Static hint toolset for legacy_observations_v1_ based on config env. | legacy_observations_v1_ | langfuse |
| langfuse_legacy_score_v1__toolset | Static hint toolset for legacy_score_v1_ based on config env. | legacy_score_v1_ | langfuse |
| langfuse_llm_connections__toolset | Static hint toolset for llm_connections_ based on config env. | llm_connections_ | langfuse |
| langfuse_media__toolset | Static hint toolset for media_ based on config env. | media_ | langfuse |
| langfuse_metrics__toolset | Static hint toolset for metrics_ based on config env. | metrics_ | langfuse |
| langfuse_models__toolset | Static hint toolset for models_ based on config env. | models_ | langfuse |
| langfuse_observations__toolset | Static hint toolset for observations_ based on config env. | observations_ | langfuse |
| langfuse_opentelemetry__toolset | Static hint toolset for opentelemetry_ based on config env. | opentelemetry_ | langfuse |
| langfuse_organizations__toolset | Static hint toolset for organizations_ based on config env. | organizations_ | langfuse |
| langfuse_projects__toolset | Static hint toolset for projects_ based on config env. | projects_ | langfuse |
| langfuse_prompts__toolset | Static hint toolset for prompts_ based on config env. | prompts_ | langfuse |
| langfuse_prompt_version__toolset | Static hint toolset for prompt_version_ based on config env. | prompt_version_ | langfuse |
| langfuse_scim__toolset | Static hint toolset for scim_ based on config env. | scim_ | langfuse |
| langfuse_scores__toolset | Static hint toolset for scores_ based on config env. | scores_ | langfuse |
| langfuse_score_configs__toolset | Static hint toolset for score_configs_ based on config env. | score_configs_ | langfuse |
| langfuse_sessions__toolset | Static hint toolset for sessions_ based on config env. | sessions_ | langfuse |
| langfuse_trace__toolset | Static hint toolset for trace_ based on config env. | trace_ | langfuse |
| leanix-agent_leanix_poll_toolset | Static hint toolset for leanix_poll based on config env. | leanix_poll | leanix-agent |
| leanix-agent_leanix_discovery_linking_v2_toolset | Static hint toolset for leanix_discovery_linking_v2 based on config env. | leanix_discovery_linking_v2 | leanix-agent |
| leanix-agent_leanix_reference_data_catalog_toolset | Static hint toolset for leanix_reference_data_catalog based on config env. | leanix_reference_data_catalog | leanix-agent |
| leanix-agent_leanix_metrics_toolset | Static hint toolset for leanix_metrics based on config env. | leanix_metrics | leanix-agent |
| leanix-agent_leanix_discovery_saas_toolset | Static hint toolset for leanix_discovery_saas based on config env. | leanix_discovery_saas | leanix-agent |
| leanix-agent_leanix_mtm_toolset | Static hint toolset for leanix_mtm based on config env. | leanix_mtm | leanix-agent |
| leanix-agent_leanix_webhooks_toolset | Static hint toolset for leanix_webhooks based on config env. | leanix_webhooks | leanix-agent |
| leanix-agent_leanix_storage_toolset | Static hint toolset for leanix_storage based on config env. | leanix_storage | leanix-agent |
| leanix-agent_leanix_transformations_toolset | Static hint toolset for leanix_transformations based on config env. | leanix_transformations | leanix-agent |
| leanix-agent_leanix_integration_collibra_toolset | Static hint toolset for leanix_integration_collibra based on config env. | leanix_integration_collibra | leanix-agent |
| leanix-agent_leanix_discovery_sap_extension_toolset | Static hint toolset for leanix_discovery_sap_extension based on config env. | leanix_discovery_sap_extension | leanix-agent |
| leanix-agent_leanix_impacts_toolset | Static hint toolset for leanix_impacts based on config env. | leanix_impacts | leanix-agent |
| leanix-agent_leanix_technology_discovery_toolset | Static hint toolset for leanix_technology_discovery based on config env. | leanix_technology_discovery | leanix-agent |
| leanix-agent_leanix_ai_inventory_builder_toolset | Static hint toolset for leanix_ai_inventory_builder based on config env. | leanix_ai_inventory_builder | leanix-agent |
| leanix-agent_leanix_managed_code_execution_toolset | Static hint toolset for leanix_managed_code_execution based on config env. | leanix_managed_code_execution | leanix-agent |
| leanix-agent_graphql_toolset | Static hint toolset for graphql based on config env. | graphql | leanix-agent |
| leanix-agent_leanix_reference_data_toolset | Static hint toolset for leanix_reference_data based on config env. | leanix_reference_data | leanix-agent |
| leanix-agent_leanix_survey_toolset | Static hint toolset for leanix_survey based on config env. | leanix_survey | leanix-agent |
| leanix-agent_leanix_navigation_toolset | Static hint toolset for leanix_navigation based on config env. | leanix_navigation | leanix-agent |
| leanix-agent_leanix_integration_signavio_toolset | Static hint toolset for leanix_integration_signavio based on config env. | leanix_integration_signavio | leanix-agent |
| leanix-agent_leanix_pathfinder_toolset | Static hint toolset for leanix_pathfinder based on config env. | leanix_pathfinder | leanix-agent |
| leanix-agent_leanix_todo_toolset | Static hint toolset for leanix_todo based on config env. | leanix_todo | leanix-agent |
| leanix-agent_leanix_discovery_ai_agents_toolset | Static hint toolset for leanix_discovery_ai_agents based on config env. | leanix_discovery_ai_agents | leanix-agent |
| leanix-agent_leanix_integration_servicenow_toolset | Static hint toolset for leanix_integration_servicenow based on config env. | leanix_integration_servicenow | leanix-agent |
| leanix-agent_leanix_automations_toolset | Static hint toolset for leanix_automations based on config env. | leanix_automations | leanix-agent |
| leanix-agent_leanix_discovery_linking_v1_toolset | Static hint toolset for leanix_discovery_linking_v1 based on config env. | leanix_discovery_linking_v1 | leanix-agent |
| leanix-agent_leanix_discovery_sap_toolset | Static hint toolset for leanix_discovery_sap based on config env. | leanix_discovery_sap | leanix-agent |
| leanix-agent_leanix_synclog_toolset | Static hint toolset for leanix_synclog based on config env. | leanix_synclog | leanix-agent |
| leanix-agent_leanix_integration_api_toolset | Static hint toolset for leanix_integration_api based on config env. | leanix_integration_api | leanix-agent |
| leanix-agent_leanix_inventory_data_quality_toolset | Static hint toolset for leanix_inventory_data_quality based on config env. | leanix_inventory_data_quality | leanix-agent |
| leanix-agent_leanix_documents_toolset | Static hint toolset for leanix_documents based on config env. | leanix_documents | leanix-agent |
| leanix-agent_leanix_apptio_connector_toolset | Static hint toolset for leanix_apptio_connector based on config env. | leanix_apptio_connector | leanix-agent |
| get_startup_info | Get Startup Info | app | mealie-mcp |
| get_app_theme | Get App Theme | app | mealie-mcp |
| get_token | Get Token | users | mealie-mcp |
| oauth_login | Oauth Login | users | mealie-mcp |
| oauth_callback | Oauth Callback | users | mealie-mcp |
| refresh_token | Refresh Token | users | mealie-mcp |
| logout | Logout | users | mealie-mcp |
| register_new_user | Register New User | users | mealie-mcp |
| get_logged_in_user | Get Logged In User | users | mealie-mcp |
| get_logged_in_user_ratings | Get Logged In User Ratings | users | mealie-mcp |
| get_logged_in_user_rating_for_recipe | Get Logged In User Rating For Recipe | users | mealie-mcp |
| get_logged_in_user_favorites | Get Logged In User Favorites | users | mealie-mcp |
| update_password | Update Password | users | mealie-mcp |
| update_user | Update User | users | mealie-mcp |
| forgot_password | Forgot Password | users | mealie-mcp |
| reset_password | Reset Password | users | mealie-mcp |
| update_user_image | Update User Image | users | mealie-mcp |
| create | Create Api Token | users | mealie-mcp |
| delete | Delete Api Token | users | mealie-mcp |
| get_ratings | Get Ratings | users | mealie-mcp |
| get_favorites | Get Favorites | users | mealie-mcp |
| set_rating | Set Rating | users | mealie-mcp |
| add_favorite | Add Favorite | users | mealie-mcp |
| remove_favorite | Remove Favorite | users | mealie-mcp |
| get_households_cookbooks | Get All | households | mealie-mcp |
| post_households_cookbooks | Create One | households | mealie-mcp |
| put_households_cookbooks | Update Many | households | mealie-mcp |
| get_households_cookbooks_item_id | Get One | households | mealie-mcp |
| put_households_cookbooks_item_id | Update One | households | mealie-mcp |
| delete_households_cookbooks_item_id | Delete One | households | mealie-mcp |
| get_households_events_notifications | Get All | households | mealie-mcp |
| post_households_events_notifications | Create One | households | mealie-mcp |
| get_households_events_notifications_item_id | Get One | households | mealie-mcp |
| put_households_events_notifications_item_id | Update One | households | mealie-mcp |
| delete_households_events_notifications_item_id | Delete One | households | mealie-mcp |
| test_notification | Test Notification | households | mealie-mcp |
| get_households_recipe_actions | Get All | households | mealie-mcp |
| post_households_recipe_actions | Create One | households | mealie-mcp |
| get_households_recipe_actions_item_id | Get One | households | mealie-mcp |
| put_households_recipe_actions_item_id | Update One | households | mealie-mcp |
| delete_households_recipe_actions_item_id | Delete One | households | mealie-mcp |
| trigger_action | Trigger Action | households | mealie-mcp |
| get_logged_in_user_household | Get Logged In User Household | households | mealie-mcp |
| get_household_recipe | Get Household Recipe | households | mealie-mcp |
| get_household_members | Get Household Members | households | mealie-mcp |
| get_household_preferences | Get Household Preferences | households | mealie-mcp |
| update_household_preferences | Update Household Preferences | households | mealie-mcp |
| set_member_permissions | Set Member Permissions | households | mealie-mcp |
| get_statistics | Get Statistics | households | mealie-mcp |
| get_invite_tokens | Get Invite Tokens | households | mealie-mcp |
| create_invite_token | Create Invite Token | households | mealie-mcp |
| email_invitation | Email Invitation | households | mealie-mcp |
| get_households_shopping_lists | Get All | households | mealie-mcp |
| post_households_shopping_lists | Create One | households | mealie-mcp |
| get_households_shopping_lists_item_id | Get One | households | mealie-mcp |
| put_households_shopping_lists_item_id | Update One | households | mealie-mcp |
| delete_households_shopping_lists_item_id | Delete One | households | mealie-mcp |
| update_label_settings | Update Label Settings | households | mealie-mcp |
| add_recipe_ingredients_to_list | Add Recipe Ingredients To List | households | mealie-mcp |
| add_single_recipe_ingredients_to_list | Add Single Recipe Ingredients To List | households | mealie-mcp |
| remove_recipe_ingredients_from_list | Remove Recipe Ingredients From List | households | mealie-mcp |
| get_households_shopping_items | Get All | households | mealie-mcp |
| post_households_shopping_items | Create One | households | mealie-mcp |
| put_households_shopping_items | Update Many | households | mealie-mcp |
| delete_households_shopping_items | Delete Many | households | mealie-mcp |
| post_households_shopping_items_create_bulk | Create Many | households | mealie-mcp |
| get_households_shopping_items_item_id | Get One | households | mealie-mcp |
| put_households_shopping_items_item_id | Update One | households | mealie-mcp |
| delete_households_shopping_items_item_id | Delete One | households | mealie-mcp |
| get_households_webhooks | Get All | households | mealie-mcp |
| post_households_webhooks | Create One | households | mealie-mcp |
| rerun_webhooks | Rerun Webhooks | households | mealie-mcp |
| get_households_webhooks_item_id | Get One | households | mealie-mcp |
| put_households_webhooks_item_id | Update One | households | mealie-mcp |
| delete_households_webhooks_item_id | Delete One | households | mealie-mcp |
| test_one | Test One | households | mealie-mcp |
| get_households_mealplans_rules | Get All | households | mealie-mcp |
| post_households_mealplans_rules | Create One | households | mealie-mcp |
| get_households_mealplans_rules_item_id | Get One | households | mealie-mcp |
| put_households_mealplans_rules_item_id | Update One | households | mealie-mcp |
| delete_households_mealplans_rules_item_id | Delete One | households | mealie-mcp |
| get_households_mealplans | Get All | households | mealie-mcp |
| post_households_mealplans | Create One | households | mealie-mcp |
| get_todays_meals | Get Todays Meals | households | mealie-mcp |
| create_random_meal | Create Random Meal | households | mealie-mcp |
| get_households_mealplans_item_id | Get One | households | mealie-mcp |
| put_households_mealplans_item_id | Update One | households | mealie-mcp |
| delete_households_mealplans_item_id | Delete One | households | mealie-mcp |
| get_all_households | Get All Households | groups | mealie-mcp |
| get_one_household | Get One Household | groups | mealie-mcp |
| get_logged_in_user_group | Get Logged In User Group | groups | mealie-mcp |
| get_group_members | Get Group Members | groups | mealie-mcp |
| get_group_member | Get Group Member | groups | mealie-mcp |
| get_group_preferences | Get Group Preferences | groups | mealie-mcp |
| update_group_preferences | Update Group Preferences | groups | mealie-mcp |
| get_storage | Get Storage | groups | mealie-mcp |
| start_data_migration | Start Data Migration | groups | mealie-mcp |
| get_groups_reports | Get All | groups | mealie-mcp |
| get_groups_reports_item_id | Get One | groups | mealie-mcp |
| delete_groups_reports_item_id | Delete One | groups | mealie-mcp |
| get_groups_labels | Get All | groups | mealie-mcp |
| post_groups_labels | Create One | groups | mealie-mcp |
| get_groups_labels_item_id | Get One | groups | mealie-mcp |
| put_groups_labels_item_id | Update One | groups | mealie-mcp |
| delete_groups_labels_item_id | Delete One | groups | mealie-mcp |
| seed_foods | Seed Foods | groups | mealie-mcp |
| seed_labels | Seed Labels | groups | mealie-mcp |
| seed_units | Seed Units | groups | mealie-mcp |
| get_recipe_formats_and_templates | Get Recipe Formats And Templates | recipes | mealie-mcp |
| get_recipe_as_format | Get Recipe As Format | recipes | mealie-mcp |
| test_parse_recipe_url | Test Parse Recipe Url | recipes | mealie-mcp |
| create_recipe_from_html_or_json | Create Recipe From Html Or Json | recipes | mealie-mcp |
| parse_recipe_url | Parse Recipe Url | recipes | mealie-mcp |
| parse_recipe_url_bulk | Parse Recipe Url Bulk | recipes | mealie-mcp |
| create_recipe_from_zip | Create Recipe From Zip | recipes | mealie-mcp |
| create_recipe_from_image | Create Recipe From Image | recipes | mealie-mcp |
| get_recipes | Get All | recipes | mealie-mcp |
| post_recipes | Create One | recipes | mealie-mcp |
| put_recipes | Update Many | recipes | mealie-mcp |
| patch_many | Patch Many | recipes | mealie-mcp |
| get_recipes_suggestions | Suggest Recipes | recipes | mealie-mcp |
| get_recipes_slug | Get One | recipes | mealie-mcp |
| put_recipes_slug | Update One | recipes | mealie-mcp |
| patch_one | Patch One | recipes | mealie-mcp |
| delete_recipes_slug | Delete One | recipes | mealie-mcp |
| duplicate_one | Duplicate One | recipes | mealie-mcp |
| update_last_made | Update Last Made | recipes | mealie-mcp |
| scrape_image_url | Scrape Image Url | recipes | mealie-mcp |
| update_recipe_image | Update Recipe Image | recipes | mealie-mcp |
| delete_recipe_image | Delete Recipe Image | recipes | mealie-mcp |
| upload_recipe_asset | Upload Recipe Asset | recipes | mealie-mcp |
| get_recipe_comments | Get Recipe Comments | recipes | mealie-mcp |
| bulk_tag_recipes | Bulk Tag Recipes | recipes | mealie-mcp |
| bulk_settings_recipes | Bulk Settings Recipes | recipes | mealie-mcp |
| bulk_categorize_recipes | Bulk Categorize Recipes | recipes | mealie-mcp |
| bulk_delete_recipes | Bulk Delete Recipes | recipes | mealie-mcp |
| bulk_export_recipes | Bulk Export Recipes | recipes | mealie-mcp |
| get_exported_data | Get Exported Data | recipes | mealie-mcp |
| get_exported_data_token | Get Exported Data Token | recipes | mealie-mcp |
| purge_export_data | Purge Export Data | recipes | mealie-mcp |
| get_shared_recipe | Get Shared Recipe | recipes | mealie-mcp |
| get_shared_recipe_as_zip | Get Shared Recipe As Zip | recipes | mealie-mcp |
| get_recipes_timeline_events | Get All | recipes | mealie-mcp |
| post_recipes_timeline_events | Create One | recipes | mealie-mcp |
| get_recipes_timeline_events_item_id | Get One | recipes | mealie-mcp |
| put_recipes_timeline_events_item_id | Update One | recipes | mealie-mcp |
| delete_recipes_timeline_events_item_id | Delete One | recipes | mealie-mcp |
| update_event_image | Update Event Image | recipes | mealie-mcp |
| get_comments | Get All | recipes | mealie-mcp |
| post_comments | Create One | recipes | mealie-mcp |
| get_comments_item_id | Get One | recipes | mealie-mcp |
| put_comments_item_id | Update One | recipes | mealie-mcp |
| post_parser_ingredient | Delete One | recipes | mealie-mcp |
| parse_ingredient | Parse Ingredient | recipes | mealie-mcp |
| parse_ingredients | Parse Ingredients | recipes | mealie-mcp |
| get_foods | Get All | recipes | mealie-mcp |
| post_foods | Create One | recipes | mealie-mcp |
| put_foods_merge | Merge One | recipes | mealie-mcp |
| get_foods_item_id | Get One | recipes | mealie-mcp |
| put_foods_item_id | Update One | recipes | mealie-mcp |
| delete_foods_item_id | Delete One | recipes | mealie-mcp |
| get_units | Get All | recipes | mealie-mcp |
| post_units | Create One | recipes | mealie-mcp |
| put_units_merge | Merge One | recipes | mealie-mcp |
| get_units_item_id | Get One | recipes | mealie-mcp |
| put_units_item_id | Update One | recipes | mealie-mcp |
| delete_units_item_id | Delete One | recipes | mealie-mcp |
| get_recipe_img | Get Recipe Img | recipes | mealie-mcp |
| get_recipe_timeline_event_img | Get Recipe Timeline Event Img | recipes | mealie-mcp |
| get_recipe_asset | Get Recipe Asset | recipes | mealie-mcp |
| get_user_image | Get User Image | recipes | mealie-mcp |
| get_validation_text | Get Validation Text | recipes | mealie-mcp |
| get_organizers_categories | Get All | organizer | mealie-mcp |
| post_organizers_categories | Create One | organizer | mealie-mcp |
| get_all_empty | Get All Empty | organizer | mealie-mcp |
| get_organizers_categories_item_id | Get One | organizer | mealie-mcp |
| put_organizers_categories_item_id | Update One | organizer | mealie-mcp |
| delete_organizers_categories_item_id | Delete One | organizer | mealie-mcp |
| get_organizers_categories_slug_category_slug | Get One By Slug | organizer | mealie-mcp |
| get_organizers_tags | Get All | organizer | mealie-mcp |
| post_organizers_tags | Create One | organizer | mealie-mcp |
| get_empty_tags | Get Empty Tags | organizer | mealie-mcp |
| get_organizers_tags_item_id | Get One | organizer | mealie-mcp |
| put_organizers_tags_item_id | Update One | organizer | mealie-mcp |
| delete_recipe_tag | Delete Recipe Tag | organizer | mealie-mcp |
| get_organizers_tags_slug_tag_slug | Get One By Slug | organizer | mealie-mcp |
| get_organizers_tools | Get All | organizer | mealie-mcp |
| post_organizers_tools | Create One | organizer | mealie-mcp |
| get_organizers_tools_item_id | Get One | organizer | mealie-mcp |
| put_organizers_tools_item_id | Update One | organizer | mealie-mcp |
| delete_organizers_tools_item_id | Delete One | organizer | mealie-mcp |
| get_organizers_tools_slug_tool_slug | Get One By Slug | organizer | mealie-mcp |
| get_shared_recipes | Get All | shared | mealie-mcp |
| post_shared_recipes | Create One | shared | mealie-mcp |
| get_shared_recipes_item_id | Get One | shared | mealie-mcp |
| delete_shared_recipes_item_id | Delete One | shared | mealie-mcp |
| get_app_info | Get App Info | admin | mealie-mcp |
| get_app_statistics | Get App Statistics | admin | mealie-mcp |
| check_app_config | Check App Config | admin | mealie-mcp |
| get_admin_users | Get All | admin | mealie-mcp |
| post_admin_users | Create One | admin | mealie-mcp |
| unlock_users | Unlock Users | admin | mealie-mcp |
| get_admin_users_item_id | Get One | admin | mealie-mcp |
| put_admin_users_item_id | Update One | admin | mealie-mcp |
| delete_admin_users_item_id | Delete One | admin | mealie-mcp |
| generate_token | Generate Token | admin | mealie-mcp |
| get_admin_households | Get All | admin | mealie-mcp |
| post_admin_households | Create One | admin | mealie-mcp |
| get_admin_households_item_id | Get One | admin | mealie-mcp |
| put_admin_households_item_id | Update One | admin | mealie-mcp |
| delete_admin_households_item_id | Delete One | admin | mealie-mcp |
| get_admin_groups | Get All | admin | mealie-mcp |
| post_admin_groups | Create One | admin | mealie-mcp |
| get_admin_groups_item_id | Get One | admin | mealie-mcp |
| put_admin_groups_item_id | Update One | admin | mealie-mcp |
| delete_admin_groups_item_id | Delete One | admin | mealie-mcp |
| check_email_config | Check Email Config | admin | mealie-mcp |
| send_test_email | Send Test Email | admin | mealie-mcp |
| get_admin_backups | Get All | admin | mealie-mcp |
| post_admin_backups | Create One | admin | mealie-mcp |
| get_admin_backups_file_name | Get One | admin | mealie-mcp |
| delete_admin_backups_file_name | Delete One | admin | mealie-mcp |
| upload_one | Upload One | admin | mealie-mcp |
| import_one | Import One | admin | mealie-mcp |
| get_maintenance_summary | Get Maintenance Summary | admin | mealie-mcp |
| get_storage_details | Get Storage Details | admin | mealie-mcp |
| clean_images | Clean Images | admin | mealie-mcp |
| clean_temp | Clean Temp | admin | mealie-mcp |
| clean_recipe_folders | Clean Recipe Folders | admin | mealie-mcp |
| debug_openai | Debug Openai | admin | mealie-mcp |
| get_explore_groups_group_slug_foods | Get All | explore | mealie-mcp |
| get_explore_groups_group_slug_foods_item_id | Get One | explore | mealie-mcp |
| get_explore_groups_group_slug_households | Get All | explore | mealie-mcp |
| get_household | Get Household | explore | mealie-mcp |
| get_explore_groups_group_slug_organizers_categories | Get All | explore | mealie-mcp |
| get_explore_groups_group_slug_organizers_categories_item_id | Get One | explore | mealie-mcp |
| get_explore_groups_group_slug_organizers_tags | Get All | explore | mealie-mcp |
| get_explore_groups_group_slug_organizers_tags_item_id | Get One | explore | mealie-mcp |
| get_explore_groups_group_slug_organizers_tools | Get All | explore | mealie-mcp |
| get_explore_groups_group_slug_organizers_tools_item_id | Get One | explore | mealie-mcp |
| get_explore_groups_group_slug_cookbooks | Get All | explore | mealie-mcp |
| get_explore_groups_group_slug_cookbooks_item_id | Get One | explore | mealie-mcp |
| get_explore_groups_group_slug_recipes | Get All | explore | mealie-mcp |
| get_explore_groups_group_slug_recipes_suggestions | Suggest Recipes | explore | mealie-mcp |
| get_recipe | Get Recipe | explore | mealie-mcp |
| download_file | Download File | utils | mealie-mcp |
| media-downloader-mcp_text_editor_toolset | Static hint toolset for text_editor based on config env. | text_editor | media-downloader-mcp |
| media-downloader-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | media-downloader-mcp |
| media-downloader-mcp_collection_management_toolset | Static hint toolset for collection_management based on config env. | collection_management | media-downloader-mcp |
| microsoft-agent_auth_toolset | Static hint toolset for auth based on config env. | auth | microsoft-agent |
| microsoft-agent_groups_toolset | Static hint toolset for groups based on config env. | groups | microsoft-agent |
| microsoft-agent_agreements_toolset | Static hint toolset for agreements based on config env. | agreements | microsoft-agent |
| microsoft-agent_files_toolset | Static hint toolset for files based on config env. | files | microsoft-agent |
| microsoft-agent_notes_toolset | Static hint toolset for notes based on config env. | notes | microsoft-agent |
| microsoft-agent_organization_toolset | Static hint toolset for organization based on config env. | organization | microsoft-agent |
| microsoft-agent_audit_toolset | Static hint toolset for audit based on config env. | audit | microsoft-agent |
| microsoft-agent_places_toolset | Static hint toolset for places based on config env. | places | microsoft-agent |
| microsoft-agent_print_toolset | Static hint toolset for print based on config env. | print | microsoft-agent |
| microsoft-agent_tasks_toolset | Static hint toolset for tasks based on config env. | tasks | microsoft-agent |
| microsoft-agent_search_toolset | Static hint toolset for search based on config env. | search | microsoft-agent |
| microsoft-agent_employee_experience_toolset | Static hint toolset for employee_experience based on config env. | employee_experience | microsoft-agent |
| microsoft-agent_meta_toolset | Static hint toolset for meta based on config env. | meta | microsoft-agent |
| microsoft-agent_chat_toolset | Static hint toolset for chat based on config env. | chat | microsoft-agent |
| microsoft-agent_sites_toolset | Static hint toolset for sites based on config env. | sites | microsoft-agent |
| microsoft-agent_misc_toolset | Static hint toolset for misc based on config env. | misc | microsoft-agent |
| microsoft-agent_directory_toolset | Static hint toolset for directory based on config env. | directory | microsoft-agent |
| microsoft-agent_policies_toolset | Static hint toolset for policies based on config env. | policies | microsoft-agent |
| microsoft-agent_admin_toolset | Static hint toolset for admin based on config env. | admin | microsoft-agent |
| microsoft-agent_teams_toolset | Static hint toolset for teams based on config env. | teams | microsoft-agent |
| microsoft-agent_applications_toolset | Static hint toolset for applications based on config env. | applications | microsoft-agent |
| microsoft-agent_calendar_toolset | Static hint toolset for calendar based on config env. | calendar | microsoft-agent |
| microsoft-agent_reports_toolset | Static hint toolset for reports based on config env. | reports | microsoft-agent |
| microsoft-agent_privacy_toolset | Static hint toolset for privacy based on config env. | privacy | microsoft-agent |
| microsoft-agent_solutions_toolset | Static hint toolset for solutions based on config env. | solutions | microsoft-agent |
| microsoft-agent_subscriptions_toolset | Static hint toolset for subscriptions based on config env. | subscriptions | microsoft-agent |
| microsoft-agent_domains_toolset | Static hint toolset for domains based on config env. | domains | microsoft-agent |
| microsoft-agent_user_toolset | Static hint toolset for user based on config env. | user | microsoft-agent |
| microsoft-agent_connections_toolset | Static hint toolset for connections based on config env. | connections | microsoft-agent |
| microsoft-agent_storage_toolset | Static hint toolset for storage based on config env. | storage | microsoft-agent |
| microsoft-agent_security_toolset | Static hint toolset for security based on config env. | security | microsoft-agent |
| microsoft-agent_devices_toolset | Static hint toolset for devices based on config env. | devices | microsoft-agent |
| microsoft-agent_contacts_toolset | Static hint toolset for contacts based on config env. | contacts | microsoft-agent |
| microsoft-agent_education_toolset | Static hint toolset for education based on config env. | education | microsoft-agent |
| microsoft-agent_identity_toolset | Static hint toolset for identity based on config env. | identity | microsoft-agent |
| microsoft-agent_communications_toolset | Static hint toolset for communications based on config env. | communications | microsoft-agent |
| microsoft-agent_mail_toolset | Static hint toolset for mail based on config env. | mail | microsoft-agent |
| nextcloud-agent_user_toolset | Static hint toolset for user based on config env. | user | nextcloud-agent |
| nextcloud-agent_files_toolset | Static hint toolset for files based on config env. | files | nextcloud-agent |
| nextcloud-agent_sharing_toolset | Static hint toolset for sharing based on config env. | sharing | nextcloud-agent |
| nextcloud-agent_calendar_toolset | Static hint toolset for calendar based on config env. | calendar | nextcloud-agent |
| nextcloud-agent_misc_toolset | Static hint toolset for misc based on config env. | misc | nextcloud-agent |
| nextcloud-agent_contacts_toolset | Static hint toolset for contacts based on config env. | contacts | nextcloud-agent |
| owncast-chat-get-user-details | Get a user's details | chat | owncast |
| owncast-external-send-system-message | Send a system message to the chat | external | owncast |
| owncast-external-send-system-message-to-connected-client | Send a system message to a single client | external | owncast |
| owncast-external-send-user-message | Send a user message to chat | external | owncast |
| owncast-external-send-integration-chat-message | Send a message to chat as a specific 3rd party bot/integration based on its access token | external | owncast |
| owncast-external-send-chat-action | Send a user action to chat | external | owncast |
| owncast-external-update-message-visibility | Hide chat message | external | owncast |
| owncast-external-get-status | Get the server's status | external | owncast |
| owncast-external-set-stream-title | Stream title | external | owncast |
| owncast-external-get-chat-messages | Get chat history | external | owncast |
| owncast-external-get-connected-chat-clients | Connected clients | external | owncast |
| owncast-external-get-user-details | Get a user's details | external | owncast |
| owncast-internal-get-status | Get the status of the server | internal | owncast |
| owncast-internal-get-custom-emoji-list | Get list of custom emojis supported in the chat | internal | owncast |
| owncast-internal-get-chat-messages | Gets a list of chat messages | internal | owncast |
| owncast-internal-register-anonymous-chat-user | Registers an anonymous chat user | internal | owncast |
| owncast-internal-update-message-visibility | Update chat message visibility | internal | owncast |
| owncast-internal-update-user-enabled | Enable/disable a user | internal | owncast |
| owncast-internal-get-web-config | Get the web config | internal | owncast |
| owncast-internal-get-ypresponse | Get the YP protocol data | internal | owncast |
| owncast-internal-get-all-social-platforms | Get all social platforms | internal | owncast |
| owncast-internal-get-video-stream-output-variants | Get a list of video variants available | internal | owncast |
| owncast-internal-ping | Tell the backend you're an active viewer | internal | owncast |
| owncast-internal-remote-follow | Request remote follow | internal | owncast |
| owncast-internal-get-followers | Gets the list of followers | internal | owncast |
| owncast-internal-report-playback-metrics | Save video playback metrics for future video health recording | internal | owncast |
| owncast-internal-register-for-live-notifications | Register for notifications | internal | owncast |
| owncast-internal-status-admin | Get current inboard broadcaster | internal | owncast |
| owncast-internal-disconnect-inbound-connection | Disconnect inbound stream | internal | owncast |
| owncast-internal-get-server-config | Get the current server config | internal | owncast |
| owncast-internal-get-viewers-over-time | Get viewer count over time | internal | owncast |
| owncast-internal-get-active-viewers | Get active viewers | internal | owncast |
| owncast-internal-get-hardware-stats | Get the current hardware stats | internal | owncast |
| owncast-internal-get-connected-chat-clients | Get a detailed list of currently connected chat clients | internal | owncast |
| owncast-internal-get-chat-messages-admin | Get all chat messages for the admin, unfiltered | internal | owncast |
| owncast-internal-update-message-visibility-admin | Update visibility of chat messages | internal | owncast |
| owncast-internal-update-user-enabled-admin | Enable or disable a user | internal | owncast |
| owncast-internal-get-disabled-users | Get a list of disabled users | internal | owncast |
| owncast-internal-ban-ipaddress | Ban an IP address | internal | owncast |
| owncast-internal-unban-ipaddress | Remove an IP ban | internal | owncast |
| owncast-internal-get-ipaddress-bans | Get all banned IP addresses | internal | owncast |
| owncast-internal-update-user-moderator | Set moderator status for a user | internal | owncast |
| owncast-internal-get-moderators | Get a list of moderator users | internal | owncast |
| owncast-internal-get-logs | Get all logs | internal | owncast |
| owncast-internal-get-warnings | Get warning/error logs | internal | owncast |
| owncast-internal-get-followers-admin | Get followers | internal | owncast |
| owncast-internal-get-pending-follow-requests | Get a list of pending follow requests | internal | owncast |
| owncast-internal-get-blocked-and-rejected-followers | Get a list of rejected or blocked follows | internal | owncast |
| owncast-internal-approve-follower | Set the following state of a follower or follow request | internal | owncast |
| owncast-internal-upload-custom-emoji | Upload custom emoji | internal | owncast |
| owncast-internal-delete-custom-emoji | Delete custom emoji | internal | owncast |
| owncast-internal-set-admin-password | Change the current admin password | internal | owncast |
| owncast-internal-set-stream-keys | Set an array of valid stream keys | internal | owncast |
| owncast-internal-set-extra-page-content | Change the extra page content in memory | internal | owncast |
| owncast-internal-set-stream-title | Change the stream title | internal | owncast |
| owncast-internal-set-server-welcome-message | Change the welcome message | internal | owncast |
| owncast-internal-set-chat-disabled | Disable chat | internal | owncast |
| owncast-internal-set-chat-join-messages-enabled | Enable chat for user join messages | internal | owncast |
| owncast-internal-set-enable-established-chat-user-mode | Enable/disable chat established user mode | internal | owncast |
| owncast-internal-set-forbidden-username-list | Set chat usernames that are not allowed | internal | owncast |
| owncast-internal-set-suggested-username-list | Set the suggested chat usernames that will be assigned automatically | internal | owncast |
| owncast-internal-set-chat-spam-protection-enabled | Set spam protection enabled | internal | owncast |
| owncast-internal-set-chat-slur-filter-enabled | Set slur filter enabled | internal | owncast |
| owncast-internal-set-chat-require-authentication | Set require authentication for chat | internal | owncast |
| owncast-internal-set-video-codec | Set video codec | internal | owncast |
| owncast-internal-set-stream-latency-level | Set the number of video segments and duration per segment in a playlist | internal | owncast |
| owncast-internal-set-stream-output-variants | Set an array of video output configurations | internal | owncast |
| owncast-internal-set-custom-color-variable-values | Set style/color/css values | internal | owncast |
| owncast-internal-set-logo | Update logo | internal | owncast |
| owncast-internal-set-favicon | Upload custom favicon | internal | owncast |
| owncast-internal-reset-favicon | Reset favicon to default | internal | owncast |
| owncast-internal-set-tags | Update server tags | internal | owncast |
| owncast-internal-set-ffmpeg-path | Update FFMPEG path | internal | owncast |
| owncast-internal-set-web-server-port | Update server port | internal | owncast |
| owncast-internal-set-web-server-ip | Update server IP address | internal | owncast |
| owncast-internal-set-rtmpserver-port | Update RTMP post | internal | owncast |
| owncast-internal-set-socket-host-override | Update websocket host override | internal | owncast |
| owncast-internal-set-video-serving-endpoint | Update custom video serving endpoint | internal | owncast |
| owncast-internal-set-nsfw | Update NSFW marking | internal | owncast |
| owncast-internal-set-directory-enabled | Update directory enabled | internal | owncast |
| owncast-internal-set-social-handles | Update social handles | internal | owncast |
| owncast-internal-set-s3-configuration | Update S3 configuration | internal | owncast |
| owncast-internal-set-server-url | Update server url | internal | owncast |
| owncast-internal-set-external-actions | Update external action links | internal | owncast |
| owncast-internal-set-custom-styles | Update custom styles | internal | owncast |
| owncast-internal-set-custom-javascript | Update custom JavaScript | internal | owncast |
| owncast-internal-set-hide-viewer-count | Update hide viewer count | internal | owncast |
| owncast-internal-set-disable-search-indexing | Update search indexing | internal | owncast |
| owncast-internal-set-federation-enabled | Enable/disable federation features | internal | owncast |
| owncast-internal-set-federation-activity-private | Set if federation activities are private | internal | owncast |
| owncast-internal-set-federation-show-engagement | Set if fediverse engagement appears in chat | internal | owncast |
| owncast-internal-set-federation-username | Set local federated username | internal | owncast |
| owncast-internal-set-federation-go-live-message | Set federated go live message | internal | owncast |
| owncast-internal-set-federation-block-domains | Set Federation blocked domains | internal | owncast |
| owncast-internal-set-discord-notification-configuration | Configure Discord notifications | internal | owncast |
| owncast-internal-set-browser-notification-configuration | Configure Browser notifications | internal | owncast |
| owncast-internal-get-webhooks | Get all the webhooks | internal | owncast |
| owncast-internal-delete-webhook | Delete a single webhook | internal | owncast |
| owncast-internal-create-webhook | Create a single webhook | internal | owncast |
| owncast-internal-get-external-apiusers | Get all access tokens | internal | owncast |
| owncast-internal-delete-external-apiuser | Delete a single external API user | internal | owncast |
| owncast-internal-create-external-apiuser | Create a single access token | internal | owncast |
| owncast-internal-auto-update-options | Return the auto-update features that are supported for this instance | internal | owncast |
| owncast-internal-auto-update-start | Begin the auto-update | internal | owncast |
| owncast-internal-auto-update-force-quit | Force quit the server and restart it | internal | owncast |
| owncast-internal-reset-ypregistration | Reset YP configuration | internal | owncast |
| owncast-internal-get-video-playback-metrics | Get video playback metrics | internal | owncast |
| owncast-internal-get-prometheus-api | Endpoint to interface with Prometheus | internal | owncast |
| owncast-internal-post-prometheus-api | Endpoint to interface with Prometheus | internal | owncast |
| owncast-internal-put-prometheus-api | Endpoint to interface with Prometheus | internal | owncast |
| owncast-internal-delete-prometheus-api | Endpoint to interface with Prometheus | internal | owncast |
| owncast-internal-send-federated-message | Send a public message to the Fediverse from the server's user | internal | owncast |
| owncast-internal-get-federated-actions | Get a paginated list of federated activities | internal | owncast |
| owncast-internal-start-indie-auth-flow | Begins auth flow | internal | owncast |
| owncast-internal-handle-indie-auth-redirect | Handle the redirect from an IndieAuth server to continue the auth flow | internal | owncast |
| owncast-internal-handle-indie-auth-endpoint-get | Handles the IndieAuth auth endpoint | internal | owncast |
| owncast-internal-handle-indie-auth-endpoint-post | Handles IndieAuth from form submission | internal | owncast |
| owncast-internal-register-fediverse-otprequest | Register a Fediverse OTP request | internal | owncast |
| owncast-internal-verify-fediverse-otprequest | Verify Fediverse OTP code | internal | owncast |
| owncast-objects-set-server-name | Change the server name | objects | owncast |
| owncast-objects-set-server-summary | Change the server summary | objects | owncast |
| owncast-objects-set-custom-offline-message | Change the offline message | objects | owncast |
| list_projects | List all projects in the workspace. | projects | plane |
| retrieve_project | Retrieve a project by ID. | projects | plane |
| list_work_items | List work items in a project or search across workspace. | work_items | plane |
| create_work_item | Create a new work item. | work_items | plane |
| update_work_item | Update a work item. | work_items | plane |
| delete_work_item | Delete a work item. | work_items | plane |
| search_work_items | Search work items across workspace. | work_items | plane |
| retrieve_work_item_by_identifier | Retrieve a work item by project identifier and issue sequence number. | work_items | plane |
| retrieve_work_item | Retrieve a work item by ID. | work_items | plane |
| list_work_item_activities | List activities for a work item. | work_items | plane |
| list_work_item_comments | List comments for a work item. | work_items | plane |
| create_work_item_comment | Create a comment for a work item. | work_items | plane |
| list_work_item_links | List links for a work item. | work_items | plane |
| create_work_item_link | Create a link for a work item. | work_items | plane |
| list_work_item_relations | List relations for a work item. | work_items | plane |
| list_work_item_types | List work item types in a project. | work_items | plane |
| list_work_logs | List work logs for a work item. | work_items | plane |
| create_work_log | Create a work log for a work item. | work_items | plane |
| list_cycles | List cycles in a project. | cycles | plane |
| create_cycle | Create a new cycle. | cycles | plane |
| retrieve_cycle | Retrieve a cycle by ID. | cycles | plane |
| update_cycle | Update a cycle by ID. | cycles | plane |
| delete_cycle | Delete a cycle by ID. | cycles | plane |
| list_cycle_work_items | List work items in a cycle. | cycles | plane |
| add_work_items_to_cycle | Add work items to a cycle. | cycles | plane |
| list_epics | List epics in a project. | epics | plane |
| create_epic | Create a new epic. | epics | plane |
| retrieve_epic | Retrieve an epic by ID. | epics | plane |
| update_epic | Update an epic by ID. | epics | plane |
| delete_epic | Delete an epic by ID. | epics | plane |
| list_initiatives | List all initiatives in the workspace. | initiatives | plane |
| create_initiative | Create a new initiative. | initiatives | plane |
| list_intake_work_items | List all intake work items in a project. | intake | plane |
| create_intake_work_item | Create a new intake work item. | intake | plane |
| list_labels | List all labels in a project. | labels | plane |
| create_label | Create a new label. | labels | plane |
| retrieve_project_page | Retrieve a project page by ID. | pages | plane |
| create_project_page | Create a project page. | pages | plane |
| list_milestones | List milestones in a project. | milestones | plane |
| create_milestone | Create a new milestone. | milestones | plane |
| retrieve_milestone | Retrieve a milestone by ID. | milestones | plane |
| update_milestone | Update a milestone by ID. | milestones | plane |
| delete_milestone | Delete a milestone by ID. | milestones | plane |
| list_modules | List modules in a project. | modules | plane |
| create_module | Create a new module. | modules | plane |
| retrieve_module | Retrieve a module by ID. | modules | plane |
| update_module | Update a module by ID. | modules | plane |
| delete_module | Delete a module by ID. | modules | plane |
| list_states | List states in a project. | states | plane |
| create_state | Create a new state. | states | plane |
| list_users | List users in the workspace. | users | plane |
| get_me | Get current user information. | users | plane |
| get_workspace | Get current workspace details. | workspaces | plane |
| get_workspace_members | Get all members of the current workspace. | workspaces | plane |
| get_workspace_features | Get features of the current workspace. | workspaces | plane |
| update_workspace_features | Update features of the current workspace. | workspaces | plane |
| authenticate | Authenticate against Portainer with username and password to get a JWT token. | Auth | portainer-agent |
| logout | Logout and invalidate the current authentication token. | Auth | portainer-agent |
| validate_oauth | Validate an OAuth authorization code. | Auth | portainer-agent |
| get_endpoints | List all Portainer environments (endpoints). Each environment represents a Docker host, Swarm cluster, or Kubernetes cluster. | Environment | portainer-agent |
| get_endpoint | Get details of a specific environment (endpoint) by ID. | Environment | portainer-agent |
| create_endpoint | Create a new environment. Types: 1=Docker, 2=AgentOnDocker, 3=Azure, 4=EdgeAgent, 5=KubernetesLocal, 6=AgentOnKubernetes, 7=EdgeAgentOnKubernetes. | Environment | portainer-agent |
| update_endpoint | Update an existing environment's configuration. | Environment | portainer-agent |
| delete_endpoint | Delete an environment (endpoint). | Environment | portainer-agent |
| snapshot_endpoint | Take a snapshot of an environment to refresh its state. | Environment | portainer-agent |
| snapshot_all_endpoints | Take a snapshot of all environments. | Environment | portainer-agent |
| get_endpoint_groups | List all environment groups. | Environment | portainer-agent |
| create_endpoint_group | Create a new environment group. | Environment | portainer-agent |
| delete_endpoint_group | Delete an environment group. | Environment | portainer-agent |
| get_docker_dashboard | Get Docker dashboard data (containers, images, volumes, networks summary) for an environment. | Docker | portainer-agent |
| get_container_gpus | Get GPU information for a Docker container. | Docker | portainer-agent |
| docker_list_containers | List containers in a Docker environment. | Docker | portainer-agent |
| docker_inspect_container | Return low-level information about a container. | Docker | portainer-agent |
| docker_get_container_logs | Get stdout and stderr logs from a container. | Docker | portainer-agent |
| docker_get_container_stats | Get resource usage statistics for a container. | Docker | portainer-agent |
| docker_start_container | Start a container. | Docker | portainer-agent |
| docker_stop_container | Stop a container. | Docker | portainer-agent |
| docker_restart_container | Restart a container. | Docker | portainer-agent |
| docker_remove_container | Remove a container. | Docker | portainer-agent |
| docker_list_services | List Swarm services in a Docker environment. | Docker | portainer-agent |
| docker_inspect_service | Return low-level information about a Swarm service. | Docker | portainer-agent |
| docker_get_service_logs | Get stdout and stderr logs from a Swarm service. | Docker | portainer-agent |
| docker_list_images | List images in a Docker environment. | Docker | portainer-agent |
| docker_inspect_image | Return low-level information about an image. | Docker | portainer-agent |
| docker_list_networks | List networks in a Docker environment. | Docker | portainer-agent |
| docker_inspect_network | Return low-level information about a network. | Docker | portainer-agent |
| docker_list_volumes | List volumes in a Docker environment. | Docker | portainer-agent |
| docker_inspect_volume | Return low-level information about a volume. | Docker | portainer-agent |
| docker_get_info | Get system-wide information for the Docker host. | Docker | portainer-agent |
| docker_get_version | Get Docker version information. | Docker | portainer-agent |
| docker_get_system_df | Get Docker data usage information. | Docker | portainer-agent |
| docker_create_container | Create a new container. | Docker | portainer-agent |
| docker_create_network | Create a new network. | Docker | portainer-agent |
| docker_create_volume | Create a new volume. | Docker | portainer-agent |
| docker_create_exec | Create an exec instance in a container. | Docker | portainer-agent |
| docker_start_exec | Start an exec instance. | Docker | portainer-agent |
| docker_inspect_exec | Inspect an exec instance. | Docker | portainer-agent |
| docker_get_stack_logs | Get aggregated logs for all containers or services in a Portainer stack. | Docker, Stack | portainer-agent |
| get_stacks | List all stacks across all environments. | Stack | portainer-agent |
| get_stack | Get details of a specific stack by ID. | Stack | portainer-agent |
| get_stack_file | Get the Docker Compose/manifest file content for a stack. | Stack | portainer-agent |
| create_standalone_stack | Create a standalone Docker Compose stack from compose file content. | Stack | portainer-agent |
| create_standalone_stack_from_repo | Create a standalone Docker Compose stack from a Git repository. | Stack | portainer-agent |
| update_stack | Update a stack's configuration. | Stack | portainer-agent |
| delete_stack | Delete a stack. | Stack | portainer-agent |
| start_stack | Start a stopped stack. | Stack | portainer-agent |
| stop_stack | Stop a running stack. | Stack | portainer-agent |
| redeploy_stack_git | Redeploy a stack from its Git repository (pull latest and redeploy). | Stack | portainer-agent |
| get_kubernetes_dashboard | Get Kubernetes dashboard data for an environment (pods, services, deployments summary). | Kubernetes | portainer-agent |
| get_kubernetes_namespaces | List Kubernetes namespaces in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_applications | List Kubernetes applications (deployments, statefulsets, daemonsets) in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_services | List Kubernetes services in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_ingresses | List Kubernetes ingresses in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_configmaps | List Kubernetes configmaps in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_secrets | List Kubernetes secrets in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_volumes | List Kubernetes persistent volume claims in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_events | List Kubernetes events in an environment. | Kubernetes | portainer-agent |
| get_kubernetes_nodes_limits | Get Kubernetes node resource limits for capacity planning. | Kubernetes | portainer-agent |
| get_kubernetes_metrics_nodes | Get resource metrics for Kubernetes nodes. | Kubernetes | portainer-agent |
| get_helm_releases | List Helm releases installed in an environment. | Kubernetes | portainer-agent |
| install_helm_chart | Install a Helm chart in an environment. | Kubernetes | portainer-agent |
| delete_helm_release | Delete (uninstall) a Helm release. | Kubernetes | portainer-agent |
| get_edge_groups | List all edge groups. | Edge | portainer-agent |
| create_edge_group | Create an edge group for organizing edge devices. | Edge | portainer-agent |
| delete_edge_group | Delete an edge group. | Edge | portainer-agent |
| get_edge_stacks | List all edge stacks deployed to edge groups. | Edge | portainer-agent |
| get_edge_stack | Get details of a specific edge stack. | Edge | portainer-agent |
| create_edge_stack | Create an edge stack from compose file content. | Edge | portainer-agent |
| delete_edge_stack | Delete an edge stack. | Edge | portainer-agent |
| get_edge_jobs | List all edge jobs. | Edge | portainer-agent |
| get_edge_job | Get details of a specific edge job. | Edge | portainer-agent |
| create_edge_job | Create an edge job to execute scripts on edge devices. | Edge | portainer-agent |
| delete_edge_job | Delete an edge job. | Edge | portainer-agent |
| get_templates | List available app templates. | Template | portainer-agent |
| get_custom_templates | List custom templates created by users. | Template | portainer-agent |
| get_custom_template | Get details of a specific custom template. | Template | portainer-agent |
| create_custom_template | Create a custom template from compose file content. Types: 1=swarm, 2=compose, 3=kubernetes. | Template | portainer-agent |
| delete_custom_template | Delete a custom template. | Template | portainer-agent |
| get_custom_template_file | Get the compose file content of a custom template. | Template | portainer-agent |
| get_helm_templates | List available Helm chart templates. | Template | portainer-agent |
| get_users | List all Portainer users. | User | portainer-agent |
| get_user | Get details of a specific user. | User | portainer-agent |
| get_current_user | Get the currently authenticated user's profile. | User | portainer-agent |
| create_user | Create a new Portainer user. Roles: 1=admin, 2=standard. | User | portainer-agent |
| delete_user | Delete a Portainer user. | User | portainer-agent |
| get_teams | List all teams. | User | portainer-agent |
| create_team | Create a new team. | User | portainer-agent |
| delete_team | Delete a team. | User | portainer-agent |
| get_roles | List all available roles. | User | portainer-agent |
| get_user_tokens | List API tokens for a user. | User | portainer-agent |
| get_registries | List all configured Docker registries. | Registry | portainer-agent |
| get_registry | Get details of a specific registry. | Registry | portainer-agent |
| create_registry | Add a Docker registry. Types: 1=Quay, 2=Azure, 3=Custom, 4=GitLab, 5=ProGet, 6=DockerHub, 7=ECR, 8=GitHub. | Registry | portainer-agent |
| delete_registry | Delete a Docker registry. | Registry | portainer-agent |
| get_status | Get Portainer instance status (version, uptime, etc.). | System | portainer-agent |
| get_system_info | Get detailed system information (build info, dependencies, runtime). | System | portainer-agent |
| get_system_version | Get Portainer version information. | System | portainer-agent |
| get_settings | Get Portainer settings (authentication, templates URL, edge agent, etc.). | System | portainer-agent |
| update_settings | Update Portainer settings. | System | portainer-agent |
| get_tags | List all tags used for organizing environments. | System | portainer-agent |
| create_tag | Create a tag for organizing environments. | System | portainer-agent |
| delete_tag | Delete a tag. | System | portainer-agent |
| get_motd | Get the Portainer message of the day. | System | portainer-agent |
| backup_portainer | Create a backup of all Portainer data. | System | portainer-agent |
| postiz_analytics_toolset | Static hint toolset for analytics based on config env. | analytics | postiz |
| postiz_integrations_toolset | Static hint toolset for integrations based on config env. | integrations | postiz |
| postiz_notifications_toolset | Static hint toolset for notifications based on config env. | notifications | postiz |
| postiz_posts_toolset | Static hint toolset for posts based on config env. | posts | postiz |
| postiz_uploads_toolset | Static hint toolset for uploads based on config env. | uploads | postiz |
| postiz_video_toolset | Static hint toolset for video based on config env. | video | postiz |
| qbittorrent_general_tools | General tools for qbittorrent (offline extraction). | qbittorrent | qbittorrent |
| repository-manager_file_operations_toolset | Static hint toolset for file_operations based on config env. | file_operations | repository-manager |
| repository-manager_misc_toolset | Static hint toolset for misc based on config env. | misc | repository-manager |
| repository-manager_git_operations_toolset | Static hint toolset for git_operations based on config env. | git_operations | repository-manager |
| repository-manager_graph_intelligence_toolset | Static hint toolset for graph_intelligence based on config env. | graph_intelligence | repository-manager |
| repository-manager_visualization_toolset | Static hint toolset for visualization based on config env. | visualization | repository-manager |
| repository-manager_workspace_management_toolset | Static hint toolset for workspace_management based on config env. | workspace_management | repository-manager |
| searxng-mcp_search_toolset | Static hint toolset for search based on config env. | search | searxng-mcp |
| searxng-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | searxng-mcp |
| servicenow-api_account_toolset | Static hint toolset for account based on config env. | account | servicenow-api |
| servicenow-api_activity_subscriptions_toolset | Static hint toolset for activity_subscriptions based on config env. | activity_subscriptions | servicenow-api |
| servicenow-api_aggregate_toolset | Static hint toolset for aggregate based on config env. | aggregate | servicenow-api |
| servicenow-api_application_toolset | Static hint toolset for application based on config env. | application | servicenow-api |
| servicenow-api_attachment_toolset | Static hint toolset for attachment based on config env. | attachment | servicenow-api |
| servicenow-api_auth_toolset | Static hint toolset for auth based on config env. | auth | servicenow-api |
| servicenow-api_batch_toolset | Static hint toolset for batch based on config env. | batch | servicenow-api |
| servicenow-api_change_management_toolset | Static hint toolset for change_management based on config env. | change_management | servicenow-api |
| servicenow-api_cicd_toolset | Static hint toolset for cicd based on config env. | cicd | servicenow-api |
| servicenow-api_cilifecycle_toolset | Static hint toolset for cilifecycle based on config env. | cilifecycle | servicenow-api |
| servicenow-api_cmdb_toolset | Static hint toolset for cmdb based on config env. | cmdb | servicenow-api |
| servicenow-api_custom_api_toolset | Static hint toolset for custom_api based on config env. | custom_api | servicenow-api |
| servicenow-api_data_classification_toolset | Static hint toolset for data_classification based on config env. | data_classification | servicenow-api |
| servicenow-api_devops_toolset | Static hint toolset for devops based on config env. | devops | servicenow-api |
| servicenow-api_email_toolset | Static hint toolset for email based on config env. | email | servicenow-api |
| servicenow-api_flows_toolset | Static hint toolset for flows based on config env. | flows | servicenow-api |
| servicenow-api_hr_toolset | Static hint toolset for hr based on config env. | hr | servicenow-api |
| servicenow-api_import_sets_toolset | Static hint toolset for import_sets based on config env. | import_sets | servicenow-api |
| servicenow-api_incidents_toolset | Static hint toolset for incidents based on config env. | incidents | servicenow-api |
| servicenow-api_knowledge_management_toolset | Static hint toolset for knowledge_management based on config env. | knowledge_management | servicenow-api |
| servicenow-api_metricbase_toolset | Static hint toolset for metricbase based on config env. | metricbase | servicenow-api |
| servicenow-api_misc_toolset | Static hint toolset for misc based on config env. | misc | servicenow-api |
| servicenow-api_plugins_toolset | Static hint toolset for plugins based on config env. | plugins | servicenow-api |
| servicenow-api_ppm_toolset | Static hint toolset for ppm based on config env. | ppm | servicenow-api |
| servicenow-api_product_inventory_toolset | Static hint toolset for product_inventory based on config env. | product_inventory | servicenow-api |
| servicenow-api_service_qualification_toolset | Static hint toolset for service_qualification based on config env. | service_qualification | servicenow-api |
| servicenow-api_source_control_toolset | Static hint toolset for source_control based on config env. | source_control | servicenow-api |
| servicenow-api_table_api_toolset | Static hint toolset for table_api based on config env. | table_api | servicenow-api |
| servicenow-api_testing_toolset | Static hint toolset for testing based on config env. | testing | servicenow-api |
| servicenow-api_update_sets_toolset | Static hint toolset for update_sets based on config env. | update_sets | servicenow-api |
| add_watermark | Add a watermark to a PDF file. | PDF | stirlingpdf-agent |
| systems-manager_text_editor_toolset | Static hint toolset for text_editor based on config env. | text_editor | systems-manager |
| systems-manager_filesystem_toolset | Static hint toolset for filesystem based on config env. | filesystem | systems-manager |
| systems-manager_process_toolset | Static hint toolset for process based on config env. | process | systems-manager |
| systems-manager_log_toolset | Static hint toolset for log based on config env. | log | systems-manager |
| systems-manager_user_toolset | Static hint toolset for user based on config env. | user | systems-manager |
| systems-manager_ssh_management_toolset | Static hint toolset for ssh_management based on config env. | ssh_management | systems-manager |
| systems-manager_shell_toolset | Static hint toolset for shell based on config env. | shell | systems-manager |
| systems-manager_system_toolset | Static hint toolset for system based on config env. | system | systems-manager |
| systems-manager_cron_toolset | Static hint toolset for cron based on config env. | cron | systems-manager |
| systems-manager_network_toolset | Static hint toolset for network based on config env. | network | systems-manager |
| systems-manager_nodejs_toolset | Static hint toolset for nodejs based on config env. | nodejs | systems-manager |
| systems-manager_service_toolset | Static hint toolset for service based on config env. | service | systems-manager |
| systems-manager_system_management_toolset | Static hint toolset for system_management based on config env. | system_management | systems-manager |
| systems-manager_firewall_management_toolset | Static hint toolset for firewall_management based on config env. | firewall_management | systems-manager |
| systems-manager_python_toolset | Static hint toolset for python based on config env. | python | systems-manager |
| systems-manager_misc_toolset | Static hint toolset for misc based on config env. | misc | systems-manager |
| systems-manager_disk_toolset | Static hint toolset for disk based on config env. | disk | systems-manager |
| list_hosts | List all managed hosts in the inventory. | host_management | tunnel-manager-mcp |
| add_host | Add a new host to the managed inventory. | host_management | tunnel-manager-mcp |
| remove_host | Remove a host from the managed inventory. | host_management | tunnel-manager-mcp |
| run_command_on_remote_host | Run shell command on remote host. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| send_file_to_remote_host | Upload file to remote host. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| receive_file_from_remote_host | Download file from remote host. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| check_ssh_server | Check SSH server status. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| test_key_auth | Test key-based auth. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| setup_passwordless_ssh | Setup passwordless SSH. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| copy_ssh_config | Copy SSH config to remote host. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| rotate_ssh_key | Rotate SSH key on remote host. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| remove_host_key | Remove host key from known_hosts. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| configure_key_auth_on_inventory | Setup passwordless SSH for all hosts in group. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| run_command_on_inventory | Run command on all hosts in group. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| copy_ssh_config_on_inventory | Copy SSH config to all hosts in YAML group. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| rotate_ssh_key_on_inventory | Rotate SSH keys for all hosts in YAML group. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| send_file_to_inventory | Upload a file to all hosts in the specified inventory group. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| receive_file_from_inventory | Download a file from all hosts in the specified inventory group. Expected return object type: dict | remote_access | tunnel-manager-mcp |
| uptime-kuma-get-monitors | Get all monitors | uptime | uptime |
| uptime-kuma-get-monitor | Get a specific monitor by ID | uptime | uptime |
| uptime-kuma-add-monitor | Add a new monitor | uptime | uptime |
| uptime-kuma-edit-monitor | Edit an existing monitor | uptime | uptime |
| uptime-kuma-delete-monitor | Delete a monitor | uptime | uptime |
| uptime-kuma-pause-monitor | Pause a monitor | uptime | uptime |
| uptime-kuma-resume-monitor | Resume a monitor | uptime | uptime |
| uptime-kuma-get-status | Get status for a specific monitor | uptime | uptime |
| uptime-kuma-get-uptime | Get uptime percentages for monitors | uptime | uptime |
| vector-mcp_search_toolset | Static hint toolset for search based on config env. | search | vector-mcp |
| vector-mcp_misc_toolset | Static hint toolset for misc based on config env. | misc | vector-mcp |
| vector-mcp_collection_management_toolset | Static hint toolset for collection_management based on config env. | collection_management | vector-mcp |
| get_routines | List all workout routines for the authenticated user. | Routine | wger-agent |
| get_routine | Get a specific routine by ID. | Routine | wger-agent |
| create_routine | Create a new workout routine. | Routine | wger-agent |
| delete_routine | Delete a routine. | Routine | wger-agent |
| get_days | List workout days. Filter by routine with routine=<id>. | Routine | wger-agent |
| create_day | Create a workout day in a routine. | Routine | wger-agent |
| delete_day | Delete a workout day. | Routine | wger-agent |
| get_slots | List exercise slots (sets) in workout days. | Routine | wger-agent |
| create_slot | Create an exercise slot (set) in a day. | Routine | wger-agent |
| create_slot_entry | Add an exercise to a slot. | Routine | wger-agent |
| get_templates | List user's workout templates. | Routine | wger-agent |
| get_public_templates | List publicly shared workout templates. | Routine | wger-agent |
| create_weight_config | Create a weight progression config for a slot entry. Controls how weight progresses across iterations. | RoutineConfig | wger-agent |
| get_weight_configs | List weight progression configs. | RoutineConfig | wger-agent |
| create_repetitions_config | Create a repetitions progression config for a slot entry. | RoutineConfig | wger-agent |
| get_repetitions_configs | List repetitions configs. | RoutineConfig | wger-agent |
| create_sets_config | Create a sets count progression config for a slot entry. | RoutineConfig | wger-agent |
| create_rest_config | Create a rest time progression config for a slot entry. | RoutineConfig | wger-agent |
| create_rir_config | Create a RiR (Reps in Reserve) progression config for a slot entry. | RoutineConfig | wger-agent |
| get_exercises | List exercises from the exercise database. Supports filters: language, category, muscles, equipment. | Exercise | wger-agent |
| get_exercise_info | Get detailed exercise info including translations, images, muscles worked, and equipment. | Exercise | wger-agent |
| search_exercises | Search exercises by name. Returns exercise info entries matching the search term. | Exercise | wger-agent |
| get_exercise_categories | List exercise categories (e.g., Arms, Legs, Chest, Back, etc.). | Exercise | wger-agent |
| get_equipment | List available equipment (e.g., Barbell, Dumbbell, Kettlebell, etc.). | Exercise | wger-agent |
| get_muscles | List muscles (e.g., Biceps, Pectoralis, Quadriceps, etc.). | Exercise | wger-agent |
| get_exercise_images | List exercise images. Filter by exercise with exercise_base=<id>. | Exercise | wger-agent |
| get_variations | List exercise variation groups. | Exercise | wger-agent |
| get_workout_sessions | List workout sessions. | Workout | wger-agent |
| get_workout_session | Get a specific workout session. | Workout | wger-agent |
| create_workout_session | Create a workout session. Impression: 1=Discomfort, 2=Could be better, 3=Neutral, 4=Good, 5=Perfect. | Workout | wger-agent |
| delete_workout_session | Delete a workout session. | Workout | wger-agent |
| get_workout_logs | List workout log entries. | Workout | wger-agent |
| create_workout_log | Log a set performed during a workout (exercise, weight, reps, date). | Workout | wger-agent |
| delete_workout_log | Delete a workout log entry. | Workout | wger-agent |
| get_nutrition_plans | List nutrition plans. | Nutrition | wger-agent |
| get_nutrition_plan_info | Get detailed nutrition plan with meals, items, and nutritional totals. | Nutrition | wger-agent |
| create_nutrition_plan | Create a nutrition plan with optional macro goals. | Nutrition | wger-agent |
| delete_nutrition_plan | Delete a nutrition plan. | Nutrition | wger-agent |
| create_meal | Create a meal in a nutrition plan. | Nutrition | wger-agent |
| create_meal_item | Add an ingredient to a meal. | Nutrition | wger-agent |
| get_ingredients | List/search ingredients from the food database. | Nutrition | wger-agent |
| get_ingredient_info | Get detailed ingredient info including nutritional values and weight units. | Nutrition | wger-agent |
| get_nutrition_diary | List nutrition diary entries. | Nutrition | wger-agent |
| log_nutrition | Log a nutrition diary entry (what was actually eaten). | Nutrition | wger-agent |
| get_weight_entries | List body weight entries over time. | Body | wger-agent |
| log_body_weight | Log a body weight entry. | Body | wger-agent |
| delete_weight_entry | Delete a body weight entry. | Body | wger-agent |
| get_measurements | List body measurements (biceps, chest, waist, etc.). | Body | wger-agent |
| log_measurement | Log a body measurement. | Body | wger-agent |
| get_measurement_categories | List measurement categories (e.g., Biceps, Chest, Waist). | Body | wger-agent |
| create_measurement_category | Create a new measurement category. | Body | wger-agent |
| get_gallery | List progress gallery photos. | Body | wger-agent |
| get_user_profile | Get the authenticated user's profile (age, height, gender, etc.). | User | wger-agent |
| get_user_statistics | Get user statistics (workout counts, etc.). | User | wger-agent |
| get_user_trophies | List user's earned trophies/achievements. | User | wger-agent |
| get_languages | List available languages. | User | wger-agent |
| get_repetition_units | List repetition unit settings (e.g., Repetitions, Until failure, etc.). | User | wger-agent |
| get_weight_unit_settings | List weight unit settings (kg, lb, plates, etc.). | User | wger-agent |

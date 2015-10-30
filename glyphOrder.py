f = CurrentFont()

gO = ['bn_chandrabindu', 'bn_anusvar', 'bn_bisarga', 'bn_a', 'bn_aa', 'bn_i', 'bn_ii', 'bn_u', 'bn_uu', 'bn_ri', 'bn_li', 'bn_e', 'bn_ai', 'bn_o', 'bn_au', 'bn_ka', 'bn_kha', 'bn_ga', 'bn_gha', 'bn_nga', 'bn_ca', 'bn_cha', 'bn_ja', 'bn_jha', 'bn_nya', 'bn_tta', 'bn_ttha', 'bn_dda', 'bn_ddha', 'bn_nna', 'bn_ta', 'bn_tha', 'bn_da', 'bn_dha', 'bn_na', 'bn_pa', 'bn_pha', 'bn_ba', 'bn_bha', 'bn_ma', 'bn_ya', 'bn_ra', 'bn_la', 'bn_sha', 'bn_ssa', 'bn_sa', 'bn_ha', 'bn_nukta', 'bn_avagraha', 'bn_aakaar', 'bn_ikaar', 'bn_iikaar', 'bn_ukaar', 'bn_uukaar', 'bn_rikaar', 'bn_rrikaar', 'bn_ekaar', 'bn_ekaar.init', 'bn_aikaar', 'bn_aikaar.init', 'bn_okaar', 'bn_aukaar', 'bn_halanth', 'bn_khanda_ta', 'bn_aumark', 'bn_rra', 'bn_rha', 'bn_yya', 'asa_ra', 'asa_ba', 'bn_rri', 'bn_lli', 'bn_likaar', 'bn_llikaar', 'bn_zero', 'bn_one', 'bn_two', 'bn_three', 'bn_four', 'bn_five', 'bn_six', 'bn_seven', 'bn_eight', 'bn_nine', 'bn_zero.pnum', 'bn_one.pnum', 'bn_two.pnum', 'bn_three.pnum', 'bn_four.pnum', 'bn_five.pnum', 'bn_six.pnum', 'bn_seven.pnum', 'bn_eight.pnum', 'bn_nine.pnum', 'bn_rupeemark', 'bn_rupeesign', 'bn_danda', 'bn_doubledanda', 'bn_currency1', 'bn_currency2', 'bn_currency3', 'bn_currency4', 'bn_currencyless', 'bn_currency16', 'bn_isshar', 'bn_k_ka', 'bn_k_tta', 'bn_k_tt_ra', 'bn_k_ta', 'bn_k_t_ba', 'bn_k_t_ra', 'bn_k_na', 'bn_k_ba', 'bn_k_ma', 'bn_k_ra', 'bn_k_ra.alt01', 'bn_k_la', 'bn_k_ssa', 'bn_k_ss_nna', 'bn_k_ss_ba', 'bn_k_ss_ma', 'bn_k_ss_ra', 'bn_k_sa', 'bn_kh_ba', 'bn_kh_ra', 'bn_ga_ukaar', 'bn_g_ga', 'bn_g_da', 'bn_g_dha', 'bn_g_dh_ba', 'bn_g_dh_ra', 'bn_g_na', 'bn_g_ba', 'bn_g_ma', 'bn_g_ra', 'bn_g_ra_ukaar', 'bn_g_ra_uukaar', 'bn_g_la', 'bn_gh_na', 'bn_gh_ba', 'bn_gh_ra', 'bn_ng_ka', 'bn_ng_k_ra', 'bn_ng_k_ssa', 'bn_ng_k_ss_ra', 'bn_ng_kha', 'bn_ng_ga', 'bn_ng_g_ra', 'bn_ng_gha', 'bn_ng_gh_ra', 'bn_ng_ma', 'bn_ng_ra', 'bn_c_ca', 'bn_c_cha', 'bn_c_ch_ba', 'bn_c_ch_ra', 'bn_c_nya', 'bn_c_ra', 'bn_ch_ba', 'bn_ch_ra', 'bn_j_ja', 'bn_j_j_ba', 'bn_j_jha', 'bn_j_nya', 'bn_j_ba', 'bn_j_ra', 'bn_jh_ra', 'bn_ny_ca', 'bn_ny_cha', 'bn_ny_ja', 'bn_ny_jha', 'bn_ny_ra', 'bn_tt_tta', 'bn_tt_ba', 'bn_tt_ra', 'bn_tth_ra', 'bn_dd_dda', 'bn_dd_ra', 'bn_ddh_ra', 'bn_nn_tta', 'bn_nn_ttha', 'bn_nn_dda', 'bn_nn_dda.alt01', 'bn_nn_dd_ra', 'bn_nn_ddha', 'bn_nn_nna', 'bn_nn_ba', 'bn_nn_ma', 'bn_nn_ra', 'bn_t_ta', 'bn_t_t_ba', 'bn_t_t_ra', 'bn_t_tha', 'bn_t_na', 'bn_t_ba', 'bn_t_ma', 'bn_t_ra', 'bn_t_ra.alt01', 'bn_t_ra_ukaar', 'bn_t_ra_uukaar', 'bn_th_ba', 'bn_th_ra', 'bn_th_ra_ukaar', 'bn_th_ra_uukaar', 'bn_th_la', 'bn_d_ga', 'bn_d_gha', 'bn_d_da', 'bn_d_d_ba', 'bn_d_dha', 'bn_d_dh_ba', 'bn_d_na', 'bn_d_ba', 'bn_d_bha', 'bn_d_bh_ra', 'bn_d_ma', 'bn_d_ra', 'bn_d_ra_ukaar', 'bn_d_ra_uukaar', 'bn_dh_na', 'bn_dh_ba', 'bn_dh_ra', 'bn_dh_ra_ukaar', 'bn_dh_ra_uukaar', 'bn_n_k_ta', 'bn_n_jha', 'bn_n_tta', 'bn_n_tt_ra', 'bn_n_ttha', 'bn_n_dda', 'bn_n_dd_ra', 'bn_n_ta', 'bn_n_t_ba', 'bn_n_t_ra', 'bn_n_tha', 'bn_n_da', 'bn_n_d_ba', 'bn_n_d_ra', 'bn_n_dha', 'bn_n_dh_ba', 'bn_n_dh_ra', 'bn_n_na', 'bn_n_ba', 'bn_n_ma', 'bn_n_ra', 'bn_n_sa', 'bn_p_tta', 'bn_p_ta', 'bn_p_t_ra', 'bn_p_na', 'bn_p_pa', 'bn_p_ra', 'bn_p_ra_ukaar', 'bn_p_ra_uukaar', 'bn_p_la', 'bn_p_sa', 'bn_ph_tta', 'bn_ph_ra', 'bn_ph_la', 'bn_b_ja', 'bn_b_da', 'bn_b_dha', 'bn_b_ba', 'bn_b_bha', 'bn_b_ra', 'bn_b_ra_ukaar', 'bn_b_ra_uukaar', 'bn_b_da_ukaar', 'bn_b_da_uukaar', 'bn_b_la', 'bn_bh_ra', 'bn_bh_ra_ukaar', 'bn_bh_ra_uukaar', 'bn_bh_la', 'bn_m_na', 'bn_m_pa', 'bn_m_p_ra', 'bn_m_pha', 'bn_m_ba', 'bn_m_bha', 'bn_m_bh_ra', 'bn_m_ma', 'bn_m_ra', 'bn_m_la', 'bn_y_ra', 'bn_ra_ukaar', 'bn_ra_uukaar', 'bn_l_ka', 'bn_l_ga', 'bn_l_ga_ukaar', 'bn_l_tta', 'bn_l_dda', 'bn_l_da', 'bn_l_pa', 'bn_l_pha', 'bn_l_ba', 'bn_l_ma', 'bn_l_ra', 'bn_l_la', 'bn_l_sa', 'bn_sha_ukaar', 'bn_sh_ca', 'bn_sh_cha', 'bn_sh_tta', 'bn_sh_na', 'bn_sh_ba', 'bn_sh_ma', 'bn_sh_ra', 'bn_sh_ra_iikaar', 'bn_sh_ra_ukaar', 'bn_sh_ra_uukaar', 'bn_sh_la', 'bn_ss_ka', 'bn_ss_k_ra', 'bn_ss_tta', 'bn_ss_tt_ra', 'bn_ss_ttha', 'bn_ss_nna', 'bn_ss_pa', 'bn_ss_p_ra', 'bn_ss_pha', 'bn_ss_ba', 'bn_ss_ma', 'bn_ss_ra', 'bn_s_ka', 'bn_s_k_ba', 'bn_s_k_ra', 'bn_s_kha', 'bn_s_tta', 'bn_s_tt_ra', 'bn_s_ta', 'bn_s_ta_ukaar', 'bn_s_t_ba', 'bn_s_t_ra', 'bn_s_tha', 'bn_s_na', 'bn_s_pa', 'bn_s_p_ra', 'bn_s_p_la', 'bn_s_pha', 'bn_s_ba', 'bn_s_ma', 'bn_s_ra', 'bn_s_ra_ukaar', 'bn_s_ra_uukaar', 'bn_s_la', 'bn_ha_ukaar', 'bn_ha_rikaar', 'bn_h_nna', 'bn_h_na', 'bn_h_ba', 'bn_h_ma', 'bn_h_ra', 'bn_h_la', 'bn_h_yya', 'bn_rr_ga', 'asa_ra_ukaar', 'asa_ra_uukaar', 'asa_ba_ukaar', 'asa_ba_uukaar', 'bn_reph', 'bn_iikaar_reph', 'bn_aumark_reph', 'bn_ba_phala', 'bn_ya_phala', 'bn_ra_phala', 'uni25CC', 'uni20B9.rupee', 'bn_ikaar.fl.wi2', 'bn_ikaar.fl.wi1', 'bn_ikaar.fl', 'bn_da_ukaar', 'bn_da_uukaar', 'bn_ka.half', 'bn_kha.half', 'bn_ga.half', 'bn_gha.half', 'bn_nga.half', 'bn_ca.half', 'bn_cha.half', 'bn_ja.half', 'bn_jha.half', 'bn_nya.half', 'bn_tta.half', 'bn_ttha.half', 'bn_dda.half', 'bn_ddha.half', 'bn_nna.half', 'bn_ta.half', 'bn_tha.half', 'bn_da.half', 'bn_dha.half', 'bn_na.half', 'bn_pa.half', 'bn_pha.half', 'bn_ba.half', 'bn_bha.half', 'bn_ma.half', 'bn_ya.half', 'bn_ra.half', 'bn_la.half', 'bn_sha.half', 'bn_ssa.half', 'bn_sa.half', 'bn_ha.half', 'bn_rra.half', 'bn_rha.half', 'bn_yya.half', 'asa_ra.half', 'asa_ba.half', 'bn_k_ssa.half', 'bn_j_nya.half', 'bn_ukaar.alt', 'bn_uukaar.alt', 'uni200C', 'uni200D']

f.glyphOrder = gO
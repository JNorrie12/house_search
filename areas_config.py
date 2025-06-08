london_areas = { 
    'chingford' : f'USERDEFINEDAREA%5E%7B%22polylines%22%3A%22qx%7EyHtoDhi%40geA%7ED%7DnArBeW_Y%7D%60Aij%40pGi%5EjD%7DFsOuKwIiOsHiW_F_DkZ%7Dh%40%7E%5B_OjnAsIr%60Bn%7DCdwB%7EWm%5B%22%7D',
    'walthamstow' : f'USERDEFINEDAREA%5E%7B%22polylines%22%3A%22cy%7CyHaXhqAcf%40jVj_A~L%7Cb%40hHxJ~GbW~PxYtx%40%60zCuo%40jq%40uw%40e_%40s%60%40bO_iAoM%7B%5C%5CgRUm%60AtIuWk%40kp%40jFmTUg%7D%40zLkw%40%22%7D',
    'leytonstone' : f'USERDEFINEDAREA%5E%7B"polylines"%3A"ycvyHdsFtjAi~C%5Eki%40~NwXhTgm%40uUo%7CBuaAk%40%7Db%40PiUpGuMtm%40_%60%40vXiYrcA~Ptm%40~DnFhEnTtT%7C%5BrL%7Cq%40%60e%40%60_B%7CBg%40"%7D',
    'wanstead': f'USERDEFINEDAREA%5E%7B%22polylines%22%3A%22i%7BvyHsxBuEceCuiCnU_QbOsKlq%40rCbm%40Sdn%40hzA%60%40toAip%40%22%7D',
    'woodford': f'USERDEFINEDAREA%5E%7B"id"%3A"9561632"%7D',
    'loughton': f'USERDEFINEDAREA%5E%7B"id"%3A"9561644"%7D',
    'theydon_bois': f'USERDEFINEDAREA%5E%7B"id"%3A"10679248"%7D',
    'epping': f'USERDEFINEDAREA%5E%7B%22polylines%22%3A%22adpzHeaQxz%40%7Dx%40%7CZq_B%7DZg%7D%40i%7BB%7BKsQ%7CsBbrAtoB%22%7D',
    'cheshunt': f'USERDEFINEDAREA%5E%7B%22polylines%22%3A%22msnzHhuFr%40%7Ba%40%7CUo%5C%5C~AcWeuD_%5C%5C%5EpiAUpNf%5Dlb%40hZ~MpP%60%40rNjDp~%40o%5C%5C%22%7D',
    'isle_of_dogs': f'USERDEFINEDAREA%5E%7B%22polylines%22%3A%22s_kyHxwD_Km%5BhKqs%40i%40_z%40uA%7DLjIgJ%60t%40fJl_%40gQva%40vBtQvkAwUnz%40a%5E%60%5Dka%40%60%40kc%40s%40aTtA%22%7D',
    'surrey_quays': f'USERDEFINEDAREA%5E%7B"id"%3A"10679272"%7D',
    'nunhead': f'USERDEFINEDAREA%5E%7B"polylines"%3A"%7DedyHfkE%60W_%60%40lViz%40zNjt%40dGtm%40qBhw%40jLpNuGpNtHtLk_%40%7C%7C%40qR_%60%40aLqR_SnF%7BHmj%40k%40o%5C%5CiEuWdSc%5B"%7D',
    'putney': f'USERDEFINEDAREA%5E%7B"polylines"%3A"m_cyH~wh%40w%5Bhl%40%7BLfaAl%5CpNfRf%7C%40pqAlEtr%40sx%40%7D%5C%7BsAse%40gsAuJuf%40yf%40YgSlgA"%7D',
    'wimbledon' : f'USERDEFINEDAREA%5E%7B"polylines"%3A"ukyxH%7C%7Bo%40ob%40yv%40kNmlBmsCbOi%5EehBaPukAptAuPhbB%7Di%40xg%40g%60%40~mA%7C_DjFhoC%60Vdu%40og%40vQwYrl%40eS%60%40"%7D',
}

non_london_areas = {
    'tunbridge_wells': f'USERDEFINEDAREA%5E%7B"id"%3A"10736848"%7D',
    'tonbridge': f'USERDEFINEDAREA%5E%7B"id"%3A"9441117"%7D',
    'chelmsford': f'USERDEFINEDAREA%5E%7B"id"%3A"10736863"%7D',
    'colchester': f'USERDEFINEDAREA%5E%7B"id"%3A"9621809"%7D',
    'bishops_stortford': f'USERDEFINEDAREA%5E%7B"id"%3A"9441123"%7D',
    'cambridge': f'USERDEFINEDAREA%5E%7B"id"%3A"9441141"%7D',
    'st_albans': f'USERDEFINEDAREA%5E%7B"id"%3A"9441150"%7D',
    'seven_oaks' : f'USERDEFINEDAREA%5E%7B"polylines"%3A"qs_xHkqZpdFyqHaGy%7DCkdEknAc%7DBnc%40wQ%60qDjcAxdGjs%40rcA"%7D',
    'winchester' : f'USERDEFINEDAREA%5E%7B"polylines"%3A"wlpvHb~iGnLobFw_A_kFuuBucAi%7DAd~E_Zv_CfbHfsD"%7D'
}

def area_csv_path(area_name: str, date) -> str:
    return f"./data/property_prices_{date}_{area_name}.csv"
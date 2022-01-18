var $ = django.jQuery;


$(document).ready(function(){
	//Garante que estÃ¡ no change_form
	if($('#id_client').length){
		customizeForm();
	};
});

/*
	Esta função faz com que as divs da URL e do Estabelecimento
	apareÃ§am/sumam dependendo da opção escolhida no campo "Tipo"
 */
function customizeForm() {
	var range_select = $('#id_status');

    //Divs a serem exibidas/escondidas
	var div_date_expiration = $('.field-date_expiration');
	var div_overdraft_value = $('.field-overdraft_value');
	var div_financing_amount = $('.field-financing_amount');
	var div_scheduled_date = $('.field-scheduled_date');
	var div_company = $('.field-company');
	var div_reason = $('.field-reason');
	var div_released_amount_card = $('.field-released_amount_card');
	var div_appraised_value = $('.field-appraised_value');
	var div_value = $('.field-value');
	var div_value_parcel_siric = $('.field-value_parcel_siric');
	var div_subsidy_value = $('.field-subsidy_value');
	var div_value_fgts = $('.field-value_fgts');
	var div_amortization = $('.field-amortization');
	var div_deadline = $('.field-deadline');
	var div_restriction_date = $('.field-restriction_date');
	var div_date = $('.field-date');


	showOrHide();

	range_select.change(
		function(){
			showOrHide();
		}
	);

	function showOrHide() {
		var opt = $('#id_status option:selected').val();

        switch(opt){
		case 'Aprovado Habitacional':
            $(div_date_expiration).show();
            $(div_financing_amount).show();
            $(div_value_parcel_siric).show();
            $(div_subsidy_value).show();
            $(div_value_fgts).show();
            $(div_amortization).show();
            $(div_deadline).show();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_overdraft_value).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            $(div_scheduled_date).hide();
		    break;

	    case 'Aprovado Comercial':
            $(div_date_expiration).show();
            $(div_released_amount_card).show();
            $(div_overdraft_value).show();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_scheduled_date).hide();
            $(div_value_parcel_siric).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_deadline).hide();
            $(div_financing_amount).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
		    break;

	    case 'Conforme':
	        $(div_deadline).hide();
            $(div_date).show();
            $(div_scheduled_date).show();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'Vistoria':
            $(div_date).show();
            $(div_scheduled_date).show();
            $(div_appraised_value).show();
            $(div_date_expiration).show();
            $(div_financing_amount).hide();
            $(div_scheduled_date).hide();
            $(div_deadline).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;

        case 'Restricao':
            $(div_date).show();
            $(div_scheduled_date).hide();
            $(div_deadline).hide();
            $(div_appraised_value).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).show();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_value).show();
            $(div_restriction_date).show();
            break;


        case 'Pendente Documento':
            $(div_deadline).hide();
            $(div_date).show();
            $(div_scheduled_date).hide();
            $(div_appraised_value).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).show();
            $(div_released_amount_card).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;

        case 'Inconforme':
            $(div_date).show();
            $(div_scheduled_date).hide();
            $(div_deadline).hide();
            $(div_appraised_value).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).show();
            $(div_released_amount_card).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;

        case 'Reprovado':
            $(div_date).show();
            $(div_scheduled_date).hide();
            $(div_appraised_value).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_deadline).hide();
            $(div_released_amount_card).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'Internalizado':
            $(div_date).show();
            $(div_deadline).hide();
            $(div_scheduled_date).hide();
            $(div_appraised_value).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).show();
            $(div_released_amount_card).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'Pendente Critica':
            $(div_date).show();
            $(div_deadline).hide();
            $(div_scheduled_date).hide();
            $(div_appraised_value).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'Desistiu':
            $(div_date).show();
            $(div_scheduled_date).hide();$(div_date).show();
            $(div_deadline).hide();
            $(div_date_expiration).hide();
            $(div_scheduled_date).hide();
            $(div_overdraft_value).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            $(div_appraised_value).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).show();
            $(div_released_amount_card).hide();
            $(div_value).hide();
            $(div_deadline).hide();
            $(div_restriction_date).hide();
            break;

	    case 'Assinar Formularios':
            $(div_date).show();
            $(div_deadline).hide();
            $(div_date_expiration).hide();
            $(div_scheduled_date).hide();
            $(div_overdraft_value).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;

        case 'Em Analise':
            $(div_date).show();
            $(div_date_expiration).hide();
            $(div_scheduled_date).hide();
            $(div_overdraft_value).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            $(div_deadline).hide();
            break;

        case 'Garantia Analise CEHOP':
            $(div_date).show();
            $(div_deadline).hide();
            $(div_date_expiration).hide();
            $(div_overdraft_value).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;

        case 'Garantia Inconforme':
            $(div_date).show();
            $(div_date_expiration).hide();
            $(div_overdraft_value).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_deadline).hide();
            $(div_restriction_date).hide();
            break;

        case 'Garantia Conforme':
            $(div_date).show();
            $(div_deadline).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_overdraft_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'Reavaliar':
            $(div_date).show();
            $(div_deadline).hide();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_overdraft_value).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'Contrato Assinado':
            $(div_date).show();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_deadline).hide();
            $(div_overdraft_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'Registrado':
            $(div_date).show();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_deadline).hide();
            $(div_overdraft_value).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            break;


        case 'QV Solicitado':
            $(div_date).show();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_overdraft_value).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_deadline).hide();
            $(div_restriction_date).hide();
            break;

        case 'Baixa FGTS':
            $(div_date).show();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_overdraft_value).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_restriction_date).hide();
            $(div_deadline).hide();
            break;

        case 'Enviado CEHOP':
            $(div_date).show();
            $(div_date_expiration).hide();
            $(div_financing_amount).hide();
            $(div_value_parcel_siric).hide();
            $(div_subsidy_value).hide();
            $(div_value_fgts).hide();
            $(div_amortization).hide();
            $(div_company).hide();
            $(div_reason).hide();
            $(div_overdraft_value).hide();
            $(div_released_amount_card).hide();
            $(div_appraised_value).hide();
            $(div_value).hide();
            $(div_deadline).hide();
            $(div_restriction_date).hide();
            break;
		}
	}
}

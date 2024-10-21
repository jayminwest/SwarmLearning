import logging

logger = logging.getLogger(__name__)

# Transfer functions
def transfer_to_delegator(text=""):
    logger.info("Transferring control to Delegator")
    from .DelegatorAgent import delegator_agent
    return delegator_agent

def transfer_to_tagging_agent(text=""):
    logger.info("Transferring control to Tagging Agent")
    from .TaggingAgent import tagging_agent
    return tagging_agent

def transfer_to_linking_agent(text=""):
    logger.info("Transferring control to Linking Agent")
    from .LinkingAgent import linking_agent
    return linking_agent

def transfer_to_organization_agent(text=""):
    logger.info("Transferring control to Organization Agent")
    from .OrganizationAgent import organization_agent
    return organization_agent

def transfer_to_typo_correction_agent(text=""):
    logger.info("Transferring control to Typo Correction Agent")
    from .TypoCorrectionAgent import typo_correction_agent
    return typo_correction_agent

def transfer_to_reference_management_agent(text=""):
    logger.info("Transferring control to Reference Management Agent")
    from .ReferenceManagementAgent import reference_management_agent
    return reference_management_agent

def transfer_to_content_review_agent(text=""):
    logger.info("Transferring control to Content Review Agent")
    from .ContentReviewAgent import content_review_agent
    return content_review_agent

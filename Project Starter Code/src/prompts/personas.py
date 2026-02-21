"""
Legal Persona Definitions for AI Agents
========================================
CRITICAL: The agents don't have personalities!
They don't know who they are or how to analyze legal cases.

Your mission: Give them expert personas in TODOs 6, 7, and 8.
"""

from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class LegalPersonas:
    """
    Manages legal expert personas for the AI system.

    CURRENT STATE: BROKEN
    - Agents have no personality
    - They can't provide expert analysis
    - They don't know their specializations

    YOUR MISSION: Create three distinct expert personas!
    """

    def __init__(self):
        """Initialize the personas."""
        self.personas = {
            "IP_Litigation_Expert": self._create_IP_Litigation_Expert_persona(),
            "IP_Valuation_Specialist": self._create_IP_Valuation_Specialist_persona(),
            "Patent_Researcher": self._create_Patent_Researcher_persona()
        }
        logger.info(f"Loaded {len(self.personas)} legal personas")

    def _create_IP_Litigation_Expert_persona(self) -> str:

        # TODO 6: Create complete Business Analyst persona
        # YOUR CODE HERE (approximately 150-200 words)
        # Remember to:
        # - Define the role clearly
        # - List specific expertise areas
        # - Describe communication style
        # - Include relevant frameworks
        # - Explain analytical approach

        # BROKEN PLACEHOLDER - REPLACE THIS!
        persona = """You are a Senior IP Litigation Expert with 15+ years of experience specializing in intellectual property disputes, patent infringement cases, and commercial litigation strategy. Your expertise spans quantitative damages analysis, liability assessment, and forensic financial evaluation in high-stakes IP cases.

        Your areas of expertise include:
        - Patent infringement liability analysis with claim-by-claim evaluation
        - Damage calculation using the Georgia-Pacific factors (15-factor reasonable royalty framework)
        - Lost profits quantification using the Panduit test (demand, acceptable substitutes, capacity, profit amount)
        - Market sizing and TAM/SAM/SOM analysis for technology IP portfolios
        - Financial modeling including NPV, DCF, and ROI projections for litigation outcomes
        - Willful infringement and enhanced damages assessment under 35 U.S.C. § 284

        Communication style: You are data-driven and precise. Every claim is backed by specific numbers, percentages, dollar ranges, and statistical confidence intervals. You present findings in structured tables and use quantitative evidence to support conclusions. You avoid vague language and instead provide measurable metrics.

        Your analytical approach follows this framework:
        1. Identify each cause of action and evaluate the strength of evidence for each element
        2. Assess liability probability using precedent analysis and claim construction
        3. Calculate potential damages across all applicable categories (actual, statutory, punitive)
        4. Present ranges with confidence intervals rather than single-point estimates
        5. Cross-validate conclusions using multiple independent legal and financial methodologies

        You always cite specific legal frameworks by name, explain your methodology transparently, and flag assumptions that could materially affect case outcomes."""

        return persona

    def _create_IP_Valuation_Specialist_persona(self) -> str:
        """
        TODO 7: Create the Market Researcher persona.

        CURRENT STATE: Generic placeholder with no expertise

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Lead Legal Market Researcher for IP disputes
        2. Expertise areas: Competitive intelligence, patent landscapes, prior art
        3. Communication style: Technical, references specific patents and companies
        4. Analytical frameworks: Patent citation analysis, technology S-curves, etc.
        5. Specific approach to competitive analysis

        The persona should:
        - Start with "You are a Lead Legal Market Researcher..."
        - Focus on competitive dynamics and market positioning
        - Include technology trend analysis
        - Reference specific analytical tools
        - Describe approach to prior art and patent analysis

        This researcher focuses on competitive landscape, prior art, and market dynamics.
        They should identify specific companies, patents, and technology trends.
        """

        # TODO 7: Create complete Market Researcher persona
        # YOUR CODE HERE (approximately 150-200 words)
        # Remember to:
        # - Define the role with market research focus
        # - List competitive intelligence expertise
        # - Describe technical communication style
        # - Include patent analysis frameworks
        # - Explain competitive analysis approach

        # BROKEN PLACEHOLDER - REPLACE THIS!
        persona = """You are a Lead IP Valuation Specialist with deep expertise in intellectual property valuation, patent portfolio assessment, and technology market analysis. You specialize in determining the economic value of IP assets, mapping competitive patent landscapes, and identifying prior art that affects case positioning.

        Your areas of expertise include:
        - Patent portfolio valuation using income, market, and cost approaches
        - Prior art identification through systematic database searches and citation analysis
        - Competitive intelligence on IP strategies, licensing programs, and patent assertion
        - Technology S-curve analysis to assess innovation maturity and market disruption potential
        - Industry and market analysis using Porter's Five Forces framework for competitive dynamics
        - Licensing rate benchmarking and comparable transaction analysis across technology sectors

        Communication style: You are technical and evidence-based, always referencing specific patents by number, naming competitor companies explicitly, and citing concrete market data and valuation metrics. You present findings as structured valuation briefs with clear methodology attribution. You distinguish between established facts and analytical inferences.

        Your analytical approach follows this framework:
        1. Map the relevant patent landscape and identify key players and their IP positions
        2. Conduct systematic prior art searches across patent databases and technical literature
        3. Analyze competitive positioning including market share, technology differentiation, and licensing activity
        4. Apply appropriate valuation methodologies with documented assumptions and comparables
        5. Synthesize findings into actionable intelligence on IP value and competitive implications

        You always ground your analysis in verifiable data sources, identify gaps in the valuation picture, and highlight areas where additional investigation would strengthen the IP position."""

        return persona

    def _create_Patent_Researcher_persona(self) -> str:
        """
        TODO 8: Create the Strategic Consultant persona.

        CURRENT STATE: Generic placeholder with no expertise

        Requirements:
        Create a detailed persona (minimum 150 words) that includes:
        1. Role definition: Principal Strategic Consultant for legal strategy
        2. Expertise areas: Risk assessment, settlement strategy, strategic planning
        3. Communication style: Executive-level, focuses on business outcomes and ROI
        4. Analytical frameworks: Game theory, decision trees, risk matrices
        5. Specific approach to strategic recommendations

        The persona should:
        - Start with "You are a Principal Strategic Consultant..."
        - Focus on strategic implications and business value
        - Include risk assessment methodologies
        - Provide actionable recommendations
        - Think multiple moves ahead

        This consultant focuses on strategy, risk, and implementation planning.
        They should provide specific action items, timelines, and success metrics.
        """

        # TODO 8: Create complete Strategic Consultant persona
        # YOUR CODE HERE (approximately 150-200 words)
        # Remember to:
        # - Define the role with strategic focus
        # - List risk and strategy expertise
        # - Describe executive communication style
        # - Include strategic frameworks
        # - Explain recommendation approach

        # BROKEN PLACEHOLDER - REPLACE THIS!
        persona = """
        You are a Principal Patent Researcher and Strategic IP Advisor with extensive experience guiding Fortune 500 companies and law firms through complex patent disputes, risk evaluation, and IP strategy development. You specialize in translating deep patent research into actionable business strategies with measurable ROI.

        Your areas of expertise include:
        - Patent claim analysis and freedom-to-operate assessment for strategic risk evaluation
        - Litigation risk assessment using probability-weighted decision trees and risk matrices
        - Settlement strategy optimization through game theory and negotiation analysis
        - Strategic planning for IP portfolio monetization, defensive positioning, and licensing programs
        - Business impact analysis including revenue protection, market access, and competitive advantage
        - Implementation planning with clear timelines, resource requirements, and success metrics

        Communication style: You communicate at the executive level, focusing on strategic implications, business outcomes, and ROI rather than purely technical patent details. You present recommendations as prioritized action items with estimated costs, timelines, and expected returns. You frame risks in terms of business impact and probability.

        Your analytical approach follows this framework:
        1. Conduct thorough patent research including claim scope, prosecution history, and validity
        2. Evaluate risk across multiple dimensions using probability and impact scoring
        3. Model decision scenarios using game theory to anticipate opposing party responses
        4. Develop prioritized recommendations with specific implementation steps and resource requirements
        5. Define success metrics and monitoring checkpoints for ongoing strategy evaluation

        You always think multiple moves ahead, consider second-order effects of each recommendation, and ensure every strategic action item has a clear owner, timeline, and measurable outcome.
        """

        return persona

    def get_persona(self, persona_type: str) -> str:
        """
        Retrieve a specific persona prompt.

        Args:
            persona_type: Type of persona to retrieve

        Returns:
            The complete persona prompt

        Raises:
            ValueError: If persona_type is not recognized
        """
        if persona_type not in self.personas:
            raise ValueError(f"Unknown persona type: {persona_type}. "
                           f"Available personas: {list(self.personas.keys())}")
        return self.personas[persona_type]

    def get_all_personas(self) -> Dict[str, str]:
        """Get all available personas."""
        return self.personas.copy()

    def validate_persona(self, persona_text: str) -> Dict[str, Any]:
        """
        Validate that a persona meets quality criteria.

        Args:
            persona_text: The persona prompt text to validate

        Returns:
            Dict containing validation results
        """
        validation_results = {
            "has_role_definition": False,
            "has_expertise_areas": False,
            "has_communication_style": False,
            "has_frameworks": False,
            "sufficient_length": False,
            "score": 0.0,
            "feedback": []
        }

        # Check for role definition
        if "you are" in persona_text.lower():
            validation_results["has_role_definition"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing role definition")

        # Check for expertise areas
        if "expertise" in persona_text.lower() or "specialize" in persona_text.lower():
            validation_results["has_expertise_areas"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing expertise areas")

        # Check for communication style
        if "communication style" in persona_text.lower() or "style" in persona_text.lower():
            validation_results["has_communication_style"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing communication style")

        # Check for analytical frameworks
        if "framework" in persona_text.lower() or "approach" in persona_text.lower():
            validation_results["has_frameworks"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append("Missing analytical frameworks")

        # Check length
        word_count = len(persona_text.split())
        if word_count >= 150:
            validation_results["sufficient_length"] = True
            validation_results["score"] += 0.2
        else:
            validation_results["feedback"].append(f"Too short: {word_count} words (minimum 150)")

        # Overall assessment
        if validation_results["score"] >= 0.8:
            validation_results["feedback"].insert(0, "Persona meets quality standards")
        else:
            validation_results["feedback"].insert(0, "Persona needs improvement")

        return validation_results


# Helper function for testing
def test_personas():
    """Test that all personas are properly defined."""
    personas = LegalPersonas()

    print("Testing Legal Personas\n" + "="*50)

    for persona_type in ["business_analyst", "market_researcher", "strategic_consultant"]:
        print(f"\nTesting {persona_type}:")
        persona_text = personas.get_persona(persona_type)
        validation = personas.validate_persona(persona_text)

        print(f"  Score: {validation['score']:.1f}/1.0")
        print(f"  Word count: {len(persona_text.split())} words")

        if validation['score'] >= 0.8:
            print("  ✅ PASSED")
        else:
            print("  ❌ FAILED")
            for feedback in validation['feedback']:
                print(f"    - {feedback}")

    return True


if __name__ == "__main__":
    test_personas()

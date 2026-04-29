Title: Frequently Asked Questions
template: slide
save_as: faq.html

Here we list some common questions. If you have a question not found here, you can always reach out to the <a href="helpdesk.html#content">Helpdesk</a>.

**How do I convert a TESS magnitude into a flux?**
<p style="margin-left: 2em">The flux in e-/s can be estimated via the following equation:</p>

<p style="margin-left: 4em">Flux [e-/s] = 10<sup>[(20.44-Tmag)/2.5]</sup></p>

<p style="margin-left: 2em">This is derived from the values presented on page 37 of the <a href = 'https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/active-missions/tess/_documents/TESS_Instrument_Handbook_v0.1.pdf'>Instrument hand book</a>.</p>

**Is there proprietary period on TESS data?**

<p style="margin-left: 2em">No, all TESS data becomes immediately public when it arrives in the TESS archive <a href = 'https://archive.stsci.edu/tess/'>MAST</a>. The approximate date of data availability for a given sector can be found <a href = 'https://outerspace.stsci.edu/display/TESS/TESS+Holdings+Available+by+MAST+Service'> here</a>.</p>

**What if I have an interesting and timely target that needs to be observed quickly and in short-cadence?**

<p style="margin-left: 2em">Target of opportunity proposals are solicited for rapidly evolving phenomena whose occurrence is not predictable at the time of the GI proposal deadline. These proposals would commence after the spacecraft upload following the trigger event, which could be as long as 2 months after the event. The impact to science of such a potential delay must be addressed in proposals requesting ToO observations. These proposals may be submitted during the regular cycle and are eligible for funding.</p>

<p style="margin-left: 2em">Additionally, a fraction of the GI targets will be reserved for rapid turn-around, Director's Discretionary Time (DDT). If your target can't wait for the next GI proposal cycle, then DDT is the route for you. Keep in mind that (i) targets need to be submitted about 6 weeks before they can to be observed; and (ii) the spacecraft has to be observing the corresponding region of the sky.</p>

**Where can I send my suggestion for an idea I'd like to see incorporated into the TESS GI program, or a software tool I'd like to suggest be developed?**

<p style="margin-left: 2em">We love feedback! Please contact our <a href="helpdesk.html">helpdesk</a> with any suggestions or questions.</p>

**I see an interesting feature in my TESS light curve. What could it be?**

<p style="margin-left: 2em">Some common sources of anomalous light curves features include the target star being on a bad CCD column, scattered light from the Earth and/or Moon, or asteroids quickly crossing your target. It is recommended that Full-Frame Images taken at the same time as the anomalous feature be checked to verify whether or not the interesting feature seen is astrophysical in nature. The <a href = "https://lightkurve.github.io/lightkurve/tutorials/1-getting-started/interactively-inspecting-data.html"> lighkurve package</a> can also be used to interactively inspect the region surrounding your target.</p>

**Is there a standard acknowledgement to use when publishing TESS data?**

<p style="margin-left: 2em">In your acknowledgments, please add "This paper includes data collected by the TESS mission, which are publicly available from the Mikulski Archive for Space Telescopes (MAST). Funding for the TESS mission is provided by NASA's Science Mission directorate."</p>

<p style="margin-left: 2em">It is also encouraged to consider making a DOI of the TESS datasets you used in your work.  This allows other users to retrieve the same exact data sets you used. You can find more information on this process <a href = "https://archive.stsci.edu/publishing/doi">here</a>.</p>

**How do I acknowledge High Level Science Products?**

<p style="margin-left: 2em">For HLSPs, you should acknowledge the primary papers describing the HLSPs.  The <a href="https://archive.stsci.edu/hlsp/"> HLSP homepage</a> for each individual product contians the primary paper reference and the DOI information on the top-left section of the page. On the bottom of the page under the "Citations", you can find more information on the data licence, which conveys how users may use and share the data.</p>

**Depending on the Product, which papers should I cite?**

<p style="margin-left: 2em">You can find useful lists of papers, and acknowledgements on our <a href="citation_guidelines.html">citation guidelines page</a>. This page also provides suggested text for TOIs and points of contact if additional help is needed.</p>

**Where can I find SPOC Data Validation (DV) reports?**

<p>SPOC DV reports can be found via the <a href = "https://archive.stsci.edu/tess/bulk_downloads/bulk_downloads_ffi-tp-lc-dv.html">MAST Bulk downloads page</a> towards the bottom of the page. You may also retrive DV products with Astroquery as shown via a <a href="https://spacetelescope.github.io/mast_notebooks/notebooks/TESS/beginner_astroquery_dv/beginner_astroquery_dv.html">MAST notebook</a>.</p>

<p>Please Note that the difference image test conducted by the SPOC can typically locate the source of the transits to within 2.5 arcsec for reasonably strong transit signals. We recommending using the ticoffset-rm entry from the DV report, which indicates the source offset from the catalog location in arcsec and the significance, in sigma. Dividing the source offset by the significance yields the 1-sigma uncertainty in arcsec.</p>

<p>The out-of-transit (OOT) offset can be compromised in crowded fields and is not recommended as the TIC-offset is usually more reliable. The difference image centroiding test complements high resolution imaging and is usually available well before any follow-up observations are conducted. For multisector searches from June 2025 onwards the joint TIC offset, TicOffset-jnt, is recommended as it is significantly more accurate than the TicOffset-rm metric. The TOI alert date can be found in the TOI Catalog at tev.mit.edu along with QLP, FAINT and SPOC DV reports for each TOI (note the TOI catalog does not include all SPOC DV reports, all of which can be found at MAST).</p>

<p>If you need help running data validation in a forced ephemeris mode to generate DV reports for any additional candidates identified through independent transit searches to help bolster confidence in the detection and planetary classification or to help identify issues with such candidates please reach out to the <a href="helpdesk.html">TESS helpdesk</a>.</p>

**What happens if an extraordinary transient (or other) event happens in the TESS field of view that would benefit from a rapid analysis of TESS data?**

<p style="margin-left: 2em">
When an extraordinary transient event occurs within the TESS field of view, data is analyzed and disseminated to the community via the procedures outlined in <a href="docs/Standard_Processes_for_Rapid_TESS_Data_Release_and_Access_20260219.pdf">this policy document</a>.</p>

